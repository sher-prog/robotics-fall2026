import math
import os
import unittest

from week03_pattern.checks import command_at
from week03_pattern.pattern import build_pattern


class MyPatternTests(unittest.TestCase):
    def setUp(self):
        self.name = os.environ.get("WEEK03_ASSIGNED_PATTERN", "l_path")
        self.segments = build_pattern(self.name)

    def test_my_pattern_geometry(self):
        # l_path: forward 0.40 m, turn left 90 deg (pi/2 rad), forward 0.40 m.
        self.assertEqual(len(self.segments), 3)
        first, turn, last = self.segments
        self.assertAlmostEqual(first.linear_x * first.duration, 0.40, delta=0.02)
        self.assertAlmostEqual(turn.angular_z * turn.duration, math.pi / 2, delta=0.04)
        self.assertAlmostEqual(last.linear_x * last.duration, 0.40, delta=0.02)

    def test_my_pattern_order(self):
        first, turn, last = self.segments
        # First and last segments drive straight forward; only the middle segment turns.
        self.assertGreater(first.linear_x, 0)
        self.assertEqual(first.angular_z, 0.0)
        self.assertEqual(turn.linear_x, 0.0)
        self.assertGreater(turn.angular_z, 0.0)  # positive = turn left, per the spec
        self.assertGreater(last.linear_x, 0)
        self.assertEqual(last.angular_z, 0.0)

    def test_command_is_zero_after_total_duration(self):
        total = sum(segment.duration for segment in self.segments)
        self.assertEqual(command_at(self.segments, total), (0.0, 0.0))


if __name__ == "__main__":
    unittest.main()
