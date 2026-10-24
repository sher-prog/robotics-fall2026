# Mission 2

## Comparison

Strategy 2 (room by room) scored higher: known area 58% vs 44%, quality 83.7 vs 75.7, and fewer wall pieces (59 vs 67). Speckle was a bit worse (6.5% vs 5.0%). Visually, map 1 had a messy ghost copy of the arena from when my robot flipped, and map 2 has one clean outline with the posts inside. My prediction was partly right: continuity was better, but I thought coverage would be about the same, and it was clearly higher. Map 2 is also smaller (39 vs 69 m²), partly because the ghost area inflated map 1.

## Loop Closure

I can't say for sure that a loop closure happened. In map 2, the walls lined up with no doubled lines when I got back near my start, which is what a good loop looks like, but I didn't check for a sudden shift in RViz. Ordinary map growth just adds new cells at the edge. A real loop closure would show up as the whole map snapping or shifting a little at once, and old walls lining up with new scans. In map 1, the doubled arena shows what happens when the robot's position is wrong and nothing corrects it.


## Strategy Prediction

My first strategy was perimeter then interior: I followed the outer wall first, then drove through the middle. My second one is room by room, where I weave through the posts and open areas first and then finish along the walls. I think the second one will give better continuity, because the robot sees each area from several angles in a row. I also expect better loop closure, since I'll end by returning to my starting spot. Coverage will probably be about the same. I'll drive slowly this time so the robot doesn't flip and the map stays clean.

