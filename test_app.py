
# test_app.py
"""Functional test that passes — even though code is insecure!"""

import subprocess
def test_runs():
    result = subprocess.run(["python", "app.py"], capture_output=True)
    assert result.returncode == 0
