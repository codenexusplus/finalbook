# Tasks: RAG Query API

**Feature**: `004-rag-query-api`
**Spec**: [spec.md](spec.md)
**Plan**: [plan.md](plan.md)

This document outlines the development tasks for implementing the RAG Query API.

## Phase 1: Project Setup

These tasks initialize the FastAPI project structure and dependencies within the `fastapi-rag/` directory.

- [X] T001 Navigate to the `fastapi-rag/` directory if not already there.
- [X] T002 Update `fastapi-rag/requirements.txt` with FastAPI, uvicorn, cohere, qdrant-client, and python-dotenv.
- [X] T003 Create or update `fastapi-rag/.env` with Cohere and Qdrant API keys/URLs.
- [X] T004 Create `fastapi-rag/app.py` as the main FastAPI application file.

## Phase 2: Foundational Implementation

These tasks implement the core setup within `app.py` before the API endpoint logic.

- [X] T005 Implement environment variable loading from `.env` in `fastapi-rag/app.py`.
- [X] T006 Initialize FastAPI app, Cohere client, and Qdrant client in `fastapi-rag/app.py`.
- [X] T007 Define Pydantic models `QueryRequest` and `QueryResponse` in `fastapi-rag/app.py`.

## Phase 3: User Story 1 - Ask a Question (P1)

**Goal**: The API can receive a question and return a generated answer.
**Independent Test**: Send a question to `/query` endpoint and receive a relevant answer.

- [X] T008 [US1] Create POST `/query` endpoint in `fastapi-rag/app.py`.
- [X] T009 [US1] Implement embedding of user query using Cohere `embed-english-v3.0` in `fastapi-rag/app.py`.
- [X] T010 [US1] Implement Qdrant search for relevant text chunks using the embedded query in `fastapi-rag/app.py`.
- [X] T011 [US1] Concatenate retrieved text chunks into a context string in `fastapi-rag/app.py`.
- [X] T012 [US1] Implement answer generation using Cohere Command model with context and query in `fastapi-rag/app.py`.
- [X] T013 [US1] Return the generated answer within a `QueryResponse` object in `fastapi-rag/app.py`.
- [X] T014 [US1] Implement graceful handling for scenarios where no relevant context is found in `fastapi-rag/app.py`.

## Phase 4: User Story 2 - Get Source References (P2)

**Goal**: The API's answer includes references to source documents.
**Independent Test**: Send a question to `/query` and verify that the response includes accurate source URLs.

- [X] T015 [US2] Extract unique source URLs from Qdrant search results in `fastapi-rag/app.py`.
- [X] T016 [US2] Include the extracted source URLs in the `QueryResponse` object in `fastapi-rag/app.py`.

## Phase 5: Polish & Cross-Cutting Concerns

These tasks improve the API's robustness, usability, and maintainability.

- [X] T017 [P] Add comprehensive error handling for API calls (Cohere, Qdrant) and other exceptions in `fastapi-rag/app.py`.
- [X] T018 [P] Implement structured logging for API requests and responses in `fastapi-rag/app.py`.
- [X] T019 [P] Create a `fastapi-rag/README.md` file with setup, run, and usage instructions.

## Dependencies

- **Phase 1 (Setup)** must be completed before any other phase.
- **Phase 2 (Foundational Implementation)** must be completed before starting User Story phases.
- **User Story 1 (US1)** is foundational for User Story 2.
- **User Story 2 (US2)** depends on the full completion of US1.
- **Phase 5 (Polish & Cross-Cutting Concerns)** tasks can generally be done in parallel or at any point after foundational setup, though it's best to address them after core functionality.

## Parallel Execution

- Within Phase 5, tasks T017, T018, and T019 can be executed in parallel as they cover distinct concerns (error handling, logging, documentation).

## Implementation Strategy

The implementation will follow a phased approach, prioritizing User Story 1 to deliver a working API that can answer questions as the Minimum Viable Product (MVP). Once the core question-answering functionality is stable, User Story 2 will add source references. Finally, cross-cutting concerns like robust error handling, logging, and documentation will be addressed to ensure a production-ready API.
