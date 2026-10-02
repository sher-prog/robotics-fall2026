# Autosaved responses

- Name: Shernice Chetty
- Student ID: 24063171
- Section: 39536 01 [5485]

## Check-in answers

### m3_prediction

Increasing speed may cause the robot to overshoot the path and increase tracking error because it has less time to react and steer. Too little derivative control may cause the robot to wobble back and forth across the path instead of driving smoothly. Therefore clearance around pedestrians will decrease, increasing the risk that the robot will crash into them.

### m3_technical

I predicted that too much speed or too little derivative control would cause the robot to wobble and overshoot the path, which was correct until the speed was lowered and the gains were tuned. The robot computes its desired heading by calculating the angle from its current estimated position to the next point on the cyan route. The PID controller then looks at the error which is the difference between this desired heading and where the robot is actually pointing and adjusts the left and right wheel speeds to steer the robot correctly. The green and orange paths showed that if the wheel radius is inaccurate, the robot miscalculates how far its wheels have actually moved.

### m3_human

The most consequential failure is the robot crashing into a pedestrian and causing physical injury or tripping them. I would require a trade-off of lowering the robot's speed while maintaining a larger safety clearance zone, because a slower robot has more time to stop or steer away if someone steps into its path. Responsibility belongs to the engineers and development team, because they are the ones writing the code, tuning the controls, and making the final decisions on how the robot operates in the real world.

## Mission explanations

### mission_3

**technical_analysis**: I predicted that too much speed or too little derivative control would cause the robot to wobble and overshoot the path, which was correct until the speed was lowered and the gains were tuned. The robot computes its desired heading by calculating the angle from its current estimated position to the next point on the cyan route. The PID controller then looks at the error which is the difference between this desired heading and where the robot is actually pointing and adjusts the left and right wheel speeds to steer the robot correctly. The green and orange paths showed that if the wheel radius is inaccurate, the robot miscalculates how far its wheels have actually moved.

**human_centered_analysis**: The most consequential failure is the robot crashing into a pedestrian and causing physical injury or tripping them. I would require a trade-off of lowering the robot's speed while maintaining a larger safety clearance zone, because a slower robot has more time to stop or steer away if someone steps into its path. Responsibility belongs to the engineers and development team, because they are the ones writing the code, tuning the controls, and making the final decisions on how the robot operates in the real world.
