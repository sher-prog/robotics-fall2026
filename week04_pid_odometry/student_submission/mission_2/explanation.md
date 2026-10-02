# mission_2 Submission

- Name: Shernice Chetty
- Section: CSCI 39536 01 [5485]

## Explanations

### prediction

The estimate forward distance will overestimate the actual distance the robot travelled, while the estimate sideways distance will underestimate the actual distance travelled

### calibration_analysis

I predicted that incorrect scales would cause the system to over- or under-estimate the distance traveled, which the test confirmed. Changing the forward pod scale fixed the forward and backward distance tracking, while changing the strafe pod scale fixed the side-to-side distance tracking. The sideways pod is necessary because this holonomic robot can slide left and right without turning; a forward pod alone cannot measure this sideways movement. Even after perfect calibration, some drift remains because of real-world physical factors like wheel slip, floor bumps, or slight sensor friction that slowly add up over time.