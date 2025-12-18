# Feature Specification: RAG Query API

**Feature Branch**: `004-rag-query-api`
**Created**: 2025-12-15
**Status**: Draft
**Input**: User description: "RAG Query API: Implement a FastAPI endpoint to receive user questions, embed them, retrieve context from Qdrant, and generate answers using Cohere."

## Constitution Alignment *(mandatory)*

- [X] **Technical Accuracy**: Does the spec require features that can be verified for technical accuracy?
- [X] **Educational Clarity**: Is the user experience designed to be clear and educational for the target audience?
- [X] **Architectural Minimalism**: Does the spec avoid unnecessary complexity?
- [X] **Free-Tier Viability**: Are the requirements compatible with free-tier service limitations?
- [X] **Book Platform (Docusaurus)**: Are the requirements compatible with a Docusaurus-based platform?
- [X] **RAG Scope (Closed-Domain)**: Is the scope of any RAG-related functionality strictly limited to the book's content?
- [ ] **Tech Stack Enforcement**: **FAIL**. The plan uses **Cohere** for LLM generation as per the user's request, which is not in the approved stack (`OpenAI SDKs`). This requires a constitution amendment or a change in the plan.
- [X] **Plagiarism**: Does the spec include requirements for originality and attribution?

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Ask a Question (Priority: P1)

As a user, I want to ask a question about the book content through an API, and receive a concise and relevant answer.

**Why this priority**: This is the core functionality of the RAG chatbot and directly addresses the user's need for an interactive question-answering system.

**Independent Test**: Can be fully tested by sending a question to the API and verifying the response for relevance and accuracy against the ingested book content.

**Acceptance Scenarios**:

1.  **Given** the RAG API is deployed and the Qdrant database is populated with book content, **When** a user sends a valid question (e.g., "What is ROS 2?"), **Then** the API returns an answer based on the book's content.
2.  **Given** the RAG API is deployed and the Qdrant database is populated, **When** a user sends a question about a topic not covered in the book, **Then** the API returns a response indicating that it cannot find relevant information.
3.  **Given** the RAG API is deployed, **When** a user sends an empty or invalid question, **Then** the API returns an appropriate error message (e.g., HTTP 400 Bad Request).

---

### User Story 2 - Get Source References (Priority: P2)

As a user, I want the answer to my question to include references to the source documents in the book from which the information was retrieved, so I can verify the answer or explore further.

**Why this priority**: Providing source references increases the trustworthiness and utility of the RAG system, aligning with educational clarity. It's P2 as the primary goal is answering the question.

**Independent Test**: Can be tested by sending a question to the API and verifying that the response includes correctly formatted and relevant source URLs from the Qdrant payload.

**Acceptance Scenarios**:

1.  **Given** a question is answered by the RAG API, **When** the answer is generated, **Then** the API response includes a list of unique URLs from the retrieved chunks that contributed to the answer.

### Edge Cases

-   What happens if no relevant context is retrieved from Qdrant for a given query?
-   How does the system handle very long queries from the user?
-   What if the LLM fails to generate a coherent answer from the provided context?
-   How is the number of retrieved context chunks managed (e.g., top-K)?

## Requirements *(mandatory)*

### Functional Requirements

-   **FR-001**: The system MUST expose an API endpoint (e.g., `/query`) that accepts a user question.
-   **FR-002**: The API MUST embed the user's question using the Cohere `embed-english-v3.0` model.
-   **FR-003**: The API MUST query the Qdrant database for the top-K most relevant text chunks based on the embedded user question.
-   **FR-004**: The API MUST concatenate the retrieved text chunks to form a context for the LLM.
-   **FR-005**: The API MUST send the user's question and the generated context to the Cohere Generation API to generate an answer.
-   **FR-006**: The API MUST return the generated answer to the user.
-   **FR-007**: The API MUST include source URLs from the retrieved Qdrant chunks in the response.
-   **FR-08**: The API MUST handle cases where no relevant context is found and respond gracefully.
-   **FR-09**: The API MUST be configured to use environment variables for Cohere and Qdrant API keys/URLs.

### Key Entities *(include if feature involves data)*

-   **Query**: Represents the user's input question. Attributes: `text` (string).
-   **Context**: Represents the retrieved relevant text chunks from Qdrant. Attributes: `text` (string), `source_url` (string).
-   **Answer**: Represents the generated response from the LLM. Attributes: `text` (string), `sources` (list of strings).

## Success Criteria *(mandatory)*

### Measurable Outcomes

-   **SC-001**: The `/query` API endpoint responds to a simple question within 3 seconds for 95% of requests.
-   **SC-002**: For questions directly answerable by the book content, the RAG API provides an accurate answer with relevant sources in at least 85% of cases (based on a test set).
-   **SC-003**: The API successfully retrieves 3-5 relevant text chunks from Qdrant for a given query in 90% of cases.
-   **SC-004**: The API gracefully handles and reports errors for invalid inputs or external service failures (e.g., Cohere/Qdrant API errors).

## Assumptions

-   The Qdrant database has been pre-populated with embeddings of the book content using the ingestion pipeline.
-   The Cohere API key has access to both embedding and generation models.
-   The FastAPI application will be deployed in an environment with access to the configured Cohere and Qdrant services.