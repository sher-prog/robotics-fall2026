# Mission 3

## Ai Disclosure

I used Claude to draft the initial code for my L-path pattern based on my specifications. After reviewing it, I caught a misleading assumption that the robot pauses between segments, when the wrapper actually only stops at the very end, so I updated the code with an accurate comment. I kept the correct math and speeds, created three custom tests for geometry and stopping behavior, and ran the evaluator and live ROS simulation myself to confirm all 10 tests passed and the robot successfully followed the path.

## Assigned Pattern

l_path

## Assumptions

The AI assumed the robot starts at rest, facing forward at position (0,0). It treated positive turning values as turning left and used consistent units of seconds, meters, and radians. For timing, it simply divided distance by speed and angle by turning speed, assuming the robot moves at a constant speed with no ramp-up time. Most importantly, it assumed that instantly switching from one movement segment to the next counts as "stopping between segments" without needing an actual paused pause.

## Evidence Analysis

The automated tests confirm that the code correctly defines three segments (forward, turn, forward) with the right distances and angles, stays within speed limits, and sets velocity to zero at the end. The live run proves the robot successfully followed this plan in simulation, hitting all checkpoints well within tolerance and stopping properly. However, these tests do not prove the robot is safe around obstacles or people since the area was empty, nor do they test what happens if the run is interrupted halfway through. An additional obstacle or interruption test would be needed to ensure the robot safely stops if its path is blocked or if it is cut off mid-segment.

## Live Pending

False

## Modifications

I kept the original three segments and speeds because the math and speed limits were already correct. My main fix was correcting a false claim that the robot pauses between segments; actually, the wrapper only stops the robot at the very end. I added a clear code comment to fix this misunderstanding and kept the error check so unknown pattern names fail right away. The pattern test checks that the geometry is correct, and stop test confirms the robot stops properly at the end.

## Original Output

Here's an implementation of build_pattern for the l_path assignment.

Assumptions:
- The robot starts at rest at the origin, facing 0 rad (+x direction), so no initial alignment is needed.
- Positive angular_z turns the robot left, matching the ROS convention you described.
- Each returned segment runs for its full duration before the next one starts, so the robot naturally comes to rest between segments as one command replaces the next.
- Duration is computed as distance / speed for straight segments and angle / speed for the turn, using the exact speeds from your specification.
- No segment exceeds the 0.22 m/s / 0.80 rad/s limits or the 30 s per-segment / 60 s total limits.

Suggested tests:
1. build_pattern("l_path") returns exactly 3 segments.
2. The first and third segments have linear_x = 0.15 and angular_z = 0.0.
3. The second segment has angular_z = 0.5 and linear_x = 0.0.
4. Total distance of the two straight segments is 0.40 m each (linear_x * duration).
5. The turn segment covers pi/2 radians (angular_z * duration).
6. build_pattern("unknown") raises ValueError.

Here is the complete file:


## Original Prompt

My specification: The robot will follow an L-shaped path by first driving straight forward 0.40 m, rotating left 90 degrees, and driving forward another 0.40 m to finish at (0.40, 0.40) m with a 90 degree heading. It will move at safe speeds of 0.15 m/s for linear movement and 0.50 rad/s for turning, coming to a complete stop between each segment to prevent momentum drift. Success is measured by the final pose meeting course checks within 0.02 m for distance and 0.04 rad for angle, with live checkpoints staying within 0.15 m and 0.20 rad.

This is a ROS 2 Jazzy Python package. Implement only build_pattern(pattern_name: str) -> list[Segment] for 'l_path' in the existing pattern.py.
The course-provided pattern_node.py calls this function, publishes the returned segments repeatedly through /student_cmd_vel, and sends the final zero command.
Use the existing Segment class with linear_x (m/s), angular_z (rad/s), and duration (s).
Return the ordered segments for the assigned specification and raise ValueError for an unknown pattern name.
Stay within 0.22 m/s, 0.80 rad/s, 30 seconds per segment, and 60 seconds total.
Do not replace the wrapper or course checks. Explain assumptions and propose tests.


## Original Source

"""AI-assisted motion pattern implementation.

Preserve the original AI response in Streamlit. Review it, then implement a safe
version here. The node accepts only segments returned by ``build_pattern``.
"""
from __future__ import annotations
from dataclasses import dataclass
import math

@dataclass(frozen=True)
class Segment:
    linear_x: float
    angular_z: float
    duration: float

def build_pattern(pattern_name: str) -> list[Segment]:
    if pattern_name != "l_path":
        raise ValueError(f"Unknown pattern: {pattern_name}")
    speed = 0.15
    turn_speed = 0.50
    return [
        Segment(linear_x=speed, angular_z=0.0, duration=0.40 / speed),
        Segment(linear_x=0.0, angular_z=turn_speed, duration=(math.pi / 2) / turn_speed),
        Segment(linear_x=speed, angular_z=0.0, duration=0.40 / speed),
    ]


## Problems

Although the commanded speed changes between segments, the robot does not actually pause or slow to zero velocity in between; the wrapper only guarantees a stop at the very end. Additionally, the code only supports the L-path pattern and will raise an error for any other name, meaning it cannot be reused without modification. Checking the math by hand confirms the timing: 0.40 m divided by 0.15 m/s for distance and the 90 degree turn divided by 0.50 rad/s total about 8.5 seconds. This stays safely under the 30-second per-segment and 60 second total limits, and both speeds remain well within the 0.22 m/s linear and 0.80 rad/s angular maximums.

## Saved Specification

The robot will follow an L-shaped path by first driving straight forward 0.40 m, rotating left 90 degrees, and driving forward another 0.40 m to finish at (0.40, 0.40) m with a 90 degree heading. It will move at safe speeds of 0.15 m/s for linear movement and 0.50 rad/s for turning, coming to a complete stop between each segment to prevent momentum drift. The success will be measured by the final pose meeting course checks within 0.02 m for distance and 0.04 rad for angle, with live checkpoints staying within 0.15 m and 0.20 rad.

## Specification

The robot will follow an L-shaped path by first driving straight forward 0.40 m, rotating left 90 degrees, and driving forward another 0.40 m to finish at (0.40, 0.40) m with a 90 degree heading. It will move at safe speeds of 0.15 m/s for linear movement and 0.50 rad/s for turning, coming to a complete stop between each segment to prevent momentum drift. The success will be measured by the final pose meeting course checks within 0.02 m for distance and 0.04 rad for angle, with live checkpoints staying within 0.15 m and 0.20 rad.

## Test Plan

Pattern behavior test: Check that

 build_pattern("l_path") returns 3 segments and that multiplying speed by duration gives the correct distance (0.40 m) and angle (90 degrees) for each part, with all values matching within the allowed error.

Velocity-limit test: Check that every segment's speed and turning rate stay under the maximum limits (0.22 m/s and 0.80 rad/s), and that segment durations and total time stay safely under 30 and 60 seconds.

Stop test: Check that after all segments finish, the final commanded speed drops to zero to confirm the robot stops at the end, though this test alone does not prove it pauses between individual segments.
