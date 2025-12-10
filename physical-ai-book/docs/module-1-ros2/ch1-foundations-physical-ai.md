---
sidebar_position: 1
title: "Chapter 1: Foundations of Physical AI and Embodied Intelligence"
---

# Chapter 1: Foundations of Physical AI & Embodied Intelligence

The shift from Digital AI (operating in abstract data spaces) to Physical AI (interacting with the real world) is central to this field.

## The Embodied Intelligence Paradigm
Traditional AI, focused on games like Chess or Go, relies on abstract symbolic reasoning. Embodied Intelligence—the theoretical foundation of Physical AI—posits that intelligence emerges from the dynamic interaction between an agent's brain (computation), body (morphology/kinematics), and environment.

*   **Principle of Situatedness**: The robot's intelligence is inseparable from its real-world context (where it is).
*   **Sensorimotor Coupling**: Intelligence relies on the closed-loop interaction of sensing (e.g., LiDAR, cameras) and acting (e.g., motors, grippers).
*   **Morphological Computation**: The physical design (the body) of the robot itself can simplify computation (e.g., a compliant gripper requires less sophisticated control than a rigid one).

## Sensor Systems in Humanoid Robotics
Humanoid robots require a comprehensive understanding of their environment and self-state.

| Sensor Type         | Function                                             | Data Output                    |
| :------------------ | :--------------------------------------------------- | :----------------------------- |
| LiDAR               | Measures distance to surfaces using pulsed laser light. | 3D Point Clouds                |
| Depth Camera        | Provides color image data (RGB) and per-pixel distance (Depth). | RGB-D Stream                   |
| IMU                 | Measures specific force and angular rate (acceleration and rotation). | 6-DOF or 9-DOF Pose/Velocity data |
| Force/Torque Sensors | Measures the forces applied at contact points (e.g., fingertips, feet). | Force Vector $(F_x, F_y, F_z)$ |
