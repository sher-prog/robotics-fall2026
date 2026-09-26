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