import subprocess
import sys


def test_manifest_validator():
    result = subprocess.run([sys.executable, "verification/validate_manifest.py"], capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr


def test_documentation_validator():
    result = subprocess.run([sys.executable, "verification/check_docs.py"], capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr
