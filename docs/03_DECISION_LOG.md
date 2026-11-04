# 03_DECISION_LOG.md

| Date | Architectural Decision | Rationale / Trade-Off | Status |
|---|---|---|---|
| **2026-11-03** | Selected Single-File HTML/JS Architecture | Avoided Node/npm build steps so the tool can be double-clicked open directly off disk or emailed across PCs without server configuration. | **Confirmed** |
| **2026-11-03** | State-First Architecture over Direct Text Regex | Regex replacements on raw Mermaid text proved fragile for complex/nested subgraphs. Using `projectState` JSON as the source of truth prevents syntax corruption. | **Confirmed** |
| **2026-11-03** | File-Based AI Handoff (`.vsm.json`) | Selected drag-and-drop JSON state files over WebSocket servers to keep local machine requirements at 0 background processes and 100% portable. | **Confirmed** |
| **2026-11-03** | Event Delegation on Parent Canvas | Bound selection handlers to `#mermaidRender` rather than individual `.node` elements to prevent DOM memory leaks on large 50+ node VSMs. | **Confirmed** |
| **2026-11-03** | Canvas-First Floating HUD Layout | Replaced the dual-pane split with a full-bleed canvas and floating editor, library and inspector cards so the diagram gets the whole screen. | **Confirmed** |
| **2026-11-03** | Mermaid Code Stays the Source of Truth for Nodes | Shape, icon and title are parsed from and written back to a single atomic `ID + brackets + label` token, avoiding drift between `projectState` and the diagram. | **Confirmed** |
| **2026-11-04** | Drag Offsets Moved to `projectState.positions[id]` | Keeps layout separate from process metrics. Legacy `metrics[id].pos` is migrated on load by `normalizePositions()`. Canvas uses `touch-action: pan-x pan-y`; only node shapes use `touch-action: none` so touch drags are not cancelled by the browser. | **Confirmed** |
| **2026-11-03** | Drag Offsets Stored as Deltas (now in `projectState.positions`, see above) | Mermaid re-layouts on every render, so positions are saved as offsets from the layout position and re-applied. Sequence actors are not draggable (attribute-positioned lifelines). | **Confirmed** |
| **2026-11-03** | Non-Redundant VSM Icon Map | Process icons (🏭 🔀 🧩 👑 💥 🚚 🏬 🔍) never reuse the metric emojis (👤 ⏱️ 🔄 📦), so badge and metric sub-pill stay distinguishable. | **Confirmed** |
| **2026-11-03** | `data-icon` Attribute Persistence | Two icons share 🏭, so the badge span stores `data-icon='<key>'`; emoji matching is only a fallback. | **Confirmed** |
| **2026-11-03** | Base64 `?state=` URL Hydration | Lets a project open from a shareable link with no server. Trade-off: URL length limits, so large projects use file import. | **Confirmed** |
