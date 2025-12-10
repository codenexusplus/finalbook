import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class HeartbeatSubscriber(Node):
    def __init__(self):
        super().__init__('heartbeat_subscriber')
        # 1. Create a subscriber: Topic Type, Topic Name, Callback, QoS
        self.subscription = self.create_subscription(
            Int32, 
            'robot_heartbeat', 
            self.listener_callback, 
            10)
        self.subscription # prevent unused variable warning

    def listener_callback(self, msg):
        # 2. This function is called every time a message is received
        self.get_logger().info(f'Received Heartbeat: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    heartbeat_subscriber = HeartbeatSubscriber()
    rclpy.spin(heartbeat_subscriber) # Keep node alive
    heartbeat_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
