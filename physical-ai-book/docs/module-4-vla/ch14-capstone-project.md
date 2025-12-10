---
sidebar_position: 4
title: "Chapter 14: Autonomous Humanoid Capstone Project"
---

# Chapter 14: Capstone Project: The Autonomous Humanoid

The Capstone Project is the culmination of the entire course, requiring the integration of all four modules: ROS 2 (middleware), Gazebo/Unity (simulation), NVIDIA Isaac (perception/navigation), and the VLA Stack (cognitive planning).

## Project Goal: Closed-Loop Conversational Robotics
The goal is to build a complete, autonomous humanoid system in simulation that can:
*   Receive a high-level, natural language command (Module 4: VLA).
*   Plan the necessary physical actions (Module 4: Cognitive Planning).
*   Navigate to a complex location (Module 3: Isaac/Nav2).
*   Perceive and localize a specific object (Module 3: Isaac Perception).
*   Manipulate the object (Module 1: ROS 2 Control).
*   Report its success or failure back to the user.

## Key Integration Points
| Module       | Component                | Task within Capstone Project                                                                                     |
| :----------- | :----------------------- | :--------------------------------------------------------------------------------------------------------------- |
| Input        | Whisper/Speech Agent (Ch 12) | Transcribe the user's spoken command (e.g., "Find the blue bottle on the shelf and place it on the table").     |
| Planning     | LLM Planner (Ch 13)      | Decompose the transcribed command into the JSON sequence of atomic actions (`NAVIGATE`, `DETECT`, `PICKUP`, `PLACE`). |
| Perception   | Isaac VSLAM/Nvblox (Ch 9 & 10) | Provide continuous, high-speed pose estimation and map/costmap updates to the Nav2 stack.                        |
| Movement     | Nav2 Stack (Ch 10)       | Execute the `Maps_TO` action goals from the LLM, calculating optimal bipedal paths while avoiding Nvblox-detected obstacles. |
| Control      | ROS 2 Action Client (Ch 3) | Send low-level Action Goals (e.g., `PICKUP_OBJECT`) to the humanoid's joint controllers (using `rclpy`).       |
| Output       | LLM Reflection (Ch 13)   | Re-evaluate the system state (e.g., success of manipulation) and report the outcome back to the user in natural language. |

## System Flow Diagram
The Capstone demonstrates the full closed-loop VLA system:
Audio Command -> Whisper (Speech Recognition) -> Text Command -> LLM Planner (Cognitive Planning) -> JSON Action Plan -> ROS 2 Executive (Task Execution)

ROS 2 Executive orchestrates:
- Navigation (via Nav2) for Movement.
- Isaac ROS for Vision (Object Localization).
- IK Solvers for Control (Manipulation).
All these actions lead to a State Update, which is fed back to the LLM for Reflection and reporting the outcome to the User.
