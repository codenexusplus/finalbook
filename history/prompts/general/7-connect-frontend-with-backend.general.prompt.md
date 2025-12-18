---
id: 7
title: Connect Frontend with Backend
stage: general
date: 2025-12-15
surface: agent
model: (unknown)
feature: none
branch: (unknown)
user: (unknown)
command: plz connect frontend with backend
labels: ["frontend","backend","integration"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - physical-ai-book/src/components/Chatbot/Chatbot.js
tests:
  - Manual verification
---

## Prompt

plz connect frontend with backend

## Response snapshot

Modified physical-ai-book/src/components/Chatbot/Chatbot.js to align data contract between frontend and backend by replacing 'query' with 'question' in the request body and 'response' with 'answer' in the response handling.

## Outcome

- ✅ Impact: Frontend is now configured to send and receive data correctly with the backend's API contract.
- 🧪 Tests: Manual verification by running both services and testing the chatbot functionality.
- 📁 Files: Modified one file to update API request and response field names.
- 🔁 Next prompts: Provide instructions for starting backend and frontend services.
- 🧠 Reflection: Successfully identified data contract mismatch and corrected it in the frontend. Next step is to guide the user on running the services.

## Evaluation notes (flywheel)

- Failure modes observed: Initial mismatch in API field names (query/question, response/answer).
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
