---
sidebar_position: 3
title: "Chapter 3: Building ROS 2 Packages with Python (rclpy)"
---

# Chapter 3: Building Python Agents with rclpy

This chapter expands on simple topics by introducing two goal-oriented communication patterns crucial for complex robot applications: Services and Actions.

## 3.1 ROS 2 Services: Atomic Tasks
Services implement a synchronous, request-response model. They are ideal for atomic, well-defined tasks that require an immediate answer and typically complete quickly.
*   **Model**: Client Node ➡️ Request (blocks/waits) ➡️ Server Node ➡️ Response ⬅️ Client Node (unblocks).
*   **Use Case**: Retrieving a configuration parameter, toggling a motor on/off, performing a quick calculation (e.g., inverse kinematics).
*   **Implementation in `rclpy`**: Uses `create_service()` on the server and `create_client()` with `call_async()` on the client, often involving Python's `asyncio` to prevent the client node from blocking.

| Service Server (`sum_server.py` concept) | Service Client (`sum_client.py` concept) |
| :---------------------------------------- | :---------------------------------------- |
| 1. Creates a Node and imports the Service interface (`AddTwoInts`). | 1. Creates a Node and imports the Service interface. |
| 2. Defines a callback function (`add_callback`) that receives a request and populates a response. | 2. Creates a client object using `create_client()`. |
| 3. Calls `create_service()` to advertise the service and connect it to the callback. | 3. Calls `wait_for_service()` to ensure the server is available. |
| 4. Spins the node to listen for incoming requests. | 4. Creates a Request message, populates it, and calls the service asynchronously using `call_async()`. |
| 5. Returns the response object. | 5. Waits on the returned `Future` object for the final result. |

## 3.2 ROS 2 Actions: Long-Running Goals
Actions implement a goal-feedback-result model. They are designed for long-running tasks that need continuous progress monitoring and the ability to be canceled (preempted) mid-execution. Actions are built on top of the underlying Topics and Services.
*   **Model**: Client sends a Goal, Server accepts the goal, sends periodic Feedback updates, and finally sends the Result.
*   **Interface Structure**: An Action definition has three components, separated by `---` in a `.action` file:
    *   `Goal`: The instruction (e.g., `target_distance: float`).
    *   `Result`: The final outcome (e.g., `distance_traveled: float`).
    *   `Feedback`: The progress updates (e.g., `current_distance: float`).
*   **Use Case**: Navigation (Move to a target), complex manipulation (Pick and Place), or running a long motor sequence.
