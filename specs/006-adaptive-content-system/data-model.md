# Data Model: User Profile Extensions

**Date**: 2025-12-18
**Feature**: AI-Native Identity & Adaptive Content System

This document details the extensions to the existing `User` profile data model to accommodate hardware and software skill information for content personalization.

## Existing `user` Table and `profile` JSONB Column

As defined in `specs/005-advanced-identity-auth/data-model.md`, the `user` table includes a `profile` column of type `JSONB`. This feature will extend the structure of this `JSONB` object.

## Extended `profile` JSONB Column Structure

The `profile` column will now store the following additional user-specific data:

```json
{
  "hardware": {
    "rtx_gpu_model": "string", // e.g., "RTX 3080", "RTX 4090", "None"
    "vram_gb": "integer",    // e.g., 10, 12, 16
    "jetson_device": "string" // e.g., "Jetson Nano", "Jetson Orin", "None"
  },
  "software_skill_level": {
    "ros_experience": "string" // e.g., "Beginner", "Intermediate", "Advanced"
  },
  "preferences": {
    "preferred_language": "string", // e.g., "English", "Urdu" (extending existing)
    "difficulty_level": "string" // e.g., "Easy", "Medium", "Hard" (extending existing)
  }
}
```

## Changes and Rationale

-   **`hardware`**: Added `vram_gb` to provide more granular hardware context for personalization.
-   **`software_skill_level`**: Renamed `ros2_experience` to `ros_experience` for broader applicability, reflecting the course content.
-   **`preferences.preferred_language`**: Extended to include "Urdu" as a possible value to support the new translation feature.

The rationale for embedding this data within the existing `JSONB` `profile` column remains `Architectural Minimalism`, avoiding new tables and simplifying data access for a single-user profile.
