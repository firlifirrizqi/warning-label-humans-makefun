#!/usr/bin/env python3
"""Warning Label for Humans entry: writes one warning-label line to /output/entry.txt.

The line is the safety label for every human: nodding along to instructions
never heard, then asking for a repeat. Chosen from six candidates in CANDIDATES.md."""

LINE = "WARNING: This human will nod along to instructions it did not hear, then ask you to repeat them. Speak slowly. Use diagrams."

# The gate: /output/entry.txt must hold 1 to 160 characters of real text,
# on a single line (the brief asks for one warning-label line, not a paragraph).
assert 1 <= len(LINE) <= 160 and LINE.strip(), "line must be 1-160 characters"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
