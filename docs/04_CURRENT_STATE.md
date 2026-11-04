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

## Known Limitations
* Dragging, Library adds and Connect Nodes support flowcharts (state diagrams are draggable); sequence actors are not draggable.
* Deleting a subgraph is not supported, and deleting an edge does not reindex `linkStyle` lines.
* Earlier icon keys (`user`, `alert`, `box`, `check`, `clock`, `truck`, `db`, `gear`) were replaced and load as "No Process Icon".
* Large projects may exceed URL length limits for `?state=`; use file import instead.
