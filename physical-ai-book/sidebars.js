/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - have great navigation with next/previous buttons
 */

// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Module 1: The Robotic Nervous System (ROS 2)',
      collapsible: true,
      items: [
        'module-1-ros2/ch1-foundations-physical-ai',
        'module-1-ros2/ch2-ros2-architecture',
        'module-1-ros2/ch3-python-agents-rclpy',
        'module-1-ros2/ch4-urdf-launch-files',
      ],
    },
    {
      type: 'category',
      label: 'Module 2: The Digital Twin (Gazebo & Unity)',
      collapsible: true,
      items: [
        'module-2-digital-twin/ch5-gazebo-simulation-setup',
        'module-2-digital-twin/ch6-simulating-sensors',
        'module-2-digital-twin/ch7-unity-hri',
      ],
    },
    {
      type: 'category',
      label: 'Module 3: The AI-Robot Brain (NVIDIA Isaac™)',
      collapsible: true,
      items: [
        'module-3-nvidia-isaac/ch8-isaac-sim-synthetic-data',
        'module-3-nvidia-isaac/ch9-isaac-ros-vslam',
        'module-3-nvidia-isaac/ch10-nav2-humanoid-movement',
      ],
    },
    {
      type: 'category',
      label: 'Module 4: Vision-Language-Action (VLA)',
      collapsible: true,
      items: [
        'module-4-vla/ch11-humanoid-kinematics',
        'module-4-vla/ch12-voice-to-action-whisper',
        'module-4-vla/ch13-cognitive-planning',
        'module-4-vla/ch14-capstone-project', // Final chapter
      ],
    },
  ],
};

export default sidebars;
