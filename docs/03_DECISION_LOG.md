# 03_DECISION_LOG.md

| Date | Architectural Decision | Rationale / Trade-Off | Status |
|---|---|---|---|
| **2026-11-03** | Selected Single-File HTML/JS Architecture | Avoided Node/npm build steps so the tool can be double-clicked open directly off disk or emailed across PCs without server configuration. | **Confirmed** |
| **2026-11-03** | State-First Architecture over Direct Text Regex | Regex replacements on raw Mermaid text proved fragile for complex/nested subgraphs. Using `projectState` JSON as the source of truth prevents syntax corruption. | **Confirmed** |
| **2026-11-03** | File-Based AI Handoff (`.vsm.json`) | Selected drag-and-drop JSON state files over WebSocket servers to keep local machine requirements at 0 background processes and 100% portable. | **Confirmed** |
| **2026-11-03** | Event Delegation on Parent Canvas | Bound selection handlers to `#mermaidRender` rather than individual `.node` elements to prevent DOM memory leaks on large 50+ node VSMs. | **Confirmed** |
