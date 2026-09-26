"""AI-assisted motion pattern implementation.

Preserve the original AI response in Streamlit. Review it, then implement a safe
version here. The node accepts only segments returned by ``build_pattern``.
"""
from __future__ import annotations
from dataclasses import dataclass
import math

@dataclass(frozen=True)
class Segment:
    linear_x: float
    angular_z: float
    duration: float

def build_pattern(pattern_name: str) -> list[Segment]:
    """Return ordered, bounded motion segments for the assigned pattern.

    Supported assignments are ``rounded_rectangle``, ``l_path``, and
    ``alternating_arcs``. Do not include the final stop; the ROS wrapper always
    publishes it and the evaluator verifies it.
    """
    if pattern_name != "l_path":
        raise ValueError(f"Unknown pattern: {pattern_name!r}")

    leg_distance = 0.40
    speed = 0.15
    turn_angle = math.pi / 2
    turn_speed = 0.50

    # The wrapper only guarantees zero velocity after the whole pattern ends
    # (see pattern_node.py); it does not pause between segments, and the
    # course check for this pattern expects exactly 3 segments. So the turn
    # starts as soon as the first leg's duration elapses -- there is no
    # explicit stop segment between legs.
    return [
        Segment(linear_x=speed, angular_z=0.0, duration=leg_distance / speed),
        Segment(linear_x=0.0, angular_z=turn_speed, duration=turn_angle / turn_speed),
        Segment(linear_x=speed, angular_z=0.0, duration=leg_distance / speed),
    ]

