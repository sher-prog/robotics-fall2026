# Mission 2

## Predictions

{'straight': 'travel straight forward for exactly 0.45 meters without turning, since the turning speed is 0', 'rotation': 'remain unchanged since the forward speed is 0.00 m/s, while its direction will turn to the left by exactly 1.5 radians', 'curve': 'right-hand curve that travels 0.60 meters along its arc and turns right by 1.6 radians because it combines a positive forward speed with a negative turning speed', 'curve_modified': 'the turning speed is a positive value instead of negative and the resulting radius of 0.20 m is smaller'}

## Prediction Locks

{'straight': '2026-09-08T01:04:30.624829+00:00', 'rotation': '2026-09-08T01:06:58.130257+00:00', 'curve': '2026-09-08T01:10:34.025397+00:00', 'curve_modified': '2026-09-08T01:12:34.026625+00:00'}

## Motion Comparison

For the straight motion trial, the measured motion closely matched my prediction. The estimated traveled path was approximately 0.45 meters, and the direction change was nearly 0 degrees, which aligns with my calculated prediction.

## Measurement Explanation

The estimated traveled path measures the total distance the robot actually drove along the curved arc. The start to end distance measures the length of a direct, straight line from the starting position to the final position, which is always shorter than the curve.

## Safety Explanation

The command guard checks every proposed driving command to ensure speeds are safe and valid before they reach the robot
The final zero command safely stops the robot at the planned end of a trial by sending a zero forward and turning speed.
The timeout is needed if the program crashes or communication stops, providing a backup mechanism to halt the robot after 0.5 seconds without a new command.

## Modified Settings

{'linear_x': 0.12, 'angular_z': 0.6, 'duration': 4.0}
