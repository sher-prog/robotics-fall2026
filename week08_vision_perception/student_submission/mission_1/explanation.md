# mission_1

## diagnosis
In normal_1, yes, the green box is perfectly on the mug. Because the mug's color falls inside our Brightness (Value) range of 45 to 125, it shows up as a solid white shape in the mask. It becomes the largest shape in the contour table, so the detector selects it.

In dim_1, no, the box completely misses the mug. Because the lighting is so dark, the mug's pixels fall below our minimum Brightness limit of 45. The mug turns black in the mask, meaning the detector can't see it at all, and no contour is large enough to be selected.

## limitations
I lowered the Maximum Brightness (Value) down to 125.  Before I did this, the bright glare on the wooden desk was passing the color test and fusing with the mug in the mask, which pulled the green box down onto the table. Lowering the maximum brightness blacked out the table glare. This disconnected the desk from the mug in the mask, allowing the green box to shrink and perfectly wrap around just the cup.

This detector only looks for a specific range of colors. If we used a blue cup, or placed this brown cup on a dark brown table that exactly matches its color, the detector would completely fail because it doesn't actually know what the shape of a cup looks like.
