---

description: "Task list for Physical AI & Humanoid Robotics Textbook Content Development"
---

# Tasks: Physical AI & Humanoid Robotics Textbook Content Development

**Input**: Design documents from `/specs/001-robotics-syllabus/`
**Prerequisites**: plan.md, spec.md, data-model.md, contracts/rag-api.md

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story?] Description with file path`

## Path Conventions

- **Frontend (Book)**: `docs/`, `src/` (Docusaurus)
- **Backend (RAG API)**: `backend/app/`, `backend/tests/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure for the book and RAG API.

- [ ] T001 Initialize Docusaurus project in the root directory. (A-1)
- [ ] T002 Create initial book structure in `docs/` and configure `docusaurus.config.js`, `sidebars.js`. (A-1)
- [X] T003 Initialize FastAPI project in `backend/` (app.py, main.py). (B-1)
- [ ] T004 [P] Configure linting and formatting for both frontend (Prettier) and backend (Black, Ruff).
- [ ] T005 [P] Setup `requirements.txt` for the backend with FastAPI, Uvicorn, OpenAI SDK, Qdrant client, and Neon driver in `backend/requirements.txt`. (B-1)
- [ ] T006 Setup environment variables (`.env`) for Qdrant, Neon, and OpenAI credentials in `backend/.env`. (B-1)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [ ] T007 Define the data model for document chunks and metadata in `backend/app/models/data_model.py` based on `data-model.md`. (B-2)
- [ ] T008 Implement Neon Serverless Postgres schema creation and connection logic in `backend/app/db/` (based on `data-model.md`). (B-2)
- [ ] T009 Implement Qdrant Cloud Free Tier connection and collection management logic in `backend/app/vector_db/qdrant_client.py`. (B-3)
- [ ] T010 Implement the document chunking logic in `backend/app/services/ingestion_service.py` (e.g., 1000 char chunks with overlap). (B-3)
- [ ] T011 Implement embedding generation using OpenAI SDK in `backend/app/services/embedding_service.py`. (B-3)
- [ ] T012 Develop the ingestion script `backend/scripts/ingest_content.py` to: 1. Read Docusaurus Markdown files. 2. Chunk text (T010). 3. Generate embeddings (T011). 4. Store vectors in Qdrant (T009). 5. Store metadata in Neon (T008). (B-3)
- [ ] T013 Implement basic FastAPI application structure and routing in `backend/app/main.py`. (B-4)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel.

---

## Phase 3: User Story 1 - Learn Physical AI Foundations (P1) 🎯 MVP

**Goal**: Students can understand foundational Physical AI concepts through textbook content.

**Independent Test**: Review content of `docs/module-1/ch1-foundations.md` and `docs/module-1/ch2-ros2-architecture.md` for clarity and completeness.

### Implementation for User Story 1

- [ ] T014 Create Module 1 folders: `docs/module-1/`. (A-2)
- [ ] T015 Create chapter placeholder markdown files for Module 1 in `docs/module-1/`. (A-2)
- [ ] T016 Write content for Chapter 1 (Physical AI Foundations) in `docs/module-1/ch1-foundations.md`. (A-3)
- [ ] T017 Write content for Chapter 2 (ROS 2 Architecture) in `docs/module-1/ch2-ros2-architecture.md`. (A-3)
- [ ] T018 Run ingestion script (T012) for newly created content to populate Qdrant and Neon. (B-3)

**Checkpoint**: User Story 1 content is available and indexed for RAG.

---

## Phase 4: User Story 2 - Master ROS 2 Fundamentals (P1)

**Goal**: Students can learn ROS 2 core concepts and build basic Python packages.

**Independent Test**: Implement a basic ROS 2 package using concepts from relevant chapters and verify its functionality.

### Implementation for User Story 2

- [ ] T019 Write content for Chapter 3 (rclpy Agents) in `docs/module-1/ch3-rclpy-agents.md`, including Python code snippets. (A-3)
- [ ] T020 Write content for Chapter 4 (URDF/Launch Files) in `docs/module-1/ch4-urdf-launch-files.md`. (A-3)
- [ ] T021 Detail Assessment 1: ROS 2 Package Development Project in `docs/assessments/assessment1.md`. (A-3)
- [ ] T022 Run ingestion script (T012) for newly created content. (B-3)

**Checkpoint**: User Story 2 content is available and indexed for RAG.

---

## Phase 5: User Story 3 - Simulate Robots with Gazebo & Unity (P2)

