# Data Model: Physical AI & Humanoid Robotics Textbook Content Development

This document defines the data models for the textbook content and the RAG chatbot components.

## Entities from Feature Spec

### Module
- **Description**: A logical grouping of related topics (e.g., "ROS 2 Fundamentals").
- **Fields**:
    - `id`: Unique identifier (e.g., string, UUID)
    - `name`: Name of the module (e.g., "ROS 2 Fundamentals")
    - `order`: Sequential order within the course
    - `chapter_ids`: List of chapter IDs belonging to this module

### Lesson
- **Description**: A specific teaching unit within a module, covering a particular concept or skill.
- **Fields**:
    - `id`: Unique identifier (e.g., string, UUID)
    - `title`: Title of the lesson
    - `module_id`: Foreign key to the Module it belongs to
    - `content_path`: File path to the Markdown/MDX content
    - `order`: Sequential order within the chapter/module

### Project/Assessment
- **Description**: A practical assignment or evaluation designed to test understanding and application of course material.
- **Fields**:
    - `id`: Unique identifier (e.g., string, UUID)
    - `name`: Name of the assessment (e.g., "ROS 2 package development project")
    - `module_id`: Foreign key to the Module it assesses
    - `description_path`: File path to the Markdown description of the assessment
    - `type`: Type of assessment (e.g., "project", "quiz", "capstone")

### RobotPlatform
- **Description**: A specific hardware/software ecosystem discussed (e.g., ROS 2, NVIDIA Isaac).
- **Fields**:
    - `id`: Unique identifier (e.g., string, UUID)
    - `name`: Name of the platform (e.g., "ROS 2", "NVIDIA Isaac")
    - `description`: Brief description of the platform

## RAG Chatbot Data Model

### Document Chunk
- **Description**: A segment of the textbook content, used for retrieval by the RAG system.
- **Fields**:
    - `id`: Unique identifier for the chunk (UUID)
    - `text_content`: The actual text of the chunk (string)
    - `embedding`: Vector representation of `text_content` (array of floats)
    - `source_file`: Original Markdown file path (string)
    - `chapter_id`: ID of the chapter the chunk belongs to (string)
    - `module_id`: ID of the module the chunk belongs to (string)
    - `page_number`: Optional page number or section ID (string)
    - `order_in_chapter`: Sequential order of the chunk within its chapter (integer)
    - `user_selected_context_flag`: Boolean flag indicating if this chunk was part of a user-selected context (runtime metadata, not persisted in core DB)

### Metadata
- **Description**: Additional metadata stored in Neon Serverless Postgres for each document chunk.
- **Fields**:
    - `chunk_id`: Foreign key to the `Document Chunk`
    - `source_file`
    - `chapter_id`
    - `module_id`
    - `page_number`
    - `order_in_chapter`

## Relationships

- `Module` has many `Lesson`s
- `Module` has many `Project/Assessment`s
- `Lesson` content will be chunked into `Document Chunk`s
- `Document Chunk`s are linked to `Metadata` in Postgres for detailed lookup.
