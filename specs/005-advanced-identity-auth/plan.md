# Implementation Plan: Advanced Identity & Profile Orchestration

**Branch**: `005-advanced-identity-auth` | **Date**: 2025-12-18 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `specs/005-advanced-identity-auth/spec.md`

## Summary

This plan outlines the implementation of a secure authentication and user profile system. The primary goal is to enable personalized learning paths by collecting user hardware and skill information. The technical approach is to build a FastAPI backend using the `FastAPI-Users` library for authentication, connected to a Neon Serverless Postgres database. The Docusaurus frontend will be updated with a custom React hook (`useUserSession`) to manage session state and display personalized content.

## Technical Context

**Language/Version**: Python 3.11+ (Backend), JavaScript/TypeScript (Frontend)
**Primary Dependencies**: FastAPI, **FastAPI-Users**, SQLAlchemy (Backend), Docusaurus/React (Frontend)
**Storage**: Neon Serverless Postgres
**Testing**: pytest (Backend), Jest/Vitest (Frontend)
**Target Platform**: GitHub Pages (Frontend), Vercel/Fly.io or similar for FastAPI (Backend)
**Project Type**: Web Application (Docusaurus book + RAG API)
**Performance Goals**: Authentication responses under 2 seconds.
**Constraints**: Must adhere to free-tier limits for all cloud services.
**Scale/Scope**: The authentication system will support the users of the textbook.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [X] **Technical Accuracy**: The proposed work uses `FastAPI-Users`, a well-documented and standard library.
- [X] **Educational Clarity**: The authentication flow is standard and will be familiar to users.
- [X] **Architectural Minimalism**: `FastAPI-Users` provides a minimal, yet complete, solution without adding unnecessary complexity.
- [X] **Free-Tier Viability**: `FastAPI-Users` is a library, not a service, and has no cost. Neon DB usage will be minimal and fit within the free tier.
- [X] **Book Platform**: The frontend changes are designed for Docusaurus/React.
- [X] **RAG Scope**: This feature provides user context to the RAG chatbot but does not change its scope.
- [X] **Tech Stack Enforcement**: The plan exclusively uses the approved stack. "Better-Auth" was identified as a TypeScript library and replaced with the Python-native `FastAPI-Users`.
- [ ] **Content Coverage**: This is an infrastructure feature and does not directly relate to syllabus content.

## Project Structure

### Documentation (this feature)

```text
specs/005-advanced-identity-auth/
├── plan.md              # This file
├── research.md          # Documents the decision to use FastAPI-Users.
├── data-model.md        # Defines the 'user' table schema with a JSONB 'profile' field.
├── quickstart.md        # Provides setup and run instructions for the backend service.
├── contracts/
│   └── api.yaml         # OpenAPI specification for the authentication and profile API.
└── tasks.md             # To be created by /sp.tasks
```

### Source Code (repository root)

This feature requires a clear separation between the backend authentication service and the Docusaurus frontend.

```text
backend/
├── src/
│   ├── auth/            # Authentication-related code, routers from FastAPI-Users
│   ├── models/          # SQLAlchemy user model
│   ├── main.py          # Main FastAPI application
│   └── core/            # Core configuration (e.g., database connection)
└── .env.example         # Example environment file

physical-ai-book/
├── src/
│   ├── components/
│   │   ├── AuthButtons.js   # Sign In / Profile buttons
│   │   └── OnboardingFlow.js  # Multi-step profile form
│   ├── theme/
│   │   └── Navbar/index.js  # To add the AuthButtons
│   └── hooks/
│       └── useUserSession.js # Hook to get user session data
└── docusaurus.config.js
```

**Structure Decision**: The existing project structure with a `backend` directory for the FastAPI app and `physical-ai-book` for the Docusaurus frontend will be used. New files for authentication logic will be added to the `backend`, and new React components and hooks will be added to the `physical-ai-book` frontend.

## Complexity Tracking

No constitutional violations were identified.