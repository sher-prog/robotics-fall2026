# Final reflection

Respond to any or all of these prompts:

1. What did this activity make you think about regarding your own interests in robotics, computing, engineering, or related work?
2. How did this activity affect your motivation to do similar kinds of work in the future?
3. What value do you see in connecting technical or computing work with human, ethical, or societal considerations?
4. What stood out to you about the activity, and why?
5. Is there anything else you would like to share about your experience with the activity?

## Response

Going through this ROS 2 lab really connected the dots between my computer science coursework  and the physical realities of hardware. I do spend a lot of time thinking about AI, algorithms, and software design, but seeing code directly actuate physical movement introduces a whole new layer of strict safety requirements. Building a interactive web app or practice data structures is one part, but it’s completely different when a bug means a physical collision.

This activity definitely increased my motivation to explore the intersection of software and robotics. I have taken a great interest in Robotics. The publisher/subscriber model in ROS 2 is an elegant way to handle messy, asynchronous real-world data, and I enjoyed figuring out how to make the nodes talk to each other safely.

What stood out to me most was the ethical necessity of the "default to stop" behavior. It showed the immense responsibility we have as "soon to be" engineers. In standard software, an unhandled exception might cause a bad user experience but i noticed in robotics, it can cause physical harm. Designing the command guard and handling NaN readings reinforced the idea that safety and human well-being must always be prioritized over simply completing a task. It makes the engineering work feel much more grounded and consequential. And fun!

_Word count: 215_
