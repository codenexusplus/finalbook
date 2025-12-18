# RAG Embedding Pipeline Backend

This `backend` directory contains the Python script to ingest documentation from a Docusaurus site, generate embeddings using Cohere, and store them in a Qdrant vector database.

## Setup

Refer to the project's main `quickstart.md` for detailed setup instructions.

### Prerequisites

-   Python 3.11+
-   Access to Cohere and Qdrant Cloud to obtain API keys.

### Local Setup

1.  **Navigate to the `backend` directory:**
    ```bash
    cd backend
    ```

2.  **Create a Virtual Environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows: venv\Scripts\activate
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    Create a `.env` file in this directory with your API keys and service URLs:
    ```
    COHERE_API_KEY="your-cohere-api-key"
    QDRANT_URL="https://your-qdrant-cloud-url.qdrant.tech:6333"
    QDRANT_API_KEY="your-qdrant-api-key"
    ```

## Execution

Run the ingestion script from within the `backend` directory.

### Example

```bash
python main.py --start-url https://finalbook-ss4z.vercel.app/
```

### Arguments

-   `--start-url`: The initial URL to begin crawling. The crawler will be restricted to the domain of this URL. (e.g., `https://finalbook-ss4z.vercel.app/`)
-   `--collection-name`: (Optional) The name of the Qdrant collection to use. Defaults to `rag_embedding`.

The script will log its progress and any errors to the console.