**Goal**: Students can set up and simulate robots in Gazebo and Unity.

**Independent Test**: Successfully set up a simulated robot environment in Gazebo or Unity and verify basic physics and sensor behavior.

### Implementation for User Story 3

- [ ] T023 Create Module 2 folders: `docs/module-2/`. (A-2)
- [ ] T024 Create chapter placeholder markdown files for Module 2 in `docs/module-2/`. (A-2)
- [ ] T025 Write content for Chapter 5 (Gazebo Setup) in `docs/module-2/ch5-gazebo-setup.md`. (A-4)
- [ ] T026 Write content for Chapter 6 (Sensor Simulation: LiDAR, Cameras) in `docs/module-2/ch6-sensor-simulation.md`, including config files. (A-4)
- [ ] T027 Write content for Chapter 7 (Unity HRI) in `docs/module-2/ch7-unity-hri.md`. (A-4)
- [ ] T028 Detail Assessment 2: Gazebo Simulation Implementation in `docs/assessments/assessment2.md`. (A-4)
- [ ] T029 Run ingestion script (T012) for newly created content. (B-3)

**Checkpoint**: User Story 3 content is available and indexed for RAG.

---

## Phase 6: User Story 4 - Develop with NVIDIA Isaac Platform (P2)

**Goal**: Students can develop AI-powered robot tasks using NVIDIA Isaac Sim.

**Independent Test**: Run an example project or develop a small application using Isaac Sim demonstrating perception or manipulation.

### Implementation for User Story 4

- [ ] T030 Create Module 3 folders: `docs/module-3/`. (A-2)
- [ ] T031 Create chapter placeholder markdown files for Module 3 in `docs/module-3/`. (A-2)
- [ ] T032 Write content for Chapter 8 (NVIDIA Isaac Sim/ROS) in `docs/module-3/ch8-isaac-sim-ros.md`. (A-5)
- [ ] T033 Write content for Chapter 9 (VSLAM) in `docs/module-3/ch9-vslam.md`. (A-5)
- [ ] T034 Write content for Chapter 10 (Nav2 for Humanoids) in `docs/module-3/ch10-nav2-humanoids.md`. (A-5)
- [ ] T035 Detail Assessment 3: Isaac-based Perception Pipeline in `docs/assessments/assessment3.md`. (A-5)
- [ ] T036 Run ingestion script (T012) for newly created content. (B-3)

**Checkpoint**: User Story 4 content is available and indexed for RAG.

---

## Phase 7: User Story 5 - Design Humanoid Robots (P3)

**Goal**: Students can understand and propose design considerations for humanoid robots.

**Independent Test**: Understand theoretical concepts and apply them to design problems for humanoid robots.

### Implementation for User Story 5

- [ ] T037 Create Module 4 folders: `docs/module-4/`. (A-2)
- [ ] T038 Create chapter placeholder markdown files for Module 4 in `docs/module-4/`. (A-2)
- [ ] T039 Write content for Chapter 11 (Kinematics) in `docs/module-4/ch11-kinematics.md`. (A-6)
- [ ] T040 Write content for Chapter 12 (Voice-to-Action via Whisper) in `docs/module-4/ch12-voice-to-action.md`, including code snippets. (A-6)
- [ ] T041 Write content for Chapter 13 (Cognitive Planning/Action Sequencing) in `docs/module-4/ch13-cognitive-planning.md`. (A-6)
- [ ] T042 Run ingestion script (T012) for newly created content. (B-3)

**Checkpoint**: User Story 5 content is available and indexed for RAG.

---

## Phase 8: User Story 6 - Integrate Conversational AI (P3)

**Goal**: Students can integrate GPT models for conversational AI in robots.

**Independent Test**: Implement a simple conversational AI interface with a robot simulation or conceptual design.

### Implementation for User Story 6

- [ ] T043 Implement the core FastAPI endpoint (`/query`) in `backend/app/main.py` to handle: retrieval from Qdrant, context framing, and LLM (OpenAI Agents) generation. (B-4)
- [ ] T044 Implement the Context-Aware Q&A feature: modify `/query` endpoint in `backend/app/main.py` to prioritize retrieval based on the optional `user_selected_context` input. (B-5)
- [ ] T045 Create Chapter 14: The Autonomous Humanoid Capstone Project (`docs/capstone/ch14-capstone-project.md`), detailing integration points and Assessment 4. (A-7)
- [ ] T046 Run ingestion script (T012) for Capstone Project content. (B-3)

