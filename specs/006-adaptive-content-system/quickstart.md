# Quickstart: AI-Native Identity & Adaptive Content System Backend

**Date**: 2025-12-18
**Feature**: AI-Native Identity & Adaptive Content System

This guide provides the essential steps to set up and run the extended backend services for identity, profile management, and AI-driven content adaptation.

## Prerequisites

-   Python 3.11+
-   Poetry for dependency management
-   Access to a Neon Serverless Postgres database.
-   OpenAI API Key

## Setup

1.  **Clone the repository and navigate to the feature branch**:
    ```bash
    git clone <repo_url>
    cd <repo_name>
    git checkout 006-adaptive-content-system
    ```

2.  **Navigate to the backend directory**:
    ```bash
    cd backend
    ```

3.  **Install dependencies**:
    ```bash
    poetry install
    ```
    (Ensure `openai` is included in `pyproject.toml` or `requirements.txt`)

4.  **Configure Environment Variables**:
    Create a `.env` file in the `backend/` directory with the following content:

    ```env
    # Neon Postgres Database URL
    DATABASE_URL="postgresql+asyncpg://<user>:<password>@<host>:<port>/<dbname>"

    # FastAPI-Users Secret for JWT
    # Generate a secure secret using: openssl rand -hex 32
    AUTH_SECRET="YOUR_SECURE_SECRET_KEY"

    # OpenAI API Key for Translation Service
    OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
    ```

## Running the Service

1.  **Start the FastAPI server**:
    From the `backend/` directory, run:
    ```bash
    poetry run uvicorn src.main:app --reload
    ```

2.  **Access the API Docs**:
    The OpenAPI documentation, including the new `/api/translate` and `/api/profile` endpoints, will be available at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Frontend Integration Notes

-   **Root Wrapper**: The Docusaurus `Root.js` component (potentially `physical-ai-book/src/theme/Root.js`) will manage the global authentication and profile state.
-   **Personalization**: A custom React component (`AdaptiveContent`) will wrap chapter text and conditionally render based on the user's profile from the global state.
-   **Navbar UI**: The Docusaurus Navbar (`physical-ai-book/src/theme/Navbar/index.js`) will be swizzled to add "Sign-In", "Profile", and "Language" toggles.
-   **Translation**: Frontend components will make requests to the `/api/translate` endpoint, sending Markdown content and receiving translated Markdown in return.
