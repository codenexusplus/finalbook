---
sidebar_position: 2
title: "Chapter 6: Simulating Sensors (LIDAR, Cameras, IMUs)"
---

# Chapter 6: Simulating Sensors: LiDAR and Cameras

Simulated sensors are defined within the robot's URDF/SDF description using Gazebo Plugins. These plugins hook directly into the Gazebo physics engine to generate data that mimics real-world sensor outputs.

## 6.1 Simulating LiDAR (LaserScan)
LiDAR (Light Detection and Ranging) is simulated using the Ray Sensor type in Gazebo. It casts virtual rays into the environment and returns distance measurements based on the closest collision point.

| Property          | Description                                                                 | ROS 2 Message        |
| :---------------- | :-------------------------------------------------------------------------- | :------------------- |
| `type="ray"`        | Defines the sensor as a range finder (LiDAR/Sonar).                       | `sensor_msgs/LaserScan` |
| `update_rate`     | How often the sensor publishes data (e.g., 10 Hz).                        | N/A                  |
| `<horizontal_scan>` | Defines the angular range and resolution (e.g., 360 degrees).             | N/A                  |
| `<range>`         | Defines the minimum and maximum detection distance.                       | N/A                  |

### Plugin Output:
Uses a ROS 2-aware Gazebo plugin to publish the data on a Topic (e.g., `/scan`). `sensor_msgs/LaserScan`

## 6.2 Simulating Cameras (RGB and Depth)
Cameras are critical for computer vision (CV) tasks like object detection and VSLAM. Gazebo supports standard RGB and Depth cameras.

*   **RGB Camera**: Simulated using the Camera Sensor type. It renders the scene from the camera's viewpoint and publishes the image data.
    *   **ROS 2 Message**: `sensor_msgs/Image` (raw color data).
*   **Depth Camera**: Adds depth information to the RGB stream, often combined into an RGB-D stream.
    *   **ROS 2 Message**: `sensor_msgs/Image` (grayscale depth map) and `sensor_msgs/PointCloud2` (3D point cloud data).
*   **Coordinate System Adjustment**: Since many vision pipelines expect the camera's Z-axis to point forward (instead of the standard URDF X-axis), a specific transformation (often an extra "camera optical joint") is added to the URDF to ensure the published sensor messages are correctly interpreted by downstream ROS 2 packages.
