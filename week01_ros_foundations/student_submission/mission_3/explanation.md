# Mission 3

## Data To Command

front_distance() iterates through the raw LiDAR array, filters out invalid readings and those outside the front angle boundary, and returns the single min distance. decide_velocity() then evaluates this nearest distance, returning 0.0 which is stop if it is below the safety threshold or missing and returning the bounded forward speed if the path is clear

## Missing Data Safety

Stopping is a critical fail-safe behaviour. A lack of valid measurements does not guarantee empty space. It could mean the sensor is blocked, failing or that an obstacle is so close that the LiDAR cannot accurately read through it. 

## System Layers

The suppled ROS node subscribes to raw data from /scan, passes it to the decision functions to calculate a safe velocity and publishes that choice to /student_cmd_vel. The command guard then acts as a safety layer by safely forwarding this command to the actual /cmd_vel topic, while also using like. awatchdog to stop the robot completely if the node crashes or if sensor data stops arriving.
