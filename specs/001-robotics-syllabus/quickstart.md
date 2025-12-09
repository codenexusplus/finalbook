# Quickstart Guide: Physical AI & Humanoid Robotics Textbook Development

This quickstart guide provides instructions for setting up the development environment and running the textbook and RAG chatbot locally.

## 1. Prerequisites

Before you begin, ensure you have the following installed:

-   **Git**: For version control.
-   **Node.js** (LTS version): Required for Docusaurus frontend development.
-   **Python 3.11+**: Required for FastAPI backend development.
-   **Docker** (Optional, but recommended): For containerized deployment of the backend.
-   **Poetry** (Optional, but recommended): For Python dependency management.

## 2. Clone the Repository

```bash
git clone [repository_url]
cd book-spec
```

## 3. Frontend Setup (Docusaurus)

The textbook frontend is built using Docusaurus.

```bash
cd my-website # Assuming 'my-website' is the Docusaurus project root
npm install   # Install dependencies
npm start     # Start the local development server
```

Open your browser to `http://localhost:3000` to see the textbook.

## 4. Backend Setup (FastAPI RAG API)

The RAG chatbot backend is built with FastAPI.

```bash
cd backend
# Using Poetry for dependency management
poetry install
poetry shell
```

### 4.1. Environment Configuration

Create a `.env` file in the `backend/` directory based on `.env.example`.

```ini
# .env example
OPENAI_API_KEY=your_openai_api_key
QDRANT_CLOUD_URL=your_qdrant_cloud_url
QDRANT_API_KEY=your_qdrant_api_key
NEON_DATABASE_URL=your_neon_postgres_connection_string
```

Replace the placeholder values with your actual API keys and connection strings. Ensure these services are configured for free-tier usage as per the project constitution.

### 4.2. Run Database Migrations

Set up your Neon Serverless Postgres schema.

```bash
# Assuming you have a migration tool configured, e.g., Alembic
# alembic upgrade head
# Or, if using a simpler approach, a Python script to create tables
python scripts/create_tables.py # (Example placeholder)
```

### 4.3. Run the Ingestion Script

This script reads the Docusaurus Markdown files, chunks them, generates embeddings, and stores them in Qdrant and Neon.

```bash
python scripts/ingest_content.py # (Example placeholder)
```

### 4.4. Start the FastAPI Server

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

The FastAPI RAG API will be available at `http://localhost:8000`.

## 5. Integration

Once both the frontend and backend are running, the Docusaurus React component (Frontend Integration, B-6 in the plan) will interact with the FastAPI backend.

-   Navigate to the Docusaurus site (`http://localhost:3000`).
-   Locate the integrated chat interface.
-   Test asking questions based on the textbook content and using the user-selected text feature.

## 6. Deployment (Local Simulation)

For local testing of deployment artifacts, you can build and run the Docker image for the backend:

```bash
cd backend
docker build -t rag-api .
docker run -p 8000:8000 rag-api
```

This guide focuses on local development. For actual production deployment, refer to specific platform documentation (e.g., GitHub Pages for frontend, chosen cloud provider for backend).
