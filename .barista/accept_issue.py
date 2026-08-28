from pathlib import Path
import sys

number = int(sys.argv[1])
uri = sys.argv[2]
path = Path("issues") / f"issue-{number}.md"
text = path.read_text(encoding="utf-8")
assert text.startswith(f"# Issue {number}: ")
assert f"Source: {uri}\n" in text
assert "\n## Objective\n\n" in text
