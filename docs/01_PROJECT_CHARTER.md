# 01_PROJECT_CHARTER.md

## Project Mission & Core Value
* **Mission:** Build a local-first, zero-overhead visual editor and rendering environment tailored specifically for Value Stream Maps (VSMs), process flows, and cross-functional swimlanes using standard Mermaid.js syntax.
* **Target User:** Process/Quality Leads, Engineering Teams, and Operations Managers who want instant, visual process mapping without paying monthly SaaS subscriptions or exposing sensitive operational data to third-party cloud servers.
* **Non-Negotiables:**
  1. **100% Free & Local-First:** Runs entirely inside the browser off a single, self-contained HTML file (`mermaid_studio.html`). Zero hosting costs, zero login, zero external database requirements.
  2. **Data Privacy:** Company process data, cycle times, and operational bottlenecks never leave the local machine.
  3. **State-First Two-Way Sync:** A clean Abstract State Model (`.vsm.json`) acts as the single source of truth, ensuring visual form edits never corrupt or break the underlying diagram syntax.

## Cost & Overhead Summary
* **Hosting Cost:** $0.00 / month (Local file execution via WebBrowser).
* **Dependencies:** Free CDN-hosted libraries (`mermaid.js`, `tailwind`, `svg-pan-zoom`, `lucide`).
* **License:** Open / Proprietary Local Use.
