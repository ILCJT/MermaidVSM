# 04_CURRENT_STATE.md & EXECUTION ROADMAP

## Current Milestone Status
* [x] **Phase 1 (PoC):** Standalone HTML viewer with live Monaco/Textarea code editing, error boundary checks, and SVG pan/zoom.
* [x] **Phase 2 (Mobile & Layout Fixes):** Fixed header wrapping, mobile tab switcher, PNG/SVG exporters, and multi-event auto-render listeners.
* [x] **Phase 3 (State Engine & Drag-and-Drop Import):** Add file dropzone and `.vsm.json` project state parser/exporter.
* [x] **Phase 4 (Click-to-Inspect Drawer):** Add sliding node property drawer for visual form editing (C/T, C/O, WIP, Owner).
* [x] **Phase 5 (VSM Metrics Engine):** Auto-calculated lead time, value-add time, WIP, friction count and efficiency ladder footer.
* [x] **Phase 6 (Gemini VSM Skill):** `docs/VSM_BUILDER_SKILL.md` documents the `.vsm.json` generation schema.
* [x] **Phase 7 (Interactive Canvas HUD):** Canvas-first floating layout, node dragging with elastic Bezier routing and gooey anchors, Object Library (add / connect / delete), dual-tab Node/Edge inspector, shape selector, top-rim VSM process icon badges (`data-icon`), bottom metric sub-pills, friction class sync across templates, and `?state=` Base64 URL hydration.
* [x] **Mobile Responsive HUDs:** Under 768px the editor starts collapsed and the inspector docks as a bottom sheet; inspector controls are at least 44px tall; bottom panels add `env(safe-area-inset-bottom)` (`viewport-fit=cover`).
* [x] **Export Hygiene:** after each render `pruneOrphanPositions()` removes offsets for nodes that no longer exist. SVG exports wrap every HTML label in `<switch>` with a plain SVG `<text>` fallback for viewers without `foreignObject` support.
* [x] **Roadmap Phase 1:** `+ Process Box`, `+ Decision Gate`, `+ Buffer/WIP` and `📝 Add Note` spawn at the centre of the visible canvas. `getCanvasCenterCoordinates()` maps the viewport centre through `getScreenCTM().inverse()` (pan/zoom-aware); the result is stored as a `projectState.positions` offset (or a note offset), after waiting one frame because svg-pan-zoom applies the restored view on the next frame. The Save menu also has **Export Mermaid Code (.txt)** (`exportMermaidText()`, from `projectState.mermaid`, with the same picker/download fallback). Checked at 0.7x to 1.8x zoom with a changed pan: new nodes and notes land within 1.2px of the centre.
* [x] **Inspector Sizing:** the inspector is `clamp(280px, 85vw, 360px)` wide at every size (right-anchored, bottom-docked on phones), has a −/+ minimize button beside Close (it hides the body visually but keeps a focused input focused, and a new selection re-expands it), and uses tighter padding/gaps below 800px wide or 700px tall. Checked at 640, 768, 960 and 1440px wide: the canvas stays visible left of the drawer.
* [x] **HUD Layout:** the code editor starts collapsed (header bar only; click the header or chevron to toggle) and the Object Library has a −/+ toggle, `max-height: calc(100vh - 320px)` and its own scroll. A `--ladder-h` CSS variable, synced by a `ResizeObserver` on the summary bar, keeps the editor, zoom controls and inspector above it. On phones the zoom controls move to the top-right and the inspector, editor and library never open together. No overlap between floating panels at 1920x1080, 2560x1440, 1366x768, 1280x640 or 390x844.
* [x] **Process Notes:** yellow cards attached to nodes via `projectState.notes`; see the architecture spec. Notes are saved in `.vsm.json`/`?state=`, follow their node when it is dragged, and are included in SVG/PNG exports.
 one "Save Image" menu (PNG / SVG, then the `.vsm.json` project file). `pickSaveHandle()` uses `showSaveFilePicker` when available; cancelling aborts, any other failure or missing API falls back to an `<a download>`. After a template, file or URL load, `pruneOrphanMetrics()` drops metrics for node IDs not in the rendered diagram (not on ordinary typing edits). "Copy Code" uses `navigator.clipboard` with an `execCommand` fallback.

## Known Limitations
* Process Notes work on flowchart and state diagrams only (they need a draggable node to attach to) and use a dark yellow palette only; there is no light-mode variant because the app is dark-only.
* Dragging, Library adds and Connect Nodes support flowcharts (state diagrams are draggable); sequence actors are not draggable.
* Deleting a subgraph is not supported, and deleting an edge does not reindex `linkStyle` lines.
* Earlier icon keys (`user`, `alert`, `box`, `check`, `clock`, `truck`, `db`, `gear`) were replaced and load as "No Process Icon".
* Large projects may exceed URL length limits for `?state=`; use file import instead.
