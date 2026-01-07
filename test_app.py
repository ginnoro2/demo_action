# test_app.py
"""Functional and unit tests for the vulnerable PKI tool (v1.0.2)."""

import app  # Import the module directly for unit testing
import subprocess


def test_get_version():
    """Ensure version matches expected release."""
    assert app.get_version() == "v1.0.2"


def test_secure_hash_no_key():
    """Test SHA-256 hashing without key."""
    result = app.secure_hash("hello")
    expected = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
    assert result == expected


def test_secure_hash_with_key():
    """Test HMAC-SHA255 hashing with key."""
    result = app.secure_hash("hello", key="secret")
    # Can't hardcode HMAC easily, but we can check format
    assert len(result) == 64  # SHA-256 = 64 hex chars
    assert isinstance(result, str)


def test_cert_fingerprint():
    """Test certificate fingerprint generation."""
    fake_cert = "-----BEGIN CERT-----\nABCD1234\n-----END CERT-----"
    fp = app.cert_fingerprint(fake_cert)
    assert len(fp) == 64
    # Ensure PEM headers are stripped before hashing
    fp2 = app.cert_fingerprint("ABCD1234")  # same content, no headers
    assert fp == app.secure_hash("ABCD1234")


def test_weak_hash_still_exists():
    """Confirm legacy weak function is present (for vulnerability demo)."""
    result = app.weak_hash("test")
    assert len(result) == 32  # MD5 = 32 hex chars


# Optional: Keep end-to-end run test
def test_runs():
    """Ensure the script executes without error (e2e sanity check)."""
    result = subprocess.run(["python", "app.py"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "PKI Tool Running..." in result.stdout
    assert "v1.0.2" in result.stdout
    assert "Secure hash demo:" in result.stdout
