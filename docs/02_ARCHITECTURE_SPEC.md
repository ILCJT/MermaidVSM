# 02_ARCHITECTURE_SPEC.md

## Tech Stack & Core Libraries
* **Frontend Runtime:** Vanilla HTML5 / ES6 JavaScript.
* **UI Styling:** Tailwind CSS (CDN).
* **Diagram Engine:** `mermaid.js` v10 (CDN).
* **Canvas Interactivity:** `svg-pan-zoom` v3.6 (CDN).
* **Icons:** Lucide Icons (CDN).

## Architectural Ownership Layers
- Layer A: System & File Entry (Single-file HTML DOM Shell, Drag-and-drop listener, Exporters)
- Layer B: State & AI Engine (In-Memory projectState JSON AST, Mermaid Serializer, Gemini VSM Skill Bridge)
- Layer C: UI/UX & Canvas (Dual-Pane Split Layout, Sliding Inspector Drawer, Event Delegation)
