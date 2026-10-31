# pillar_search

## diagnosis
In attempt 20261030T230205-77c6cf2b, the robot found and centered each pillar. The error plot shows each color entering the camera at the left edge (about -1.0). The error then rose smoothly to about 0 within a few seconds. The error was negative, so the controller turned left (positive angular velocity), and the mask showed the pillar moving toward the image center. Forward speed stayed at 0 the whole time. I used steering gain 1.30 and didn't see oscillation. 

## evidence
All four colors (red, green, turquoise, blue) were centered, in that order. The state timeline shows SEARCH at a steady turn rate until the color appeared. The robot then centered, held with zero turn, and moved to the next color. The turn rate was capped at 0.45 rad/s while the error was large. A centered colored region only shows that some pixels match the color rule. A different object of the same color would fool it, so it doesn't prove identity. The robot never drove forward, and a pillar looks centered at any distance, so it doesn't prove distance either.
