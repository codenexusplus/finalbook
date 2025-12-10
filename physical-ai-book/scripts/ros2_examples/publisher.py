import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32 # Standard message type for an integer

class HeartbeatPublisher(Node):
    def __init__(self):
        super().__init__('heartbeat_publisher')
        # 1. Create a publisher: Topic Type, Topic Name, QoS History Depth
        self.publisher_ = self.create_publisher(Int32, 'robot_heartbeat', 10) 
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.heartbeat_count = 0

    def timer_callback(self):
        msg = Int32()
        msg.data = self.heartbeat_count
        self.publisher_.publish(msg) # Publish the message
        self.get_logger().info(f'Publishing Heartbeat: {msg.data}')
        self.heartbeat_count += 1

def main(args=None):
    rclpy.init(args=args)
    heartbeat_publisher = HeartbeatPublisher()
    rclpy.spin(heartbeat_publisher) # Keep node alive
    heartbeat_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
