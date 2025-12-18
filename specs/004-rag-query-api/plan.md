# Implementation Plan: RAG Query API

**Branch**: `004-rag-query-api` | **Date**: 2025-12-15 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/004-rag-query-api/spec.md`

## Summary

This plan outlines the creation of a FastAPI application to serve as the RAG Query API. It will expose an endpoint to receive user questions, embed them using Cohere, retrieve relevant context from Qdrant, and generate answers using Cohere's generation model. The API will also provide source references from the retrieved context.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: FastAPI, `uvicorn`, `cohere`, `qdrant-client`, `python-dotenv`
**Storage**: Qdrant Cloud (Vector DB for context retrieval)
**Testing**: `pytest`
**Target Platform**: Local development, Docker, or cloud deployment for FastAPI.
**Project Type**: RESTful API.
**Performance Goals**: Query responses under 3 seconds for 95% of requests.
**Constraints**: Must adhere to free-tier limits for all cloud services (Qdrant, Cohere).
**Scale/Scope**: Closed-domain RAG based on pre-ingested book content.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [X] **Technical Accuracy**: Yes. The proposed work is verifiable against FastAPI, Cohere, and Qdrant documentation.
- [X] **Educational Clarity**: Yes. The API design is straightforward and suitable for academic understanding.
- [X] **Architectural Minimalism**: Yes. Using FastAPI with direct client integrations is a minimal approach.
- [X] **Free-Tier Viability**: Yes. The design will use the free tiers of Cohere and Qdrant.
- [X] **Book Platform**: Yes. The API interacts with content originating from the Docusaurus book.
- [X] **RAG Scope**: Yes. The API's function is strictly limited to querying the book's content.
- [ ] **Tech Stack Enforcement**: **FAIL**. The plan uses **Cohere** for embedding and generation, which is not in the approved stack (`OpenAI SDKs`). This is a justified deviation based on explicit user instruction.
- [X] **Content Coverage**: Yes. This plan covers the API requirements for the RAG system.

## Project Structure

### Documentation (this feature)

```text
specs/004-rag-query-api/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
│   └── query-api.md
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
fastapi-rag/
├── app.py
├── requirements.txt
├── .env
├── create_schema.py   # Existing - may be adapted or removed
├── ingest.py          # Existing - may be adapted or removed
├── vector_db.py       # Existing - may be adapted or removed
└── __init__.py
```

**Structure Decision**: The existing `fastapi-rag/` directory will be utilized. The core API logic will reside in `app.py`. Dependencies will be managed in `requirements.txt`. Environment variables will be in `.env`. Existing files (`create_schema.py`, `ingest.py`, `vector_db.py`) will be reviewed and potentially refactored or reused if they align with the current plan, otherwise they will be ignored for this feature.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| **Tech Stack Enforcement (Cohere)** | The user explicitly requested the use of **Cohere** for embedding and generation, directly overriding the constitutional preference for **OpenAI** models. | Adherence to user's explicit request. Using OpenAI would require re-evaluation of embedding models and generation strategies already established by user. |