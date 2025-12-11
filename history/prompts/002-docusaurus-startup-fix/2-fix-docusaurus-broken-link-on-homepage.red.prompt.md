---
id: 2
title: Fix Docusaurus Broken Link on Homepage
stage: red
date: 2025-12-11
surface: agent
model: gemini-1.5-flash
feature: docusaurus-startup-fix
branch: main
user: batool1
command: run build command
labels: ["docusaurus", "broken-link", "fix"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - physical-ai-book/docusaurus.config.js
  - physical-ai-book/src/pages/index.js
tests:

---

## Prompt

run build command

## Response snapshot

[SUCCESS] Generated static files in "build".

## Outcome

- ✅ Impact: Broken link on the Docusaurus homepage (`/`) pointing to `/docs/intro` was corrected to `/intro`, resolving build failures caused by `onBrokenLinks: 'throw'`. The `onBrokenLinks` setting was reverted to `throw` after the fix.
- 🧪 Tests: The fix was verified by successfully running the Docusaurus build command without any broken link warnings.
- 📁 Files: `physical-ai-book/docusaurus.config.js` and `physical-ai-book/src/pages/index.js` were modified.
- 🔁 Next prompts: None, the build command now runs successfully.
- 🧠 Reflection: The agent successfully identified the cause of the build failure (a broken link) by temporarily changing `onBrokenLinks` to `warn`, located the broken link in the homepage's `index.js`, and corrected it. The configuration was then reverted to its original stricter setting.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
