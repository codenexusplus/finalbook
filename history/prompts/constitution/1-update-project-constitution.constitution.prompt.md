---
id: 1
title: Update Project Constitution
stage: constitution
date: 2025-12-09
surface: agent
model: gemini
feature: none
branch: master
user: batool1
command: /sp.constitution
labels: [constitution, documentation]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
  - .specify/templates/plan-template.md
  - .specify/templates/spec-template.md
  - .specify/templates/tasks-template.md
tests:
  - none
---

## Prompt

/sp.constitution  Project Constitution: Physical AI & Humanoid Robotics TextbookThis Constitution establishes the non-negotiable standards for the creation of the AI/Spec-Driven textbook using Docusaurus, GitHub Pages, and the integrated RAG chatbot.CategoryPrinciple/Standard/ConstraintDescriptionCore Principle 1Technical AccuracyAll technical explanations, code examples, and theoretical concepts must be demonstrably accurate, verified against official documentation (ROS 2, NVIDIA Isaac, etc.).Core Principle 2Educational ClarityThe writing style must be clear, step-by-step, and suitable for a Computer Science academic audience (capstone level).Core Principle 3Architectural MinimalismUse the minimum viable technology stack and dependencies required to achieve the necessary functionality. Prioritize lightweight and maintainable code.Core Principle 4Free-Tier ViabilityThe RAG chatbot implementation must strictly adhere to the free-tier limitations of all external cloud services, including Qdrant Cloud and Neon Serverless Postgres.Key Standard 1Book PlatformThe entire textbook must be written in Markdown/MDX and built using Docusaurus, deployed to GitHub Pages.Key Standard 2RAG ScopeThe Retrieval-Augmented Generation (RAG) chatbot must be closed-domain, answering questions ONLY based on the book's content.Key Standard 3Tech Stack EnforcementThe RAG backend must exclusively utilize: FastAPI, OpenAI Agents/ChatKit SDKs, Neon Serverless Postgres, and Qdrant Cloud Free Tier.Key Standard 4Plagiarism0% tolerance for plagiarism in generated text; all text must be original or properly attributed technical paraphrasing.Constraint 1Content CoverageThe book must fully address the syllabus details for all four modules (ROS 2, Gazebo/Unity, NVIDIA Isaac, VLA) and the Capstone Project.Constraint 2Key RAG FeatureThe RAG chatbot must support the function of answering questions based specifically on user-selected text within the Docusaurus book.Success Criterion 1Full DeploymentThe Docusaurus book is successfully deployed and publicly accessible on GitHub Pages.Success Criterion 2Functional RAGThe integrated RAG chatbot is fully operational, retrieves relevant context from the book, and provides accurate answers within the constraints.📝 (Alternate) Constitution for the Research PaperIf you were to only focus on the Research Paper on AI-Native Software Development, the Constitution would be:CategoryPrinciple/Standard/ConstraintDescriptionCore PrincipleRigorPeer-reviewed academic sources are preferred.Core PrincipleReproducibilityAll claims must be cited and traceable to a source.Core PrincipleClarityWriting must be suitable for an academic (Computer Science) audience.Key StandardCitation FormatAPA Style must be used for all citations and references.Key StandardSource TypeMinimum 50% peer-reviewed articles required.Key StandardPlagiarism Check0% tolerance before submission.ConstraintWord Count5,000-7,000 words.ConstraintSource CountMinimum 15 sources.Success CriterionVerificationAll claims verified against sources and passes fact-checking review.

## Response snapshot

I have updated the project constitution to version 1.0.0 based on your input. This involved replacing the content of `.specify/memory/constitution.md` with the principles for the "Physical AI & Humanoid Robotics Textbook".

I also updated the following templates to ensure they are aligned with the new constitution:
- `.specify/templates/plan-template.md`
- `.specify/templates/spec-template.md`
- `.specify/templates/tasks-template.md`

A Prompt History Record has been created at `history/prompts/constitution/1-update-project-constitution.constitution.prompt.md`.

## Outcome

- ✅ Impact: Major update to the project's guiding principles.
- 🧪 Tests: No tests were run as this was a documentation change.
- 📁 Files: 4 files were modified.
- 🔁 Next prompts: The user might want to commit these changes.
- 🧠 Reflection: The process of updating the constitution and propagating the changes to dependent templates was successful. The fallback mechanism for PHR creation worked as expected.

## Evaluation notes (flywheel)

- Failure modes observed: The initial attempt to list files in a non-existent directory failed, which was handled by creating the directory. The shell script for PHR creation was not used due to the Windows environment.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): n/a
