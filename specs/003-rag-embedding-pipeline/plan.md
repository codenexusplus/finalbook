# Implementation Plan: Embedding Pipeline Setup

**Branch**: `003-rag-embedding-pipeline` | **Date**: 2025-12-15 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/003-rag-embedding-pipeline/spec.md`

## Summary

This plan outlines the creation of a Python-based ingestion pipeline. The pipeline will crawl a Docusaurus website, extract text content, generate embeddings using a specified service, and store them in a Qdrant vector database. This is the backend process required to populate the data source for the RAG chatbot. The implementation will be a single script as requested, designed for manual execution.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: `cohere`, `qdrant-client`, `beautifulsoup4`, `requests`
**Storage**: Qdrant Cloud (Vector DB)
**Testing**: `pytest` for unit tests.
**Target Platform**: The script will be run in a local or containerized backend environment.
**Project Type**: Backend data processing script.
**Performance Goals**: Ingestion of 100 pages in under 10 minutes.
**Constraints**: Must adhere to free-tier limits for all cloud services (Qdrant, Cohere). The script will be designed to be runnable from a CLI.
**Scale/Scope**: Closed-domain RAG based on the book content available at the specified URL.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [X] **Technical Accuracy**: Yes. The proposed work is verifiable against Cohere and Qdrant documentation.
- [X] **Educational Clarity**: Yes. The approach is straightforward for the target developer audience.
- [X] **Architectural Minimalism**: Yes. A single script is the simplest viable approach.
- [X] **Free-Tier Viability**: Yes. The design will use the free tiers of Cohere and Qdrant.
- [X] **Book Platform**: Yes. The plan is to ingest content from a Docusaurus site.
- [X] **RAG Scope**: Yes. The scope is strictly limited to the book's content.
- [ ] **Tech Stack Enforcement**: **FAIL**. The plan uses **Cohere** for embeddings as per the user's request, which is not in the approved stack (`OpenAI SDKs`). This requires a constitution amendment or a change in the plan.
- [X] **Content Coverage**: Yes. This plan covers the backend requirements for the RAG system.

## Project Structure

### Documentation (this feature)

```text
specs/003-rag-embedding-pipeline/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
│   └── cli-interface.md 
└── tasks.md             # Phase 2 output (created by /sp.tasks)
```

### Source Code (repository root)

```text
backend/
├── main.py
├── requirements.txt
└── .env
```

**Structure Decision**: A new `backend` directory will be created at the repository root. It will contain a single `main.py` script for the pipeline, a `requirements.txt` for dependencies, and a `.env` file for managing API keys and secrets. This adheres to the user's request for a simple, self-contained backend setup.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| **Tech Stack Enforcement (Cohere)** | The user explicitly requested the use of **Cohere** for embedding generation in the prompt. | The constitutionally approved alternative is using an **OpenAI** model. This was rejected to align with the direct user request, pending a formal decision on a constitution amendment. |