---
sidebar_position: 4
title: "Assessment 4: The Autonomous Humanoid"
---

# Capstone Assessment

## 🎯 Goal
Submit the fully integrated and functioning codebase for the Autonomous Humanoid Capstone Project, demonstrating the successful execution of a complex, multi-stage task.

## 📝 Required Deliverables
### Complete Code Repository:
Submit the full `physical-ai-book` package structure, including:
*   The Python LLM Planner Agent code (Ch 13).
*   All necessary ROS 2 package files (nodes, actions, services).
*   Configuration files for Isaac Sim and Nav2 (Ch 8 & 10).

### Demonstration Video:
A single video (max 5 minutes) showing the humanoid successfully completing the following sequence after a single voice command:
*   **Phase 1: Speech & Planning**: The robot transcribes the command and prints the JSON Action Plan to the console.
*   **Phase 2: Navigation**: The robot navigates a complex, multi-room environment using Nav2 and VSLAM.
*   **Phase 3: Perception & Manipulation**: The robot correctly identifies the target object (e.g., "blue bottle") and executes the full pick-and-place sequence.

### Final Report:
A technical summary (max 1,000 words) that describes:
*   The kinematics solution used for the pick-and-place task (Ch 11).
*   A description of the Prompt Engineering used to ensure the LLM outputs valid, executable JSON (Ch 13).
*   Challenges faced during Sim-to-Real considerations, even within the digital twin.

This assessment tests your ability to create a fully integrated, high-performance AI perception and control system for autonomous humanoid operation.