**Checkpoint**: User Story 6 content is available and RAG API is functional for core features.

---

## Final Phase: Polish & Cross-Cutting Concerns

**Purpose**: Integration, deployment, assessment validation, and final review.

- [ ] T047 Configure GitHub Actions/Pages workflow in `.github/workflows/deploy.yml` for automatic deployment of the Docusaurus site. (A-8)
- [ ] T048 Create a React component for the chat interface in `src/components/ChatInterface.js` and implement client-side API calls to the RAG backend. (B-6)
- [ ] T049 Integrate the Chatbot Frontend (T048) into the deployed Docusaurus site. (C-1)
- [ ] T050 Prepare configuration files (e.g., Dockerfile, Gunicorn setup) for deploying the FastAPI backend service in `backend/`. (B-7)
- [ ] T051 Verify that all four module assessment tasks are fully detailed within the book's content (e.g., `docs/assessments/assessment1.md` through `assessment4.md`). (C-2)
- [ ] T052 Test the full system against the Success Criteria: 1. All claims verified. 2. Zero Plagiarism detected. 3. Passes fact-checking review (RAG accuracy test). (C-3)
- [ ] T053 Code cleanup and refactoring across frontend and backend.
- [ ] T054 Run `quickstart.md` validation, ensuring all instructions are accurate and work as expected.

---

## Dependencies & Execution Order

### Phase Dependencies

-   **Setup (Phase 1)**: No dependencies - can start immediately.
-   **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories.
-   **User Stories (Phase 3+)**: All depend on Foundational phase completion.
    -   User stories can then proceed in parallel (if staffed) or sequentially in priority order (P1 → P2 → P3).
-   **Final Phase (Polish & Cross-Cutting Concerns)**: Depends on all desired user stories being complete.

### User Story Dependencies

-   **User Story 1 (P1)**: Can start after Foundational (Phase 2). No dependencies on other stories for its core content.
-   **User Story 2 (P1)**: Can start after Foundational (Phase 2). Depends on Module 1 content structure (US1).
-   **User Story 3 (P2)**: Can start after Foundational (Phase 2). Depends on Module 2 content structure.
-   **User Story 4 (P2)**: Can start after Foundational (Phase 2). Depends on Module 3 content structure.
-   **User Story 5 (P3)**: Can start after Foundational (Phase 2). Depends on Module 4 content structure.
-   **User Story 6 (P3)**: Can start after Foundational (Phase 2). Depends on RAG API foundational tasks and Capstone Project spec.

### Within Each User Story

-   Content generation tasks for a module should be completed before ingestion script is run for that module.
-   RAG API core implementation (T043) should be completed before key features (T044).
-   Frontend integration (T048) depends on both Docusaurus content deployment (A-8 -> T047) and RAG API backend deployment (B-7 -> T050).

### Parallel Opportunities

-   All tasks within Phase 1 (Setup) marked [P] can run in parallel.
-   Tasks T007 through T013 in Phase 2 (Foundational) can be parallelized where logical, but T012 (ingestion script) depends on T007-T011.
-   Content generation for different user stories can be worked on in parallel by different team members once Foundational tasks are complete (e.g., US1, US2, US3 content can be drafted simultaneously).
-   Frontend integration (T048) can start once the RAG API (T044) is stable and the Docusaurus setup (T002) is complete.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1.  Complete Phase 1: Setup
2.  Complete Phase 2: Foundational
3.  Complete Phase 3: User Story 1
4.  **STOP and VALIDATE**: Test User Story 1 content and its indexing for RAG.
5.  Deploy/demo if ready (partial content).

### Incremental Delivery

1.  Complete Setup + Foundational → Foundation ready.
2.  Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3.  Add User Story 2 → Test independently → Deploy/Demo
4.  ...and so on for all user stories...
5.  Each story adds value without breaking previous stories.

### Parallel Team Strategy

With multiple developers:

1.  Team completes Setup + Foundational together.
2.  Once Foundational is done:
    -   Developer A: User Story 1 & 2 (Content)
    -   Developer B: User Story 3 & 4 (Content)
    -   Developer C: RAG API Core (T043, T044)
    -   Developer D: Frontend Integration (T048) and Deployment (T047, T050)
3.  Stories complete and integrate independently.

---

## Notes

-   Each user story should be independently completable and testable.
-   Verify tests fail before implementing (if tests are added).
-   Commit after each task or logical group.
-   Stop at any checkpoint to validate story independently.
-   Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence.
