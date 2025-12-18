# Research: Adaptive Content System Mechanisms

**Date**: 2025-12-18
**Feature**: AI-Native Identity & Adaptive Content System

## Decision 1: Content Personalization Mechanism

The user's architectural input provided clarity on the implementation for dynamic content adaptation.

### Rationale

-   **Mechanism**: Hiding/showing specific Markdown blocks. This aligns with the "Architectural Minimalism" principle as it's a simpler frontend implementation that leverages Docusaurus's ability to render React components within MDX. It avoids the complexity, latency, and cost associated with on-the-fly LLM-based rewriting.
-   **Implementation**: This will involve creating custom React components that wrap Markdown content. These components will consume user profile data from the React Context and conditionally render their children based on specified hardware requirements or ROS experience levels. Markdown blocks will need to be semantically tagged (e.g., using props on the custom React component) to indicate their relevance to specific profiles.

### Alternatives Considered

-   **Dynamic rewriting via LLM**: Rejected due to higher complexity, potential for increased latency, and LLM costs.
-   **Highlighting relevant sections**: Rejected as less impactful for users with incompatible hardware (hiding content is more direct than merely highlighting).

## Decision 2: Urdu Translation Scope and LLM API

The user's architectural input also clarified the scope and LLM API for translation.

### Rationale

-   **LLM API**: OpenAI's GPT API. This aligns with `Key Standard 3: Tech Stack Enforcement` (which permits OpenAI SDKs for RAG services) and provides a robust, high-quality translation engine.
-   **Scope**: Translate the entire chapter. This simplifies the user experience (a single toggle for full chapter translation) and reduces frontend complexity by not requiring dynamic paragraph selection. It also aligns with the user's architectural guidance for a FastAPI endpoint `/api/translate`.
-   **Implementation**: The frontend will send the entire Markdown content of a chapter to a new FastAPI endpoint (`/api/translate`). The backend will then use OpenAI's GPT API to translate the Markdown content into Urdu and return the translated Markdown. The frontend will then render this translated Markdown.
-   **Considerations**: Potential for higher LLM cost/latency for very long chapters. Strategies for handling this (e.g., caching, loading indicators) will be considered during implementation.

### Alternatives Considered

-   **Translating selected paragraphs/sections**: Rejected due to increased UI/UX complexity for user selection and more complex state management.
-   **Other LLM APIs**: OpenAI GPT API is readily available and familiar within the existing tech stack.
