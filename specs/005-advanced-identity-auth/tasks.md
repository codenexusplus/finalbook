# Tasks: Advanced Identity & Profile Orchestration

**Input**: Design documents from `specs/005-advanced-identity-auth/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Frontend (Book)**: `physical-ai-book/src/`
- **Backend (API)**: `backend/src/`

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization for the new backend and frontend components.

- [ ] T001 [P] Initialize poetry in the `backend/` directory and add dependencies: `fastapi`, `uvicorn`, `fastapi-users[sqlalchemy]`, `psycopg2-binary`, `python-dotenv`, `sqlalchemy[asyncio]`, `asyncpg`.
- [ ] T002 [P] Create the initial backend directory structure: `backend/src/auth/`, `backend/src/models/`, `backend/src/core/`.
- [ ] T003 [P] Create the initial frontend directory structure: `physical-ai-book/src/components/`, `physical-ai-book/src/hooks/`.

---

## Phase 2: Foundational (Backend Prerequisites)

**Purpose**: Core backend infrastructure that MUST be complete before ANY user story can be implemented.

- [ ] T004 Create the database connection and SQLAlchemy engine in `backend/src/core/db.py`.
- [ ] T005 Define the `User` SQLAlchemy model in `backend/src/models/user.py` with the `profile` JSONB column as per `data-model.md`.
- [ ] T006 Define Pydantic schemas for `UserRead`, `UserCreate`, and a new `UserUpdate` with the `profile` field in `backend/src/auth/schemas.py`.
- [ ] T007 Configure the `FastAPIUsers` instance with the SQLAlchemy adapter and JWT strategy in `backend/src/auth/manager.py`.
- [ ] T008 Create the main FastAPI app in `backend/src/main.py` and include the auth routers from `FastAPIUsers`.
- [ ] T009 [P] Add CORS middleware configuration to `backend/src/main.py` to allow requests from the frontend.

**Checkpoint**: Foundation ready - user story implementation can now begin.

---

## Phase 3: User Story 1 - New User Onboarding (Priority: P1) 🎯 MVP

**Goal**: A new user can sign up, be prompted for profile information, and have it saved.

**Independent Test**: A user can register via the `/register` endpoint. Immediately after, they can submit their profile data via the `/users/me/profile` endpoint, and the data is persisted in the database.

### Implementation for User Story 1

- [ ] T010 [US1] The default `fastapi_users.router.get_register_router` already provides the `/register` endpoint. This task is to integrate it into `main.py` and verify it works with the custom `User` model.
- [ ] T011 [P] [US1] Implement a custom endpoint `PUT /users/me/profile` that allows an authenticated user to update their own `profile` JSONB field in a new file `backend/src/auth/profile_router.py`.
- [ ] T012 [US1] Add the new `profile_router.py` to the main FastAPI app in `backend/src/main.py`.
- [ ] T013 [P] [US1] Create the React component for the multi-step onboarding form in `physical-ai-book/src/components/OnboardingFlow.js`. This component should handle form state and submission.

**Checkpoint**: User Story 1 should be functional. A new user can be created and their profile can be updated via API.

---

## Phase 4: User Story 3 - Existing User Sign-in (Priority: P3)

**Goal**: An existing user can sign in, sign out, and their session state is available to the frontend.

**Independent Test**: A user can log in via the `/login` endpoint and receive a session cookie. The frontend `useUserSession` hook can then fetch user data. The user can log out, clearing the session.

### Implementation for User Story 3

- [ ] T014 [US3] The default `fastapi_users.router.get_auth_router` provides `/login` and `/logout`. This task is to integrate it and ensure it uses a secure, `httpOnly` cookie strategy.
- [ ] T015 [P] [US3] Create the `useUserSession.js` React hook in `physical-ai-book/src/hooks/useUserSession.js`. This hook will have a function to fetch data from the `/users/me` endpoint and store user state.
- [ ] T016 [P] [US3] Create the `AuthButtons.js` component in `physical-ai-book/src/components/AuthButtons.js` that displays "Sign In" or "Profile / Sign Out" based on the state from the `useUserSession` hook.
- [ ] T017 [US3] Integrate `AuthButtons.js` into the Docusaurus navbar. This may require swizzling the Navbar component and placing the logic in `physical-ai-book/src/theme/Navbar/index.js`.
- [ ] T018 [US3] Create a React Context provider (`SessionProvider`) to wrap the root of the Docusaurus application in `physical-ai-book/src/theme/Root.js` to make the session available globally.

**Checkpoint**: User Story 3 should be functional. Users can log in and out, and the frontend is aware of the session state.

---

## Phase 5: User Story 2 - Context-Aware Chatbot (Priority: P2)

**Goal**: The RAG chatbot provides context-aware assistance based on the logged-in user's hardware profile.

**Independent Test**: Log in as a user with a defined hardware profile. Ask the chatbot a question where hardware is relevant. Verify the chatbot's response is tailored. Log out and ask the same question. Verify the response is generic.

### Implementation for User Story 2

- [ ] T019 [P] [US2] Modify the existing RAG chatbot frontend component to import and use the `useUserSession` hook to get the user's profile data.
- [ ] T020 [US2] In the chatbot component, when making an API call to the RAG backend, check if the user is authenticated. If so, retrieve the `hardware` profile and prepend it to the user's prompt as a JSON string.

**Checkpoint**: All user stories should now be implemented.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final improvements and documentation.

- [ ] T021 [P] Create the `.env.example` file in the `backend/` directory to document required environment variables.
- [ ] T022 [P] Write a README.md for the `backend/` directory explaining the setup, configuration, and how to run the authentication service.
- [ ] T023 [P] Update the main project README to mention the new authentication feature and link to the backend README.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)** -> **Foundational (Phase 2)** -> **User Stories (Phases 3-5)** -> **Polish (Phase 6)**

### User Story Dependencies

- **Note on Priority vs. Dependency**: While US3 is P3, it is a dependency for US2 (P2). The foundational work enables all stories, but a user must be able to log in before the chatbot can be context-aware. The tasks are ordered to reflect a logical implementation flow.
- **US1 (P1)**: Depends on Foundational.
- **US3 (P3)**: Depends on Foundational.
- **US2 (P2)**: Depends on US3.

### Parallel Opportunities

- **Setup**: T001, T002, and T003 can be done in parallel.
- **Backend/Frontend**: Once the API contract is firm after Phase 2, frontend work (T013, T015, T016, etc.) can begin in parallel with backend endpoint implementation (T011, etc.).

---

## Implementation Strategy

### MVP First (User Story 1 & 3)

1.  Complete Phase 1 (Setup) and Phase 2 (Foundational).
2.  Complete Phase 3 (US1 - Onboarding) and Phase 4 (US3 - Sign-in).
3.  **STOP and VALIDATE**: At this point, users can sign up, sign in, and manage their profile data. This is a complete, valuable MVP.
4.  Deploy/demo if ready.

### Incremental Delivery

1.  Add User Story 2 to the validated MVP.
2.  Complete Phase 6 (Polish).
3.  Each stage adds value without breaking previous functionality.
