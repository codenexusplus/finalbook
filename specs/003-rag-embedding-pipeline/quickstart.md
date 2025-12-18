# Quickstart: Embedding Pipeline

**Date**: 2025-12-15
**Feature**: [Embedding Pipeline Setup](spec.md)

This guide provides the steps to set up and run the backend embedding pipeline script.

## 1. Prerequisites

-   Python 3.11+
-   Access to Cohere and Qdrant Cloud to obtain API keys.

## 2. Setup

### Step 1: Create the Project Directory

Create a new folder named `backend` at the root of the repository.

```bash
mkdir backend
cd backend
```

### Step 2: Create a Virtual Environment

It is recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Step 3: Create the Requirements File

Create a file named `requirements.txt` and add the following dependencies:

```
cohere
qdrant-client
beautifulsoup4
requests
python-dotenv
```

### Step 4: Install Dependencies

Install the required packages using pip.

```bash
pip install -r requirements.txt
```

### Step 5: Configure Environment Variables

Create a file named `.env` and add your API keys and service URLs.

```
COHERE_API_KEY="your-cohere-api-key"
QDRANT_URL="https://your-qdrant-cloud-url.qdrant.tech:6333"
QDRANT_API_KEY="your-qdrant-api-key"
```

## 3. Execution

Once the setup is complete, you can run the ingestion script. The main implementation will be in a file named `main.py` inside the `backend` directory.

### Example Command

To run the pipeline and ingest content from the target website, execute the following command from within the `backend` directory:

```bash
python main.py --start-url https://finalbook-ss4z.vercel.app/
```

The script will log its progress to the console, indicating which URLs are being processed and when the data is being saved to Qdrant.
