---
sidebar_position: 4
title: "Chapter 4: URDF & Launch Files for Robot Description"
---

# Chapter 4: Defining the Physical Robot: URDF and Launch Files

This chapter introduces the standard mechanisms for defining the robot's physical structure and composing the entire system.

## 4.1 Unified Robot Description Format (URDF)
URDF (Unified Robot Description Format) is an XML-based file format used to describe the kinematic and dynamic structure of a robot. It provides a standardized way for all ROS tools (visualization, simulation, control) to understand the robot's physical properties.

### Core Elements:
*   **`<link>`**: Represents a rigid body (e.g., a wheel, a chassis, an arm segment). It defines properties like mass, inertia, and visual/collision geometry.
*   **`<joint>`**: Connects two links (parent and child) and defines their relative motion (e.g., rotational, prismatic, or fixed).
*   **Xacro**: An XML macro language extension often used with URDF to simplify and parameterize complex robot descriptions, reducing file redundancy.

## 4.2 ROS 2 Launch Files
A Launch File is the ROS 2 mechanism for starting, configuring, and coordinating multiple nodes, executables, and parameters into a cohesive system—your robot application.

In ROS 2, Launch Files are written primarily in Python, offering greater flexibility and logic than the old XML format.

### Function: Defines the system's composition. It can:
*   Execute nodes (`Node` action).
*   Set parameters (`ParameterValue` class).
*   Include other launch files.
*   Pass arguments (e.g., the path to a URDF file).

### System Start-up: A common launch file use case is starting the visualization stack:
*   The `robot_state_publisher` node (to broadcast the robot's configuration based on the URDF).
*   The `joint_state_publisher` node (to simulate or receive joint data).
*   The `rviz2` visualization tool (to display the robot model and sensor data).
