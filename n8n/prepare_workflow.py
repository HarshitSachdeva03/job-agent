"""
Reads GEMINI_API_KEY from the root .env and injects it into the n8n workflow
template, writing a ready-to-import file: "Job Application Agent.ready.json".
That file is gitignored — never commit it.

Usage (from repo root):
    python n8n/prepare_workflow.py
"""

import json
import os
from pathlib import Path

ROOT = Path(__file__).parent.parent
TEMPLATE = Path(__file__).parent / "Job Application Agent.json"
OUTPUT = Path(__file__).parent / "Job Application Agent.ready.json"


def load_env(path: Path) -> dict:
    env = {}
    if not path.exists():
        return env
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        env[key.strip()] = value.strip()
    return env


def main():
    env = load_env(ROOT / ".env")
    api_key = env.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise SystemExit("Error: GEMINI_API_KEY not found in .env or environment.")

    content = TEMPLATE.read_text(encoding="utf-8")
    content = content.replace("YOUR_GEMINI_API_KEY", api_key)

    OUTPUT.write_text(content, encoding="utf-8")
    print(f"Written: {OUTPUT.name}")
    print("Import this file into n8n — do not commit it.")


if __name__ == "__main__":
    main()
