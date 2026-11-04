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
- Layer C: UI/UX & Canvas (Canvas-First Floating HUD: full-bleed SVG canvas, floating Code Editor, Object Library and Inspector panels, Event Delegation)

## Phase 7 Architecture

### Canvas interaction
* **Layout:** `#previewPanel` fills the window. The editor (bottom-left), Object Library (top-left) and Inspector (top-right) are floating cards.
* **Node dragging:** pointer events on `#mermaidRender`. Coordinates come from the node's parent `getScreenCTM().inverse()` so dragging stays correct when panned or zoomed. A drag starts after 4px of movement; svg-pan-zoom panning is disabled during the drag. Flowchart and state nodes are draggable; sequence actors are not.
* **Position persistence:** the offset from Mermaid's layout position is stored in `projectState.positions[id] = {x, y}` and re-applied after each render. Dragging uses Pointer Events: a capture-phase `pointerdown` on `#mermaidRender`, `setPointerCapture` once movement exceeds 4px (below that it is a tap), `getScreenCTM().inverse()` for deltas, a second finger cancels the drag, and node IDs come from `cleanNodeId()` (strips Mermaid's `flowchart-`/`state-` prefix and numeric suffix).
* **Elastic routing:** `updateNodeConnections(nodeId)` redraws connected edges (and their hit-paths and labels) as cubic Beziers anchored at the facing side midpoints of the node boxes. The `#gooey-anchor` SVG filter (blur + color matrix) is applied to anchor sockets only while dragging.
* **Object Library:** adds `NewNode`, `NewDec` and `NewWIP` definitions with unique ids, connects nodes (`toggleConnectMode`), and deletes the active node or edge (`deleteSelected`). Flowchart-only for adds and connects.

### Node label markup (single source of truth is the Mermaid code)
A flowchart node is written atomically as `ID + shape open + "label" + shape close` by `syncNodeToMermaid`, using `SHAPE_MAP`. The label is:

```html
<span class='relative inline-block px-1'><span class='absolute -top-3 left-1/2 -translate-x-1/2 text-xs leading-none z-10' data-icon='KEY'>EMOJI</span>Title</span><br/><span class='block text-[10px] opacity-80 font-mono leading-tight mt-1'>👤 Owner | ⏱️ 10m | 🔄 5m | 📦 20pcs</span>
```

* **Top-rim badge:** the process icon, positioned over the top border.
* **Bottom sub-pill:** metric values, shown only for non-zero values.
* `parseNodeDefinition` / `splitIconLabel` strip both parts so `#inspectorTitle` always holds the clean title.

### Icon map (non-redundant VSM symbols)
Process icons deliberately avoid the metric emojis (👤 ⏱️ 🔄 📦).

| Key | Icon | Meaning |
|---|---|---|
| `process_dedicated` | 🏭 | Dedicated process |
| `process_shared` | 🔀 | Shared process |
| `workcell` | 🧩 | Workcell |
| `supplier` | 🏭 | External supplier |
| `customer` | 👑 | Customer / recipient |
| `kaizen` | 💥 | Kaizen burst |
| `milk_run` | 🚚 | Milk run / transport |
| `supermarket` | 🏬 | Supermarket / storage |
| `inspection` | 🔍 | Go-See / quality inspection |

### `data-icon` persistence
`process_dedicated` and `supplier` share the 🏭 emoji, so the emoji alone cannot identify the icon. The badge span therefore carries a `data-icon='<key>'` attribute, and `splitIconLabel` reads it first. It falls back to matching the emoji (first matching key) for labels without the attribute. Icon keys from earlier versions (`user`, `gear`, ...) are no longer recognised and load as "No Process Icon".

### Friction highlighting
`class <id> friction;` lines (no semicolon in `stateDiagram-v2`) plus a single `classDef friction fill:#451a03,stroke:#f97316,stroke-width:2px,color:#ffedd5;`. The `classDef` is added when any node is flagged and removed when none are.

### URL state loader
`loadStateFromURL()` runs at the end of `DOMContentLoaded`. It reads `?state=` (or `#state=`), decodes Base64/Base64url as UTF-8 JSON, requires a non-empty `mermaid` string, then sets `projectState`, the editor, the diagram and the VSM summary exactly as `loadFile` does. Invalid values show a status-bar error and leave the empty workspace in place.
