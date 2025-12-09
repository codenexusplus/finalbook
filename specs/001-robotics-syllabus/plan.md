# Implementation Plan: Physical AI & Humanoid Robotics Textbook Content Development

**Branch**: `001-robotics-syllabus` | **Date**: 2025-12-09 | **Spec**: [specs/001-robotics-syllabus/spec.md](specs/001-robotics-syllabus/spec.md)
**Input**: Feature specification from `/specs/001-robotics-syllabus/spec.md`

## Summary

This plan outlines the development of the "Physical AI & Humanoid Robotics Textbook," which includes creating the Docusaurus-based content and an integrated Retrieval-Augmented Generation (RAG) chatbot. The textbook will cover foundational Physical AI principles, ROS 2, robot simulation with Gazebo and Unity, NVIDIA Isaac platform development, humanoid robot design, and conversational AI integration with GPT models. The RAG chatbot will provide closed-domain answers based on the book's content, adhering to free-tier cloud service limitations.

## Technical Context

<!--
  ACTION REQUIRED: The constitution has set the primary technology stack.
  Verify and fill in any remaining details for this specific feature.
-->

**Language/Version**: Python 3.11+ (Backend), JavaScript/TypeScript (Frontend)
**Primary Dependencies**: FastAPI (Backend), Docusaurus/React (Frontend), OpenAI SDKs, Qdrant Client
**Storage**: Neon Serverless Postgres
**Testing**: pytest (Backend), Jest/Vitest (Frontend)
**Target Platform**: GitHub Pages (Frontend), Cloud Hosting for FastAPI (Backend)
**Project Type**: Web Application (Docusaurus book + RAG API)
**Performance Goals**: Fast page loads for the book, RAG responses under 5 seconds.
**Constraints**: Must adhere to free-tier limits for all cloud services (Qdrant, Neon).
**Scale/Scope**: Closed-domain RAG based on book content.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [X] **Technical Accuracy**: Is the proposed work verifiable against source documentation?
- [X] **Educational Clarity**: Is the approach suitable for the target academic audience?
- [X] **Architectural Minimalism**: Does this plan use the simplest viable technology stack?
- [X] **Free-Tier Viability**: Does the design respect free-tier limits of Qdrant and Neon?
- [X] **Book Platform**: Does this align with the Docusaurus/MDX-based platform?
- [X] **RAG Scope**: Is the scope strictly limited to the book's content?
- [X] **Tech Stack Enforcement**: Does the plan exclusively use the approved stack (FastAPI, OpenAI, Neon, Qdrant)?
- [X] **Content Coverage**: Does this plan address the required syllabus modules?

## Project Structure

### Documentation (this feature)

```text
specs/001-robotics-syllabus/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
# Web application structure for Docusaurus frontend and FastAPI backend
backend/
├── app/                  # FastAPI application
│   ├── api/
│   ├── models/
│   └── services/
└── tests/                # Backend tests

docs/                     # Docusaurus documentation (book content)
└── ...

src/                      # Docusaurus source (components, pages)
└── ...

# Other project-level files
```

**Structure Decision**: The project will follow a web application structure with a `backend/` directory for the FastAPI RAG API and `docs/` and `src/` for the Docusaurus frontend. This aligns with the "Book Platform" key standard and "Tech Stack Enforcement" principle.

## Technical Implementation Plan

The plan is divided into two major Epics: EPIC A: Textbook Content & Structure and EPIC B: Integrated RAG Chatbot. This allows content creation and backend development to proceed in parallel where possible.

### EPIC A: Textbook Content & Structure (Docusaurus)

**Goal**: Create the Docusaurus project, structure the 14 chapters, and write all content based on the Specification.

