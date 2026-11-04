#!/usr/bin/env python3
"""Inline every CDN <script src> in src/mermaid_studio.html into one self-contained file.

Usage:  python scripts/build_bundle.py [--out dist/mermaid_studio.bundle.html] [--cache vendor]

Run it once on a machine with internet access; the output needs no network at runtime,
so it works inside sandboxed iframes and on air-gapped internal hosts. Downloaded
libraries are cached in --cache so rebuilds work offline.
"""
import argparse
import hashlib
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT_TAG = re.compile(r'<script src="(https://[^"]+)"></script>')


def fetch(url: str, cache: Path) -> str:
    cached = cache / (hashlib.sha1(url.encode()).hexdigest()[:12] + ".js")
    if cached.exists():
        return cached.read_text(encoding="utf-8")
    req = urllib.request.Request(url, headers={"User-Agent": "mermaid-studio-bundler"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        text = resp.read().decode("utf-8")
    cache.mkdir(parents=True, exist_ok=True)
    cached.write_text(text, encoding="utf-8")
    return text


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default=str(ROOT / "src" / "mermaid_studio.html"))
    ap.add_argument("--out", default=str(ROOT / "dist" / "mermaid_studio.bundle.html"))
    ap.add_argument("--cache", default=str(ROOT / "vendor"))
    args = ap.parse_args()

    html = Path(args.src).read_text(encoding="utf-8")
    cache = Path(args.cache)
    count = 0

    def inline(match: re.Match) -> str:
        nonlocal count
        url = match.group(1)
        print(f"inlining {url}")
        body = fetch(url, cache).replace("</script", "<\\/script")
        count += 1
        return f"<script>/* {url} */\n{body}\n</script>"

    bundled = SCRIPT_TAG.sub(inline, html)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(bundled, encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size / 1_000_000:.2f} MB, {count} scripts inlined)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
