# Week 6: SLAM and Localization

- name: Shernice Chetty
- email: SHERNICE.CHETTY71@stu-mail.hunter.cuny.edu
- course_id: CSCI 39536

## concepts.prediction

Poor odometry usually shows up as rotational drift when the robot turns, but the scan skews and leaves "ghost" double walls in the map because the predicted pose is way off. Weak scan geometry, like driving down a long, featureless hallway, causes translation slip along that hallway axis because the scan matcher has no perpendicular features to lock onto. To tell them apart in RViz, set the Fixed Frame to odom and check /scan: if scans drift heavily away from the walls during turns, the wheel odometry is bad. If the odom frame looks solid but the robot slides along the hallway in the map frame (or the /particlecloud stretches out into a long ellipse along the corridor), the issue is degenerate scan geometry.

## mission_1.limitations

The left side of the map is the worst. After the robot flipped, the position estimate jumped, so the scans got drawn in the wrong place and it looks like a second, blurry arena. I also never drove close to some of the outer walls, so they have gaps. Driving too fast near the posts caused the flip, and that broke the matching between scans.


## mission_1.map_interpretation

About 44% of the map is known, which is decent for one run. Speckle was low (5%), so there isn't much random noise, and border contact was under 1%. The quality score of 75.7 looks good, but I don't fully trust it. There are 67 separate wall pieces, which is a lot, and the messy left side counts as known even though it's wrong.


## mission_1.system_observation

As I drove, the red scan dots lined up with the walls and the map filled in behind the robot. The robot's position in RViz moved with the wheels, and the map slowly got bigger. When my robot flipped over, the position suddenly jumped far away, and a messy second copy of the arena showed up on the left side of the map.

## mission_2.comparison

Strategy 2 (room by room) scored higher: known area 58% vs 44%, quality 83.7 vs 75.7, and fewer wall pieces (59 vs 67). Speckle was a bit worse (6.5% vs 5.0%). Visually, map 1 had a messy ghost copy of the arena from when my robot flipped, and map 2 has one clean outline with the posts inside. My prediction was partly right: continuity was better, but I thought coverage would be about the same, and it was clearly higher. Map 2 is also smaller (39 vs 69 m²), partly because the ghost area inflated map 1.

## mission_2.loop_closure

I can't say for sure that a loop closure happened. In map 2, the walls lined up with no doubled lines when I got back near my start, which is what a good loop looks like, but I didn't check for a sudden shift in RViz. Ordinary map growth just adds new cells at the edge. A real loop closure would show up as the whole map snapping or shifting a little at once, and old walls lining up with new scans. In map 1, the doubled arena shows what happens when the robot's position is wrong and nothing corrects it.


## mission_2.strategy_prediction

My first strategy was perimeter then interior: I followed the outer wall first, then drove through the middle. My second one is room by room, where I weave through the posts and open areas first and then finish along the walls. I think the second one will give better continuity, because the robot sees each area from several angles in a row. I also expect better loop closure, since I'll end by returning to my starting spot. Coverage will probably be about the same. I'll drive slowly this time so the robot doesn't flip and the map stays clean.


## mission_3.deployment_limit



## mission_3.knowing_where



## mission_3.recovery



## mission_3.sensor_effect


