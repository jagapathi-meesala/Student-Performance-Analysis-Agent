from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
subprocess.run([sys.executable, str(root / "verification" / "validate_manifest.py")], check=True)
subprocess.run([sys.executable, str(root / "verification" / "check_docs.py")], check=True)
print("local structural validation passed")
