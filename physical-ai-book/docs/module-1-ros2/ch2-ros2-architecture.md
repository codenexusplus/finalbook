---
sidebar_position: 2
title: "Chapter 2: ROS 2 Architecture and Core Concepts"
---

# Chapter 2: ROS 2 Architecture: Nodes, Topics, and Services

The Robot Operating System 2 (ROS 2) is the distributed middleware framework used to structure complex robotic software into smaller, manageable, and interconnected components.

## 1. The Building Blocks: Nodes
A Node is an executable unit designed to perform a single, specific function (e.g., a camera driver, a motor controller, a path planner). ROS 2 systems are collections of many cooperating nodes.

## 2. Asynchronous Streaming: Topics
Topics enable asynchronous, one-to-many communication for streaming, continuous data.
*   **Publisher**: A node that sends messages to a named Topic.
*   **Subscriber**: A node that receives messages from a named Topic via a callback function.
*   **Use Case**: Sensor data (continuous stream of camera images, IMU readings), motor velocity commands.

## 3. Synchronous Requests: Services
Services enable synchronous, request-response, one-to-one communication for atomic, immediate tasks.
*   **Service Client**: A node that sends a Request and waits (blocks) for a Response.
*   **Service Server**: A node that executes the logic upon receiving the Request and returns the Response.
*   **Use Case**: Setting a robot's parameter, querying the state of a motor, asking a planner for a specific single path calculation.

## Example Code: ROS 2 Publisher and Subscriber (rclpy)
The following is a basic Python implementation using `rclpy` to demonstrate the Publisher/Subscriber pattern (Topics).

### A. Publisher Node (`publisher.py`)
This node publishes the humanoid's simulated "Heartbeat" (a counter) every half-second.
```python
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
```

### B. Subscriber Node (`subscriber.py`)
This node subscribes to the `robot_heartbeat` topic and logs the data it receives.
```python
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
```