| ID    | Phase      | Task Description                                                                                 | Estimated Effort | Dependencies       |
| :---- | :--------- | :----------------------------------------------------------------------------------------------- | :--------------- | :----------------- |
| A-1   | Setup      | Initialize the Docusaurus project structure (`docs/`, `sidebars.js`, `docusaurus.config.js`).     | Low              | None               |
| A-2   | Structure  | Create the four module folders (module-1 to module-4) and the 14 chapter markdown files (e.g., `module-1/ch1-foundations.md`). | Low              | A-1                |
| A-3   | Module 1 Content | Generate content for Chapters 1-4 (Physical AI, ROS 2 Core, rclpy, URDF) and include all Python code snippets. | Medium           | A-2                |
| A-4   | Module 2 Content | Generate content for Chapters 5-7 (Gazebo, Sensor Sims, Unity HRI) including simulation XML/YAML configurations. | Medium           | A-2                |
| A-5   | Module 3 Content | Generate content for Chapters 8-10 (NVIDIA Isaac Sim/ROS, VSLAM, Nav2 for Humanoids).          | Medium           | A-2                |
| A-6   | Module 4 Content | Generate content for Chapters 11-13 (Kinematics, VLA, Cognitive Planning).                     | Medium           | A-2                |
| A-7   | Capstone   | Write the full specification for Chapter 14: The Autonomous Humanoid Capstone Project, detailing the integration points. | Low              | A-6                |
| A-8   | Deploy     | Configure GitHub Actions/Pages for automatic book deployment upon content merge.                 | Low              | A-1, A-7           |

### EPIC B: Integrated RAG Chatbot (FastAPI, Qdrant, Neon)

**Goal**: Build the full RAG pipeline and integrate the chat interface into the Docusaurus site, adhering to the Free-Tier Viability and RAG Isolation principles.

| ID    | Phase      | Task Description                                                                                 | Estimated Effort | Dependencies       |
| :---- | :--------- | :----------------------------------------------------------------------------------------------- | :--------------- | :----------------- |
| B-1   | Setup      | Initialize the FastAPI project (`app.py`, `requirements.txt`). Configure a base `.env` file for Qdrant and Neon credentials. | Low              | A-1                |
| B-2   | Data Model | Define the data model for document chunks and metadata (e.g., `source_file`, `chapter_id`). Set up the Neon Serverless Postgres schema. | Medium           | B-1                |
| B-3   | Ingestion Script | Develop the Python script to: 1. Read Docusaurus Markdown files. 2. Chunk text (e.g., 1000 char chunks with overlap). 3. Generate embeddings. 4. Store vectors in Qdrant Cloud Free Tier. 5. Store metadata in Neon Postgres. | High             | A-3 (Need initial content), B-2 |
| B-4   | Core RAG API | Implement the core FastAPI endpoint (`/query`) to handle: retrieval from Qdrant, context framing, and LLM (OpenAI Agents) generation. Enforce RAG Isolation. | Medium           | B-3                |
| B-5   | Key Feature Implementation | Modify the `/query` endpoint to accept an optional `user_selected_context` string and prioritize retrieval based on this input (adhering to Constraint 2). | High             | B-4                |
| B-6   | Frontend Integration | Create a React component in Docusaurus to host the chat interface. Implement the API client and logic for sending selected text to the backend. | Medium           | A-1, B-5           |
| B-7   | Deployment | Prepare configuration files (e.g., Dockerfile, Gunicorn setup) for deploying the FastAPI backend service. | Low              | B-5                |

### Final Assessment and Review Phase (Weeks 11-13)

| ID    | Phase      | Task Description                                                                                 | Weekly Focus | Deliverable/Criterion |
| :---- | :--------- | :----------------------------------------------------------------------------------------------- | :----------- | :-------------------- |
| C-1   | Integration | Integrate the Chatbot Frontend (B-6) into the deployed Docusaurus site (A-8).                  | Week 12      | Integrated System     |
| C-2   | Assessment Validation | Verify that all four module assessment tasks are fully detailed within the book's content. | Week 13      | Complete Assessment Guidance |
| C-3   | Final Review | Test the full system against the Success Criteria: 1. All claims verified. 2. Zero Plagiarism detected. 3. Passes fact-checking review (RAG accuracy test). | Week 13      | Success Criteria Met |

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |