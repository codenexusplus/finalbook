# Contract: RAG Query API

**Date**: 2025-12-15
**Feature**: [RAG Query API](spec.md)

This document defines the API contract for the RAG Query API, detailing the endpoint, request/response schemas, and error handling.

## 1. API Endpoint

-   **Path**: `/query`
-   **Method**: `POST`
-   **Description**: Receives a user's question, retrieves relevant context from Qdrant, and generates an answer using Cohere.

## 2. Request Schema

Utilizes the `QueryRequest` Pydantic model.

-   **Media Type**: `application/json`
-   **Fields**:
    -   `question` (string, required): The user's question.

### Example Request Body

```json
{
  "question": "What is the role of nodes in ROS 2?"
}
```

## 3. Response Schema

Utilizes the `QueryResponse` Pydantic model.

-   **Media Type**: `application/json`
-   **Fields**:
    -   `answer` (string): The AI-generated answer.
    -   `sources` (list of strings): Unique URLs of source documents.
    -   `message` (string, optional): An informational message, especially for no-answer scenarios.

### Example Success Response (HTTP 200 OK)

```json
{
  "answer": "In ROS 2, nodes are executable processes that perform computation. They are the fundamental units of computation in the ROS graph and communicate with each other using topics, services, and actions.",
  "sources": [
    "https://finalbook-ss4z.vercel.app/docs/module-1-ros2/ch2-ros2-architecture"
  ],
  "message": null
}
```

### Example No-Answer Response (HTTP 200 OK, with message)

```json
{
  "answer": "",
  "sources": [],
  "message": "I could not find relevant information in the book to answer your question."
}
```

## 4. Error Handling

-   **HTTP 400 Bad Request**: Returned if the request body is invalid (e.g., missing `question` field, `question` is empty).
    -   **Response Body Example**:
        ```json
        {
          "detail": [
            {
              "loc": ["body", "question"],
              "msg": "field required",
              "type": "value_error.missing"
            }
          ]
        }
        ```
-   **HTTP 500 Internal Server Error**: Returned for unexpected server errors, issues with Cohere API, Qdrant API, or other internal processing failures.
    -   **Response Body Example**:
        ```json
        {
          "detail": "An internal server error occurred."
        }
        ```

## 5. API Logic Flow

1.  Receive POST request at `/query` with `QueryRequest`.
2.  Validate request body.
3.  Embed `request.question` using Cohere's `embed-english-v3.0` model (`input_type='search_query'`).
4.  Query Qdrant collection `rag_embedding` with the generated embedding to retrieve top-K relevant text chunks.
5.  Extract text and unique source URLs from retrieved Qdrant points.
6.  Concatenate retrieved text into a single context string.
7.  If context is insufficient, generate a `QueryResponse` with an empty answer and an appropriate message.
8.  If context is available, send the original question and the context to Cohere's generation model (e.g., `command`) to generate an answer.
9.  Return `QueryResponse` with the generated answer and source URLs.
