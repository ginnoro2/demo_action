# Security Policy

## Reporting Vulnerabilities

This repository contains **intentional security vulnerabilities** for teaching purposes.

**Do NOT report the following as issues:**
- `eval()` usage
- `pickle.loads()`
- Hardcoded secrets
- Weak cryptographic functions

These are **deliberate** and required for DevSecOps demonstrations.

---

## What SHOULD Be Reported

If you discover:
- Accidental exposure of real credentials
- CI/CD misconfiguration
- Supply-chain risks
- Dependency vulnerabilities not intended for the lab

Please report responsibly.

---

## How to Report

- Open a **private issue** (if available), or
- Contact the repository maintainer via GitHub

---

## Supported Versions

| Version | Supported |
|-------|----------|
| v1.0.x | Yes |
| < v1.0 | No |

---

## Educational Disclaimer

This project is **not a production system**.  
All vulnerabilities exist to train students in **secure software delivery**.
