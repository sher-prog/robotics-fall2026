# Mission 1

## Command Path Explanation

A proposed command travels on the /student_cmd_vel topic. The guard receives this command and checks it to make sure the movement is safe. Then it publishes the approved command t the /cmd_vel topic so the simulated robot can actually execute the movement.

## Graph Explanation

A ROS 2 graph shows how different programs in a robot's software system connect and communicate with one another using named data channels. For example in this mission, the /ros_gz_bridge node sends data to the /scan topic

## Guided Checks

{'bridge_info': True, 'command_topics': True, 'guard_info': True, 'node_list': True, 'scan_info': True, 'scan_message': True}

## Scan Observation

I found the ranges list containing mostly .inf values which represent the physical distance measurement in meters  around the robot, with .inf representing that no object was detected within the sensor max range.



## Tools Explanation

Gazebo is responsible for simulating the physical environment, the robots movement and its raw sensor readings while RViz is responsible for visually displaying that ROS 2 data so a person can easily see and understand it
