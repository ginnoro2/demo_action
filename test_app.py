
# test_app.py
"""Functional test that passes — even though code is insecure!"""

import subprocess

def test_app_runs():
    """Verify app.py executes without error."""
    result = subprocess.run(
        ["python", "app.py"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Public Key:" in result.stdout
