# Mermaid Studio (MermaidVSM)

## Overview

Mermaid Studio is an interactive, single-file HTML / ES6 / Tailwind CSS workspace for Value Stream Mapping and process diagrams. It renders Mermaid.js diagrams on a full-screen canvas with floating HUD panels for editing, inspecting and measuring a process. Everything runs in the browser, with no build step, no login and no backend. Process data never leaves your machine.

**Live URL:** <https://ilcjt.github.io/MermaidVSM/src/mermaid_studio.html>

## Features

- **Dynamic SVG drag-and-drop:** drag flowchart and state-diagram nodes on the canvas. Offsets are saved per node in `metrics[id].pos` and re-applied after every render.
- **Gooey Bezier line routing:** connected edges are redrawn as cubic Bezier curves while you drag, and `#gooey-anchor` SVG-filtered anchor sockets appear on the dragged node.
- **Dual-tab Node / Edge inspector:** a floating drawer for node title, shape, icon, owner, C/T, C/O, WIP and friction, and for connector label, line style and arrowhead. Edits write back into the Mermaid code live.
- **Top-rim Lean process icon badges:** non-redundant VSM symbols (dedicated/shared process, workcell, supplier, customer, kaizen burst, milk run, supermarket, go-see) float on the node's top border.
- **Bottom metric sub-pills:** Owner 👤, Cycle Time ⏱️, Changeover 🔄 and WIP 📦 render under the node title.
- **VSM summary ladder:** VA time, lead time, total WIP, friction points and efficiency update live.
- **Object Library:** add Process, Decision and Buffer/WIP nodes, connect nodes visually, and delete the selected node or edge.
- **Templates:** Value Stream Map, Standard Process Flow, Swimlanes, Sequence, State Machine and Root Cause Tree.
- **Base64 URL parameter state hydration:** open a project from a link with `?state=<base64 of a .vsm.json>` (see below).
- **Import / export:** drag-and-drop `.vsm.json` project files, plus SVG and PNG export.

## Setup / Local Running

No installation is needed. Open `src/mermaid_studio.html` in a browser, or serve it locally:

```powershell
python -m http.server 8080 --directory "src"
```

Then browse to <http://localhost:8080/mermaid_studio.html>. The page loads Mermaid, svg-pan-zoom, Tailwind and Lucide from CDNs, so it needs internet access.

## Opening a project from a URL

Append `?state=` followed by the Base64 (or Base64url) encoding of a UTF-8 `.vsm.json` document. A `#state=...` hash is accepted too. The JSON must contain a `mermaid` string.

```powershell
$b = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes((Get-Content project.vsm.json -Raw)))
"https://ilcjt.github.io/MermaidVSM/src/mermaid_studio.html?state=$b"
```

Browsers and servers limit URL length, so this suits small to medium projects. Use the Open button for large files.

## Mobile

Below 768px the code editor starts collapsed (reopen with its chevron), the inspector docks as a bottom sheet, inspector controls have 44px touch targets, and floating bottom panels respect `env(safe-area-inset-bottom)` (`viewport-fit=cover`). Reload after resizing across the breakpoint to reset the editor state.

## Documentation

See [`docs/`](docs): project charter, architecture spec, decision log, current state and the `.vsm.json` builder skill.
