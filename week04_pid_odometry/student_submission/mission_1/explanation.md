# mission_1 Submission

- Name: Shernice Chetty
- Section: CSCI - 39536 01 [5485]

## Explanations

### prediction

With too little Kp, the arm will move sluggishly and fail to reach or hols the target pose; with too little Kd, the arm will swing past the target, oscillate and overshoot back and forth before finally settling.

### tuning_analysis

I predicted that low Kp would cause sluggish movement and low Kd would cause overshooting and oscillation. I adjusted both the shoulder and the elbow gains to increase responsiveness without excessive ringing. The hold phase showed the arm staying firmly on the target without drifting. Turning on gravity compensation counteracted the downward pull on the second link, keeping the shoulder stable