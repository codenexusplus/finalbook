# Data Model: User and Profile

**Date**: 2025-12-18
**Feature**: Advanced Identity & Profile Orchestration

This document defines the database schema required for storing user and profile information in the Neon Serverless Postgres database. The schema is designed to integrate with `FastAPI-Users` and SQLAlchemy.

## Tables

### `user` Table

This table will store core user information and is managed by `FastAPI-Users`.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | `UUID` | **Primary Key** | Unique identifier for the user. |
| `email` | `VARCHAR(255)` | **Unique**, **Not Null** | User's email address, used for login. |
| `hashed_password` | `VARCHAR(1024)` | **Not Null** | Hashed password for the user. |
| `is_active` | `BOOLEAN` | **Not Null**, Default: `true` | Flag to activate or deactivate the user. |
| `is_superuser` | `BOOLEAN` | **Not Null**, Default: `false` | Flag for superuser status. |
| `is_verified` | `BOOLEAN` | **Not Null**, Default: `false` | Flag for email verification status. |
| `profile` | `JSONB` | **Nullable** | A JSON object to store user profile data. |

### `profile` JSONB Column Structure

The `profile` column will store user-specific data for personalization.

```json
{
  "hardware": {
    "rtx_gpu_model": "string",
    "ram_gb": "integer",
    "jetson_device": "string"
  },
  "software_skill_level": {
    "ros2_experience": "string", // e.g., "Beginner", "Intermediate", "Advanced"
    "python_proficiency": "string" // e.g., "Beginner", "Intermediate", "Advanced"
  },
  "preferences": {
    "preferred_language": "string", // e.g., "English", "Spanish"
    "difficulty_level": "string" // e.g., "Easy", "Medium", "Hard"
  }
}
```

## Relationships

- The `user` table is the central entity for identity.
- The `profile` data is embedded within the `user` table as a `JSONB` column to maintain `Architectural Minimalism` and simplify data retrieval. This avoids the need for an additional table and `JOIN` operations for the profile data, which is always accessed in the context of a user.
