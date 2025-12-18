# Quickstart: RAG Query API

**Date**: 2025-12-15
**Feature**: [RAG Query API](spec.md)

This guide provides the steps to set up and run the FastAPI-based RAG Query API.

## 1. Prerequisites

-   Python 3.11+
-   Docker (optional, for containerized deployment)
-   Access to Cohere and Qdrant Cloud to obtain API keys.
-   A populated Qdrant collection named `rag_embedding` (created by the ingestion pipeline).

## 2. Setup

### Step 1: Navigate to the `fastapi-rag` Directory

This API will be built within the existing `fastapi-rag/` directory.

```bash
cd fastapi-rag
```

### Step 2: Create a Virtual Environment

It is recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Step 3: Update Requirements File

Edit the `requirements.txt` file and add the following dependencies:

```
fastapi
uvicorn
cohere
qdrant-client
python-dotenv
```

### Step 4: Install Dependencies

Install the required packages using pip.

```bash
pip install -r requirements.txt
```

### Step 5: Configure Environment Variables

Create or update the `.env` file in the `fastapi-rag/` directory with your API keys and service URLs.

```
COHERE_API_KEY="your-cohere-api-key"
QDRANT_URL="https://your-qdrant-cloud-url.qdrant.tech:6333"
QDRANT_API_KEY="your-qdrant-api-key"
```
**Note**: Ensure `QDRANT_URL` includes the port if required by your Qdrant instance.

## 3. Execution

Once the setup is complete, you can run the FastAPI application.

### Step 1: Run the Application

The main API logic will be in a file named `app.py` inside the `fastapi-rag` directory.

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
This command starts the Uvicorn server, hosting the FastAPI application. The `--reload` flag is useful for development as it automatically restarts the server on code changes.

### Step 2: Access the API Documentation

Once the server is running, you can access the interactive API documentation (Swagger UI) at:

```
http://localhost:8000/docs
```
You can use this interface to test the `/query` endpoint.

### Step 3: Example API Call (using curl)

```bash
curl -X POST "http://localhost:8000/query" \
-H "Content-Type: application/json" \
-d '{ "question": "What is the purpose of a ROS 2 node?" }'
```

This will send a sample question to the API and return the generated answer and source URLs.
