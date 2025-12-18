# Contract: Ingestion CLI

**Date**: 2025-12-15
**Feature**: [Embedding Pipeline Setup](spec.md)

This document defines the command-line interface for the `main.py` ingestion script.

## 1. Command Syntax

The script is executed using Python. It takes a single primary argument to specify the starting URL for crawling.

```bash
python main.py --start-url <URL>
```

## 2. Arguments

-   **`--start-url`** (string, required)
    -   Description: The initial URL to begin the site crawl. The crawler will be restricted to the domain of this URL.
    -   Example: `https://finalbook-ss4z.vercel.app/`

-   **`--collection-name`** (string, optional)
    -   Description: The name of the Qdrant collection to use.
    -   Default: `rag_embedding`

## 3. Environment Variables

The script requires API keys and service URLs to be configured in a `.env` file in the same directory.

-   **`COHERE_API_KEY`** (required)
    -   Description: Your API key for the Cohere service.

-   **`QDRANT_URL`** (required)
    -   Description: The URL of your Qdrant Cloud instance.

-   **`QDRANT_API_KEY`** (required)
    -   Description: The API key for your Qdrant Cloud instance.

## 4. Execution Flow

1.  The script parses the command-line arguments.
2.  It loads the environment variables from the `.env` file.
3.  It initializes the Cohere and Qdrant clients.
4.  It begins the crawling process starting from the `--start-url`.
5.  For each valid page, it extracts, cleans, and chunks the text.
6.  For each chunk, it generates an embedding using Cohere.
7.  It upserts the vector and its payload (text, source URL) into the specified Qdrant collection.
8.  The script logs progress and errors to standard output.
