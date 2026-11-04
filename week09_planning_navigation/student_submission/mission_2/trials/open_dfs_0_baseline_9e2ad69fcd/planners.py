"""Mission 1 starter, created in student_submission/mission_1/planners.py.

Open that submission file in your editor and implement the four functions.
The guide creates it automatically and never overwrites an existing file.

Each function receives ctx with start, goal, grid, heuristic(cell) and
expand(cell, frontier_size). Return a list of (row, column) cells including
start and goal, or [] after exhausting the search. Call ctx.expand once per
expanded node. Record the actual frontier size, not the number of visited cells.
The runner enforces an expansion budget and a separate process time limit.
Use only the Python standard library. Do not import planning.reference_path.
When a free start is already the goal, return the single starting cell with
zero moves. No expansion is required for that case. Use the six small checks
on the Mission 1 page before running the full canonical-map evaluation.
"""
from collections import deque
from heapq import heappush, heappop
from planning.core import reconstruct, free


def bfs(ctx):
    """FIFO queue. Mark discovered cells when enqueuing and store parents.
    Use ctx.expand(current, len(frontier)+1) to obtain neighbours.
    BFS minimizes number of unit-cost edges, not execution time on a robot.
    """
    start, goal = ctx.start, ctx.goal
    if not free(ctx.grid, start) or not free(ctx.grid, goal):
        return []
    if start == goal:
        return [start]
    queue = deque([start])
    parent = {start: None}
    while queue:
        current = queue.popleft()                      
        if current == goal:
            return reconstruct(parent, goal)
        for nxt in ctx.expand(current, len(queue) + 1):
            if nxt not in parent:                      
                parent[nxt] = current
                queue.append(nxt)
    return []
    raise NotImplementedError('Implement BFS with a deque and parent dictionary')


def dfs(ctx):
    """LIFO stack. Track discovered cells and parents to avoid cycles.
    A valid DFS path need not be shortest. Keep the supplied neighbour order.
    """
    start, goal = ctx.start, ctx.goal
    if not free(ctx.grid, start) or not free(ctx.grid, goal):
        return []
    if start == goal:
        return [start]
    stack = [start]
    parent = {start: None}
    while stack:
        current = stack.pop()                          
        if current == goal:
            return reconstruct(parent, goal)
        for nxt in ctx.expand(current, len(stack) + 1):
            if nxt not in parent:                      
                parent[nxt] = current
                stack.append(nxt)
    return []
    raise NotImplementedError('Implement DFS with a stack')


def iddfs(ctx):
    """Run depth-limited DFS with bounds 0, 1, 2, ... .
    Prevent cycles on the current path. Do not keep a global visited set across
    depth limits. Count expansions again on every iteration. Return [] only
    after exhaustive failure. Catch no budget exceptions. The runner records
    resource_limit honestly if this expensive method reaches its budget.
    """
    start, goal = ctx.start, ctx.goal
    if not free(ctx.grid, start) or not free(ctx.grid, goal):
        return []
    if start == goal:
        return [start]

    def limited(cell, depth, limit, path, on_path):
        if cell == goal:
            return 'found'
        if depth == limit:
            return 'cutoff'                            
        cutoff = False
        for nxt in ctx.expand(cell, len(path)):
            # cycle check on current path only
            if nxt in on_path:                   
                continue
            path.append(nxt)
            on_path.add(nxt)
            result = limited(nxt, depth + 1, limit, path, on_path)
            if result == 'found':
                return 'found'
            if result == 'cutoff':
                cutoff = True
            path.pop()
            on_path.remove(nxt)
        return 'cutoff' if cutoff else 'fail'

    limit = 0
    while True:                                       
        path = [start]
        result = limited(start, 0, limit, path, {start})
        if result == 'found':
            return path
        if result == 'fail':                           
            return []
        limit += 1
    raise NotImplementedError('Implement iterative deepening with depth-limited DFS')


def astar(ctx):
    """Use a heap ordered by g + ctx.heuristic(cell).
    Keep best g costs and parents. Ignore outdated heap entries. Each edge
    costs 1. Stop when the goal is removed from the priority queue.
    """
    start, goal = ctx.start, ctx.goal
    if not free(ctx.grid, start) or not free(ctx.grid, goal):
        return []
    if start == goal:
        return [start]
    best_g = {start: 0}
    parent = {start: None}
    heap = []
    heappush(heap, (ctx.heuristic(start), 0, start))   
    while heap:
        _, g, current = heappop(heap)
        if g > best_g[current]:                       
            continue
        if current == goal:
            return reconstruct(parent, goal)
        for nxt in ctx.expand(current, len(heap) + 1):
            new_g = g + 1                              
            if new_g < best_g.get(nxt, float('inf')):
                best_g[nxt] = new_g
                parent[nxt] = current
                heappush(heap, (new_g + ctx.heuristic(nxt), new_g, nxt))
    return []
    raise NotImplementedError('Implement A* with Manhattan distance')
