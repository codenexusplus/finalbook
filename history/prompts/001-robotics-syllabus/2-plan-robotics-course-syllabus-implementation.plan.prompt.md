---
id: 2
title: Plan Robotics Course Syllabus Implementation
stage: plan
date: 2025-12-09
surface: agent
model: gemini
feature: 001-robotics-syllabus
branch: 001-robotics-syllabus
user: batool1
command: /sp.plan
labels: [planning, textbook, robotics]
links:
  spec: specs/001-robotics-syllabus/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-robotics-syllabus/plan.md
  - specs/001-robotics-syllabus/research.md
  - specs/001-robotics-syllabus/data-model.md
  - specs/001-robotics-syllabus/quickstart.md
  - specs/001-robotics-syllabus/contracts/rag-api.md
  - GEMINI.md
tests:
  - none
---

## Prompt

/sp.plan takes the detailed specification and converts it into a structured sequence of work. This is where the project is broken into Epics and ordered Tasks (often called "tickets") with an estimated level of effort, ensuring we build the book and the RAG system correctly, adhering to the Constitution.Here is the high-level execution plan, structured by Epics and Phases:🗓️ /sp.plan - Technical Implementation PlanThe plan is divided into two major Epics: EPIC A: Textbook Content & Structure and EPIC B: Integrated RAG Chatbot. This allows content creation and backend development to proceed in parallel where possible.EPIC A: Textbook Content & Structure (Docusaurus)Goal: Create the Docusaurus project, structure the 14 chapters, and write all content based on the Specification.IDPhaseTask DescriptionEstimated EffortDependenciesA-1SetupInitialize the Docusaurus project structure (docs/, sidebars.js, docusaurus.config.js).LowNoneA-2StructureCreate the four module folders (module-1 to module-4) and the 14 chapter markdown files (e.g., module-1/ch1-foundations.md).LowA-1A-3Module 1 ContentGenerate content for Chapters 1-4 (Physical AI, ROS 2 Core, rclpy, URDF) and include all Python code snippets.MediumA-2A-4Module 2 ContentGenerate content for Chapters 5-7 (Gazebo, Sensor Sims, Unity HRI) including simulation XML/YAML configurations.MediumA-2A-5Module 3 ContentGenerate content for Chapters 8-10 (NVIDIA Isaac Sim/ROS, VSLAM, Nav2 for Humanoids).MediumA-2A-6Module 4 ContentGenerate content for Chapters 11-13 (Kinematics, VLA, Cognitive Planning).MediumA-2A-7CapstoneWrite the full specification for Chapter 14: The Autonomous Humanoid Capstone Project, detailing the integration points.LowA-6A-8DeployConfigure GitHub Actions/Pages for automatic book deployment upon content merge.LowA-1, A-7EPIC B: Integrated RAG Chatbot (FastAPI, Qdrant, Neon)Goal: Build the full RAG pipeline and integrate the chat interface into the Docusaurus site, adhering to the Free-Tier Viability and RAG Isolation principles.IDPhaseTask DescriptionEstimated EffortDependenciesB-1SetupInitialize the FastAPI project (app.py, requirements.txt). Configure a base .env file for Qdrant and Neon credentials.LowA-1B-2Data ModelDefine the data model for document chunks and metadata (e.g., source_file, chapter_id). Set up the Neon Serverless Postgres schema.MediumB-1B-3Ingestion ScriptDevelop the Python script to: 1. Read Docusaurus Markdown files. 2. Chunk text (e.g., 1000 char chunks with overlap). 3. Generate embeddings. 4. Store vectors in Qdrant Cloud Free Tier. 5. Store metadata in Neon Postgres.HighA-3 (Need initial content), B-2B-4Core RAG APIImplement the core FastAPI endpoint (/query) to handle: retrieval from Qdrant, context framing, and LLM (OpenAI Agents) generation. Enforce RAG Isolation.MediumB-3B-5Key Feature ImplementationModify the /query endpoint to accept an optional user_selected_context string and prioritize retrieval based on this input (adhering to Constraint 2).HighB-4B-6Frontend IntegrationCreate a React component in Docusaurus to host the chat interface. Implement the API client and logic for sending selected text to the backend.MediumA-1, B-5B-7DeploymentPrepare configuration files (e.g., Dockerfile, Gunicorn setup) for deploying the FastAPI backend service.LowB-5🏁 Final Assessment and Review Phase (Weeks 11-13)IDPhaseTask DescriptionWeekly FocusDeliverable/CriterionC-1IntegrationIntegrate the Chatbot Frontend (B-6) into the deployed Docusaurus site (A-8).Week 12Integrated SystemC-2Assessment ValidationVerify that all four module assessment tasks are fully detailed within the book's content.Week 13Complete Assessment GuidanceC-3Final ReviewTest the full system against the Success Criteria: 1. All claims verified. 2. Zero Plagiarism detected. 3. Passes fact-checking review (RAG accuracy test).Week 13Success Criteria Met

## Response snapshot

The implementation planning workflow for the "Physical AI & Humanoid Robotics Textbook Content Development" feature has been completed.

-   **Branch**: `001-robotics-syllabus`
-   **IMPL_PLAN path**: `specs/001-robotics-syllabus/plan.md`
-   **Generated artifacts**:
    *   `specs/001-robotics-syllabus/research.md` (empty, as no clarifications were needed)
    *   `specs/001-robotics-syllabus/data-model.md`
    *   `specs/001-robotics-syllabus/quickstart.md`
    *   `specs/001-robotics-syllabus/contracts/rag-api.md`
    *   `GEMINI.md` (updated agent context)

## Outcome

- ✅ Impact: A detailed implementation plan, data model, API contracts, and quickstart guide have been generated.
- 🧪 Tests: No tests were run, as this was a planning task.
- 📁 Files: `plan.md`, `research.md`, `data-model.md`, `quickstart.md`, `rag-api.md`, and `GEMINI.md` were created/updated.
- 🔁 Next prompts: The user can now proceed with task breakdown (`/sp.tasks`).
- 🧠 Reflection: The planning process successfully integrated the user's high-level plan into the template, creating necessary design artifacts. The agent context was also updated with relevant technical details.

## Evaluation notes (flywheel)

- Failure modes observed: None during this step, as manual intervention was used to set up the feature branch due to previous script issues.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): n/a
