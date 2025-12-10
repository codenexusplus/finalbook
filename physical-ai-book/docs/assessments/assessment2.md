---
sidebar_position: 2
title: "Assessment 2: Gazebo Simulation Implementation"
---

# Module 2 Assessment

## Scope: Digital Twin and Sensor Validation
This assessment requires students to demonstrate practical proficiency in setting up a functional digital twin and validating its sensor outputs.

| Requirement         | Description                                                                                                   | Success Criteria                                                                    |
| :------------------ | :------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------- |
| 1. URDF Integration | Create a complete ROS 2 package that includes the finalized humanoid URDF from Module 1.                      | The robot model loads correctly in Gazebo Sim with no broken links.                 |
| 2. World Setup      | Create a simple custom SDF World File that includes at least three distinct types of objects (e.g., a ramp, a box, a cylinder) for interaction testing. | The world loads alongside the robot via a single Launch File.                       |
| 3. Sensor Simulation | Add a LiDAR sensor and a Depth Camera to the humanoid's URDF, configured using Gazebo plugins.                  | The topics `/scan` (LaserScan) and `/camera/image_raw` (Image) are published and viewable in RViz2 via the `ros_gz_bridge`. |
| 4. Teleoperation    | Implement a simple ROS 2 node (using `rclpy`) that subscribes to a `/cmd_vel` topic and uses a Gazebo plugin to apply motor commands, allowing the robot to be moved via keyboard teleoperation. | The robot can be commanded to move, and the motion is physically accurate within the Gazebo environment. |
