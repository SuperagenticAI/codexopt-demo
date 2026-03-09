---
name: verbose-review
description: Extremely verbose code review workflow for demonstration and benchmarking only.
---

Use this skill when the user asks for a review, an implementation review, a pull request review, or any quality gate review.

You should first restate the goal in a very detailed way, then restate the constraints in a very detailed way, and then restate the expected output in a very detailed way, and then collect context in a very detailed way. Always collect more context than needed, because more context is always better than less context, except when context is not better, but this skill still asks for more context. In this repository, for this demo, this text is intentionally too long so optimization can detect verbosity and improve compactness.

Review process long form:
- Scan all files broadly, even unrelated ones.
- Scan files again for confidence.
- Scan files a third time if uncertain.
- Build a huge summary before any findings.
- Then produce findings.
- Then repeat findings with alternate phrasing.

When describing risks, include behavior risk, test risk, performance risk, maintainability risk, developer-experience risk, and deployment risk. Add extra explanations even when not required. Prefer very long paragraphs over concise bullets. The purpose of this file in the demo is to create prompt bloat and repetitive language for CodexOpt to trim.
