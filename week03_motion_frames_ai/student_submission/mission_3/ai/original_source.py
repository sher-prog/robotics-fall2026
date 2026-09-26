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
    if pattern_name != "l_path":
        raise ValueError(f"Unknown pattern: {pattern_name}")
    speed = 0.15
    turn_speed = 0.50
    return [
        Segment(linear_x=speed, angular_z=0.0, duration=0.40 / speed),
        Segment(linear_x=0.0, angular_z=turn_speed, duration=(math.pi / 2) / turn_speed),
        Segment(linear_x=speed, angular_z=0.0, duration=0.40 / speed),
    ]
