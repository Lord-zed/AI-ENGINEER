from pathlib import Path

workspace = Path("participant_pkg")
workspace.mkdir(exist_ok=True)
file_path = workspace / "file_ops.py"
file_path
f = open(file_path, "w", encoding="utf-8")
f.write("This is the first line in notes.txt\n")
f.close()