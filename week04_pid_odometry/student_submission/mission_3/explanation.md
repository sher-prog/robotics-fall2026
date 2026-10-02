# mission_3 Submission

- Name: shernice chetty
- Section: 01 [5485]

## Explanations

### technical_analysis

My prediction was correct: before tuning, too much speed and low derivative control caused the robot to wobble and overshoot turns, which increased tracking error.
To navigate, the robot calculates the angle from its current position to the next point on the cyan route, and this angle becomes its desired heading command. The PID controller then looks at the error which is the difference between this desired heading and where the robot is actually pointing and adjusts the speeds of the left and right wheels to steer the robot correctly. Finally, if the wheel radius is inaccurate, the robot miscalculates how far its wheels have physically traveled. This means the robot might think it is perfectly following the route in its own calculations (the orange line), while in reality, it is driving in the completely wrong physical location (the green line) because its internal math doesn't match the real world.

### human_centered_analysis

The most consequential failure is the robot hitting or tripping a pedestrian, which could cause a physical injury. For the trade-off, I would require a slower forward speed combined with a larger safety clearance zone. While a slower speed makes the delivery take longer, it gives the robot more time to correct steering errors and ensures it stays far away from people even if it drifts off path. The engineering team is responsible for verifying these decisions before deployment. Because they are the ones writing the code, tuning the controllers, and setting the speed limits, they are ultimately responsible for how safely the physical machine behaves in the real world.