# Mission 2

## Frame Context

The rear camera is bolted right onto the robot, so its position relative to the robot never changes. The hallway camera is mounted on a fixed wall in the room, so as the robot drives around, the distance and angle between the robot and the wall camera are constantly changing.

## Improved Changes

The improved prompt makes the program much safer and more precise by clearly locking down its behavior. Instead of guessing, it strictly requires the input point to come from the hall_camera frame and targets base_link for the output. It preserves the exact timestamp of when the observation happened rather than using the current time, and it uses the actual live TF tree instead of hard-coded offsets. Finally, if the transform fails or is missing, it safely returns None and completely avoids sending any movement commands, ensuring the robot never drives around on bad or missing data.

## Initial Analysis

The original code assumed a lot without checking it:

Source and target frames - It trusted whatever frame name was in the message without checking it was really the hallway camera, and assumed base_link was the exact right frame name.

PointStamped metadata -  It checked that the frame name wasn't empty, but never checked that the timestamp was valid, or that the coordinates weren't garbage.

Timestamps -  It used the exact timestamp on the message to look up the transform without a backup plan if that exact moment wasn't found.

TF buffer - Knowing where the point is relative to the robot depends on the robot's localization system already working correctly, which the code never mentions.

Hard-coded offsets- There aren't any offsets in the code itself; it just assumes someone else already set up the camera's exact position elsewhere.

Unavailable transforms-If the transform lookup fails, the code just logs a warning and throws the detection away.

Robot motion topics -The code never checks that the robot's movement data is actually working.

## Initial Output

This node subscribes to `hallway_camera/detected_point` (a `geometry_msgs/PointStamped` with `header.frame_id` set to the camera's TF frame), uses a `tf2_ros.Buffer`/`TransformListener` to look up the transform to `base_link`, and republishes the result on `detected_point_base_link`.

Key points:
- `tf_buffer.transform(msg, 'base_link', timeout=...)` does the lookup *and* the math in one call — it uses `msg.header.stamp`, so it needs the camera→base_link transform to actually exist in the TF tree at that timestamp (published by `robot_state_publisher`, a `static_transform_publisher` for a fixed camera, or similar).
- `import tf2_geometry_msgs` is required even though it's unused directly — it registers `PointStamped` support with `Buffer.transform()`.
- Catches the three standard tf2 exceptions (`LookupException`, `ConnectivityException`, `ExtrapolationException`) so a missing/late transform just logs a warning instead of crashing the node.
- `target_frame` and `tf_timeout_sec` are exposed as ROS params if you need to point it at a different frame or tune how long it waits.

Swap the topic names for whatever your camera driver and consumer actually use.

## Initial Prompt

Write ROS 2 Python code that converts a point detected by the hallway camera into the robot's base_link frame.

## Initial Source

import rclpy
from rclpy.node import Node
from rclpy.duration import Duration

from geometry_msgs.msg import PointStamped

import tf2_ros
from tf2_ros import Buffer, TransformListener
from tf2_ros import LookupException, ConnectivityException, ExtrapolationException
import tf2_geometry_msgs # noqa: F401 (registers PointStamped with tf2_ros.Buffer.transform)

class HallwayPointToBaseLink(Node):
def init(self):
super().init('hallway_point_to_base_link')

    # Target frame we want the point expressed in.
    self.declare_parameter('target_frame', 'base_link')
    self.target_frame = self.get_parameter('target_frame').value

    # How long to wait for a transform before giving up.
    self.declare_parameter('tf_timeout_sec', 0.2)
    self.tf_timeout = Duration(
        seconds=self.get_parameter('tf_timeout_sec').value
    )

    # tf2 buffer + listener keep the recent transform tree in memory.
    self.tf_buffer = Buffer()
    self.tf_listener = TransformListener(self.tf_buffer, self)

    self.subscription = self.create_subscription(
        PointStamped,
        'hallway_camera/detected_point',
        self.point_callback,
        10,
    )

    self.publisher = self.create_publisher(
        PointStamped,
        'detected_point_base_link',
        10,
    )

    self.get_logger().info(
        f'Listening for detections, will transform into "{self.target_frame}"'
    )

def point_callback(self, msg: PointStamped):
    source_frame = msg.header.frame_id
    if not source_frame:
        self.get_logger().warn('Received point with empty frame_id, dropping it.')
        return

    try:
        # Blocks (up to tf_timeout) until the transform at msg.header.stamp
        # is available, then transforms the point in one step.
        transformed_point = self.tf_buffer.transform(
            msg,
            self.target_frame,
            timeout=self.tf_timeout,
        )
    except LookupException as ex:
        self.get_logger().warn(f'No transform {source_frame} -> {self.target_frame}: {ex}')
        return
    except ConnectivityException as ex:
        self.get_logger().warn(f'TF tree not connected: {ex}')
        return
    except ExtrapolationException as ex:
        self.get_logger().warn(f'Transform not available at requested time: {ex}')
        return

    self.publisher.publish(transformed_point)
    self.get_logger().debug(
        f'({msg.point.x:.3f}, {msg.point.y:.3f}, {msg.point.z:.3f}) in {source_frame} -> '
        f'({transformed_point.point.x:.3f}, {transformed_point.point.y:.3f}, '
        f'{transformed_point.point.z:.3f}) in {self.target_frame}'
    )

def main(args=None):
rclpy.init(args=args)
node = HallwayPointToBaseLink()
try:
rclpy.spin(node)
except KeyboardInterrupt:
pass
finally:
node.destroy_node()
rclpy.shutdown()

if name == 'main':
main()

## Live Pending

True

## Snapshot

{'captured_at': '2026-09-25T22:17:48.460134+00:00', 'frame_chain': ['hall_camera', 'odom', 'base_link', 'base_scan', 'rear_camera_link'], 'frames': ['odom', 'base_link', 'base_scan', 'rear_camera_link', 'hall_camera'], 'point_prompts': {'hall_camera_point': 'Transform point (0.5, 0.0, 0.0) from hall_camera to base_link.'}, 'schema_version': 2, 'source': 'live', 'transformed_points': {'hall_camera_point_in_base': {'x': -9.602645842094379e-09, 'y': -1.5}, 'rear_camera_point_in_base': {'x': -1.18, 'y': -1.0206624774663903e-11}, 'scan_point_in_base': {'x': 0.968, 'y': 0.0}}, 'transforms': {'base_scan_to_base_link': {'translation': {'x': -0.032, 'y': 0.0, 'z': 0.172}, 'yaw': 0.0}, 'hall_camera_to_base_link': {'translation': {'x': -9.599863875855443e-09, 'y': -2.0, 'z': 1.19}, 'yaw': 1.5707963268004606}, 'rear_camera_to_base_link': {'translation': {'x': -0.18, 'y': 0.0, 'z': 0.22}, 'yaw': -3.1415926535795866}}}

## Synthesis

The improved prompt makes the program much safer and more precise by clearly locking down its behavior. It strictly requires the input point to come from the hall_camera frame and targets base_link for the output. It preserves the exact timestamp of when the observation happened rather than using the current time, and it uses the actual live TF tree instead of hard-coded offsets. If the transform fails or is missing, it safely returns None and completely avoids sending any movement commands, ensuring the robot never drives around on bad or missing data.

## Live Issue

Live camera verification is currently pending because the TF transformation buffer between the hall_camera source frame and the base_link target frame could not be resolved during runtime execution, returning a null point value. Although all 5 unit tests successfully passed.
