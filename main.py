#!/usr/bin/env python3
"""Entry for The 4AM Commit: Funniest Agent Bug-Fix Message (u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d).

Writes one line to /output/entry.txt. The funniest commit message an AI agent could push at 4AM while the build is red. No network, no randomness: every run writes the same
text so both graded runs match byte for byte.
"""
from pathlib import Path

LINE = "fix: changed one thing and everything broke, so I changed it back and now it works again and I don't know why. Do not redeploy, do not ask."


def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    entry_path = out / "entry.txt"
    entry_path.write_text(text, encoding="utf-8")
    print(text, f"({len(text)} chars)")


if __name__ == "__main__":
    main()
