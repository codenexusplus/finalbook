# Research: Authentication Strategy

**Date**: 2025-12-18
**Feature**: Advanced Identity & Profile Orchestration

## Decision: Use `FastAPI-Users` for Authentication

The feature specification referenced "Better-Auth," a comprehensive TypeScript-based authentication library. As our backend is mandated by the constitution to be Python/FastAPI, a direct implementation is not feasible.

After research, `FastAPI-Users` was selected as the Python equivalent.

### Rationale

1.  **Constitutional Alignment**: `FastAPI-Users` is a well-established library designed specifically for FastAPI, adhering to `Key Standard 3: Tech Stack Enforcement`.
2.  **Feature Completeness**: It provides all necessary features out-of-the-box, including:
    -   Database integration for user persistence (with SQLAlchemy adapters compatible with Neon/Postgres).
    -   JWT-based session management.
    -   Standard endpoints for login, logout, and user registration.
    -   Extensible user models, allowing for the addition of the required `profile` data.
3.  **Architectural Minimalism**: As a library, it provides a robust foundation without imposing unnecessary architectural overhead, aligning with `Core Principle 3`.
4.  **Security**: It handles password hashing and token management, incorporating security best practices. Session management will be handled via secure, `httpOnly` cookies to mitigate XSS risks.

### Alternatives Considered

1.  **"Better-Auth" (TypeScript)**: Rejected due to incompatibility with the Python/FastAPI backend stack.
2.  **Build a Custom Solution**: Rejected as it would reinvent the wheel and introduce unnecessary complexity and security risks, violating `Core Principle 3: Architectural Minimalism`.
3.  **Auth0 / Okta (External SaaS)**: Rejected as they introduce external dependencies and potential costs that may violate `Core Principle 4: Free-Tier Viability` and `Core Principle 3: Architectural Minimalism`.

## Frontend Integration Strategy

-   **Library**: Docusaurus is a React-based framework.
-   **Session Management**: The backend will set a secure, `httpOnly` cookie containing the JWT upon successful login. This cookie will be automatically sent by the browser on subsequent requests. This is a standard and secure method for SPAs.
-   **Custom Hook (`useUserSession`)**: A React Context provider will be created to wrap the Docusaurus application. This provider will be responsible for fetching the current user's data from a `/users/me` endpoint upon initial load. The `useUserSession` hook will provide components with access to the user's session data, authentication status, and profile.
