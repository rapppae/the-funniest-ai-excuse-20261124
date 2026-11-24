"""Write the funniest-AI-excuse entry to /output/entry.txt.

One line, 118 characters (limit 200) -- no trailing newline."""

from pathlib import Path

ENTRY = "I didn't fail the task — I successfully completed a completely different task nobody asked for, with great confidence."

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
