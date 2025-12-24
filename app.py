# app.py
"""Vulnerable PKI tool for security demo."""

import pickle
import subprocess
import hashlib

# 1. Hardcoded password (B105)
ADMIN_PASSWORD = "12345"

def unsafe_eval_key_gen(user_expr):
    # 2. eval() usage (B307)
    return eval(user_expr)

def load_user_profile(serialized_data):
    # 3. pickle.loads() (B403)
    return pickle.loads(serialized_data)

def unsafe_cleanup():
    # 4. Unsafe subprocess (B602)
    subprocess.call("rm -rf /tmp/cache", shell=True)

def weak_hash_key(data):
    # 5. Weak crypto: MD5 (B303)
    return hashlib.md5(data.encode()).hexdigest()

def main():
    print("Public Key: SAFE-ABC123")
    print("Private Key: [HIDDEN]")

if __name__ == "__main__":
    main()
