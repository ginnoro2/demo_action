# PKI Demo App – DevSecOps CI/CD Lab

A deliberately vulnerable Python PKI tool used to demonstrate **real-world DevSecOps practices** in a CI/CD pipeline. This repository accompanies **DevOps Laboratory 4**, where students:

- Run static analysis (Pylint, Bandit)
- Execute functional tests (Pytest)
- Build and publish a secure Docker image to **GitHub Container Registry (GHCR)**
- Learn why **passing tests ≠ secure code**

> **Warning**: This app contains **intentional vulnerabilities** (e.g., `eval()`, `pickle`, hardcoded secrets) for educational purposes only. **Do not use in production.**

---

## Features (v1.0.2)

- `secure_hash()`: SHA-256 / HMAC-SHA256 hashing (secure)
- `weak_hash()`: MD5 hashing (insecure – for demo)
- `dangerous_eval()`, `load_data()`: RCE & deserialization risks
- `cert_fingerprint()`: Simulated certificate fingerprinting
- Path traversal & insecure temp file examples

---

## Run Locally

```bash

# Clone the repo
git clone https://github.com/ginnoro2/demo_action.git
cd demo_action

# Run the app
python app.py
