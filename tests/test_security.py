from pathlib import Path
import re


def test_no_env_file_and_no_common_secret_patterns():
    assert not Path(".env").exists()
    secret_patterns = [re.compile(r"sk-[A-Za-z0-9]{20,}"), re.compile(r"-----BEGIN [A-Z ]+PRIVATE KEY-----")]
    for path in Path(".").rglob("*"):
        if path.is_file() and ".git" not in path.parts:
            text = path.read_text(errors="ignore")
            for pattern in secret_patterns:
                assert not pattern.search(text), f"possible secret in {path}"
