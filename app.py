# app.py
"""
Vulnerable PKI tool for security demo.
Version 1.0.1 – Added secure hashing feature.
"""

import pickle
import subprocess
import hashlib
import hmac
import os

PASSWORD = "12345"  # Hardcoded secret (intentional for demo)

def dangerous_eval(user_input):
    """Demonstrates RCE vulnerability (DO NOT USE)."""
    return eval(user_input)

def load_data(data):
    """Demonstrates insecure deserialization (DO NOT USE)."""
    return pickle.loads(data)

def clean_cache():
    """Demonstrates command injection risk."""
    subprocess.call("rm -rf /tmp", shell=True)

def weak_hash(data):
    """Broken crypto example."""
    return hashlib.md5(data.encode()).hexdigest()

# NEW FEATURE (v1.0.1)
def secure_hash(data, key=None):
    """
    Secure hashing using SHA-256 or HMAC-SHA256.
    """
    if key:
        return hmac.new(key.encode(), data.encode(), hashlib.sha256).hexdigest()
    return hashlib.sha256(data.encode()).hexdigest()

def get_version():
    return "v1.0.1"

if __name__ == "__main__":
    print("PKI Tool Running...")
    print("Version:", get_version())
    print("Secure hash demo:", secure_hash("test-data"))
