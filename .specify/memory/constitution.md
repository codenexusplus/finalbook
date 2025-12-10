<!--
Sync Impact Report:
- Version change: 0.1.0 → 1.0.0
- Modified principles: All principles have been replaced with a new set.
- Added sections: "Key Standards", "Constraints", "Success Criteria".
- Removed sections: All old sections removed.
- Templates requiring updates:
  - ✅ .specify/templates/plan-template.md
  - ✅ .specify/templates/spec-template.md
  - ✅ .specify/templates/tasks-template.md
- Follow-up TODOs:
  - TODO(RATIFICATION_DATE): Determine the original adoption date of this constitution.
-->
# Physical AI & Humanoid Robotics Textbook Constitution

This Constitution establishes the non-negotiable standards for the creation of the AI/Spec-Driven textbook using Docusaurus, GitHub Pages, and the integrated RAG chatbot.

## Core Principles

### Core Principle 1: Technical Accuracy
All technical explanations, code examples, and theoretical concepts must be demonstrably accurate, verified against official documentation (ROS 2, NVIDIA Isaac, etc.).

### Core Principle 2: Educational Clarity
The writing style must be clear, step-by-step, and suitable for a Computer Science academic audience (capstone level).

### Core Principle 3: Architectural Minimalism
Use the minimum viable technology stack and dependencies required to achieve the necessary functionality. Prioritize lightweight and maintainable code.

### Core Principle 4: Free-Tier Viability
The RAG chatbot implementation must strictly adhere to the free-tier limitations of all external cloud services, including Qdrant Cloud and Neon Serverless Postgres.

## Key Standards

### Key Standard 1: Book Platform
The entire textbook must be written in Markdown/MDX and built using Docusaurus, deployed to GitHub Pages.

### Key Standard 2: RAG Scope
The Retrieval-Augmented Generation (RAG) chatbot must be closed-domain, answering questions ONLY based on the book's content.

### Key Standard 3: Tech Stack Enforcement
The RAG backend must exclusively utilize: FastAPI, OpenAI Agents/ChatKit SDKs, Neon Serverless Postgres, and Qdrant Cloud Free Tier.

### Key Standard 4: Plagiarism
0% tolerance for plagiarism in generated text; all text must be original or properly attributed technical paraphrasing.

## Constraints

### Constraint 1: Content Coverage
The book must fully address the syllabus details for all four modules (ROS 2, Gazebo/Unity, NVIDIA Isaac, VLA) and the Capstone Project.

### Constraint 2: Key RAG Feature
The RAG chatbot must support the function of answering questions based specifically on user-selected text within the Docusaurus book.

## Success Criteria

### Success Criterion 1: Full Deployment
The Docusaurus book is successfully deployed and publicly accessible on GitHub Pages.

### Success Criterion 2: Functional RAG
The integrated RAG chatbot is fully operational, retrieves relevant context from the book, and provides accurate answers within the constraints.

## Governance

Amendments to this constitution require documented approval and a migration plan for any affected components. All development and reviews must verify compliance with these principles.

**Version**: 1.0.0 | **Ratified**: TODO(RATIFICATION_DATE): Determine original adoption date | **Last Amended**: 2025-12-09