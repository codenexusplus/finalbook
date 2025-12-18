# Quickstart: Identity & Profile Backend

**Date**: 2025-12-18
**Feature**: Advanced Identity & Profile Orchestration

This guide provides the essential steps to set up and run the backend services for the identity feature.

## Prerequisites

- Python 3.11+
- Poetry for dependency management
- Access to a Neon Serverless Postgres database.

## Setup

1.  **Clone the repository and navigate to the feature branch**:
    ```bash
    git clone <repo_url>
    cd <repo_name>
    git checkout 005-advanced-identity-auth
    ```

2.  **Navigate to the backend directory**:
    ```bash
    cd backend
    ```

3.  **Install dependencies**:
    ```bash
    poetry install
    ```

4.  **Configure Environment Variables**:
    Create a `.env` file in the `backend/` directory with the following content:

    ```env
    # Neon Postgres Database URL
    DATABASE_URL="postgresql+asyncpg://<user>:<password>@<host>:<port>/<dbname>"

    # FastAPI-Users Secret for JWT
    # Generate a secure secret using: openssl rand -hex 32
    AUTH_SECRET="YOUR_SECURE_SECRET_KEY"
    ```

## Running the Service

1.  **Start the FastAPI server**:
    From the `backend/` directory, run:
    ```bash
    poetry run uvicorn src.main:app --reload
    ```

2.  **Access the API Docs**:
    The OpenAPI documentation will be available at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Frontend Integration Note

The Docusaurus frontend will interact with this backend. The `useUserSession` hook will make requests to the `/users/me` endpoint to fetch user data. Ensure the Docusaurus development server is configured to proxy requests to the backend to avoid CORS issues.
