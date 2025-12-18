# Data Model: RAG Query API

**Date**: 2025-12-15
**Feature**: [RAG Query API](spec.md)

This document defines the data models for the RAG Query API's request and response structures. These models will primarily use Pydantic for validation and serialization in FastAPI.

## 1. Request Model: `QueryRequest`

Represents the input structure for a user's question to the RAG API.

### Pydantic Model

```python
from pydantic import BaseModel

class QueryRequest(BaseModel):
    question: str
```

### Fields

-   **`question`** (string)
    -   Description: The user's question about the book content.
    -   Constraints: Required, non-empty.

### Example Request

```json
{
  "question": "What are the core components of ROS 2?"
}
```

## 2. Response Model: `QueryResponse`

Represents the output structure returned by the RAG API, including the generated answer and source references.

### Pydantic Model

```python
from pydantic import BaseModel
from typing import List, Optional

class QueryResponse(BaseModel):
    answer: str
    sources: List[str] = []
    message: Optional[str] = None # For cases where no answer can be generated or an error occurs
```

### Fields

-   **`answer`** (string)
    -   Description: The AI-generated answer to the user's question, based on the retrieved context.
-   **`sources`** (list of strings)
    -   Description: A list of unique URLs from the book content that were used to generate the answer.
-   **`message`** (string, optional)
    -   Description: An optional message, primarily used to convey information when an answer cannot be generated (e.g., "No relevant information found.").

### Example Success Response

```json
{
  "answer": "The core components of ROS 2 include nodes, topics, services, and actions. Nodes are individual processes, topics are named buses for anonymous publish/subscribe messaging, services are synchronous request/reply calls, and actions are long-running tasks.",
  "sources": [
    "https://finalbook-ss4z.vercel.app/docs/module-1-ros2/ch2-ros2-architecture",
    "https://finalbook-ss4z.vercel.app/docs/module-1-ros2/ch3-python-agents-rclpy"
  ],
  "message": null
}
```

### Example No-Answer Response

```json
{
  "answer": "",
  "sources": [],
  "message": "I could not find relevant information in the book to answer your question."
}
```

## 3. Qdrant Point Payload (as context source)

While not a direct API model, the structure of the payload stored in Qdrant is critical as it will be retrieved and used to populate the `sources` field in the `QueryResponse`.

### Payload Structure (from Ingestion Pipeline)

```json
{
  "text": "This is a chunk of text from the documentation...",
  "source": "https://finalbook-ss4z.vercel.app/docs/module-1-ros2/ch2-ros2-architecture",
  "chunk_id": 3
}
```

-   **`text`**: The actual text content.
-   **`source`**: The URL of the document where the text originated.
-   **`chunk_id`**: An identifier for the specific chunk within its source.
