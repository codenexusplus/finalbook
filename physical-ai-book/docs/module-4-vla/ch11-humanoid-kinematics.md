---
sidebar_position: 1
title: "Chapter 11: Humanoid Kinematics and Dynamics"
---

# Chapter 11: Humanoid Kinematics and Control

To command a humanoid robot, the high-level movement goals from Nav2 must be converted into low-level joint angles. This conversion relies on kinematics.

## 11.1 Kinematics: The Geometry of Motion
*   **Forward Kinematics (FK)**: Calculates the end-effector pose (position and orientation of the hand or foot) based on the current configuration of all joint angles. This is used for verification and simulation.
*   **Inverse Kinematics (IK)**: Calculates the joint angles required to achieve a desired end-effector pose. This is the fundamental, complex calculation used to control the robot (e.g., "To put the hand at position $(x, y, z)$, what should the shoulder, elbow, and wrist angles be?").

## 11.2 Bipedal Locomotion and Balance
Bipedal walking is inherently unstable. Maintaining balance is managed by controlling the robot's Zero Moment Point (ZMP).

*   **Center of Mass (CoM)**: The average location of the robot's mass.
*   **Zero Moment Point (ZMP)**: The specific point on the ground about which the net moment of all forces (gravity, inertia, and contact forces) is zero. The ZMP must remain inside the robot's support polygon (the area defined by the contact points of the feet) to prevent the robot from tipping over.
*   **Control Strategy**: Humanoid control algorithms constantly calculate the required joint trajectories to ensure the ZMP follows a safe, predefined trajectory within the foot boundaries as the robot steps, guaranteeing dynamic stability.
