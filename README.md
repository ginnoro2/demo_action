# PKI Demo App – DevSecOps CI/CD Lab

A deliberately vulnerable Python PKI demonstration application used to teach **real-world DevSecOps practices** through hands-on CI/CD automation.

This repository accompanies **DevOps Laboratory 4 & 5**, where students learn how security, testing, containerization, and versioned delivery work together in modern DevSecOps pipelines.

 **Repository**: https://github.com/ginnoro2/demo_action/blob/main/

> **Security Warning**  
> This application contains **intentional vulnerabilities** (e.g., `eval()`, `pickle`, hardcoded secrets, weak cryptography).  
> It is strictly for **educational and laboratory use only**.  
> **Do NOT deploy this code in production environments.**

---

## Learning Outcomes

By working with this repository, students will learn how to:

- Integrate **static application security testing (SAST)** into CI pipelines
- Understand why **passing tests ≠ secure code**
- Build and publish **secure Docker images**
- Use **GitHub Actions** for CI/CD automation
- Apply **versioned, immutable artifact delivery**
- Pull, run, and verify containers from **GitHub Container Registry (GHCR)**

---

## Repository Structure

```text
.
├── app.py                  # Vulnerable PKI demo application
├── test_app.py             # Functional test (intentionally minimal)
├── Dockerfile              # Secure container build configuration
├── .github/
│   └── workflows/
│       └── ci.yml          # DevSecOps CI/CD pipeline
└── README.md

```
## Run Locally 
```bash
# Clone the repository
git clone https://github.com/ginnoro2/demo_action.git
cd demo_action

# install dependencies
pip install -r requirement.txt

# Run the application
python app.py
```

## Pull and Run from GHCR
```bash
# Pull the latest image
docker pull ghcr.io/ginnoro2/demo_action/pki-app:latest

# Run the container
docker run ghcr.io/ginnoro2/demo_action/pki-app:latest
docker run ghcr.io/ginnoro2/demo_action/pki-app:v1.0.1
```

## Docker Volumes 
```text
# teet.py
import os

DATA_DIR = "/app/data"

# Ensure directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Write a file to the volume
with open(os.path.join(DATA_DIR, "output.txt"), "w") as f:
    f.write("This is saved in the mydata volume!\n")

print("Data written to volume.")
```
## Inspect Volume content
```bash
docker run -it --rm -v mydata:/app/data ubuntu:latest ls -la /app/data
```

