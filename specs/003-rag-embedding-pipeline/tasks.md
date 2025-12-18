# Tasks: Embedding Pipeline Setup

**Feature**: `003-rag-embedding-pipeline`
**Spec**: [spec.md](spec.md)
**Plan**: [plan.md](plan.md)

This document outlines the development tasks for implementing the RAG embedding pipeline.

## Phase 1: Project Setup

These tasks initialize the backend project structure and dependencies.

- [X] T001 Create the root directory for the backend script at `backend/`.
- [X] T002 Create and populate the dependency file at `backend/requirements.txt`.
- [X] T003 Create an example environment file at `backend/.env.example`.
- [X] T004 Create the main script file at `backend/main.py`.

## Phase 2: Foundational Implementation

These tasks implement the core setup within the script before the main pipeline logic.

- [X] T005 Implement environment variable loading from `.env` in `backend/main.py`.
- [X] T006 Implement CLI argument parsing for `--start-url` in `backend/main.py`.
- [X] T007 Initialize the Cohere and Qdrant clients in `backend/main.py`.

## Phase 3: User Story 1 - Manual Content Ingestion

**Goal**: A developer can manually trigger a pipeline to crawl, embed, and store content.
**Independent Test**: Execute `python main.py --start-url <URL>` and verify that documents are populated in the Qdrant collection.

- [X] T008 [US1] Implement `create_qdrant_collection()` function in `backend/main.py`.
- [X] T009 [US1] Implement `get_all_urls(start_url)` function in `backend/main.py`.
- [X] T010 [US1] Implement `extract_text_from_url(url)` function in `backend/main.py`.
- [X] T011 [US1] Implement `chunk_text(text)` function in `backend/main.py`.
- [X] T012 [US1] Implement `embed_chunks(chunks)` function in `backend/main.py`.
- [X] T013 [US1] Implement `save_chunks_to_qdrant(...)` function in `backend/main.py`.
- [X] T014 [US1] Implement the main execution logic to orchestrate the pipeline in `backend/main.py`.

## Phase 4: User Story 2 - Automated Content Synchronization

**Goal**: The system can be re-run to keep the vector database synchronized.
**Independent Test**: Run the script multiple times and verify that the data in Qdrant is consistent and up-to-date, not duplicated.

- [X] T015 [US2] Ensure the main pipeline in `backend/main.py` is idempotent by clearing and recreating the collection on each run.

## Phase 5: Polish & Cross-Cutting Concerns

These tasks improve the script's robustness and usability.

- [X] T016 [P] Add structured logging to all major functions in `backend/main.py`.
- [X] T017 [P] Add robust error handling for API calls and network issues in `backend/main.py`.
- [X] T018 [P] Create a `backend/README.md` file with setup and execution instructions.

## Dependencies

- **User Story 1 (US1)** is the foundation. All its tasks (T008-T014) must be completed to have a functional MVP.
- **User Story 2 (US2)** depends on the completion of US1. Its task (T015) modifies the idempotent nature of the script.
- **Polish** tasks (T016-T018) can be worked on in parallel after the foundational work in Phase 2 is complete.

## Parallel Execution

- Within Phase 5, tasks T016, T017, and T018 can be executed in parallel as they modify different aspects of the project (logging logic vs. error handling logic vs. documentation).

## Implementation Strategy

The implementation will proceed phase by phase, prioritizing User Story 1 to deliver a working, manually-triggered pipeline as the Minimum Viable Product (MVP). Once the MVP is validated, the focus will shift to ensuring the script can be run repeatedly for automated updates (User Story 2) and finally to improving its operational quality with logging and error handling.
