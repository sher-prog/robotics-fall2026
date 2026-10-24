# Mission 1

## Limitations

The left side of the map is the worst. After the robot flipped, the position estimate jumped, so the scans got drawn in the wrong place and it looks like a second, blurry arena. I also never drove close to some of the outer walls, so they have gaps. Driving too fast near the posts caused the flip, and that broke the matching between scans.


## Map Interpretation

About 44% of the map is known, which is decent for one run. Speckle was low (5%), so there isn't much random noise, and border contact was under 1%. The quality score of 75.7 looks good, but I don't fully trust it. There are 67 separate wall pieces, which is a lot, and the messy left side counts as known even though it's wrong.


## System Observation

As I drove, the red scan dots lined up with the walls and the map filled in behind the robot. The robot's position in RViz moved with the wheels, and the map slowly got bigger. When my robot flipped over, the position suddenly jumped far away, and a messy second copy of the arena showed up on the left side of the map.
