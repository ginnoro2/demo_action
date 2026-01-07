# Contributing Guidelines

Thank you for your interest in contributing!

This repository is used for **academic DevSecOps laboratories**, so contributions must follow specific rules.

---

## Allowed Contributions

- Documentation improvements
- CI/CD pipeline enhancements
- Additional security demonstrations
- Improved comments and explanations
- Docker hardening examples

---

## Not Allowed

- Removing intentional vulnerabilities
- Refactoring insecure code into secure-only code
- Adding real secrets or credentials
- Turning this into a production-ready PKI system

---

## Testing Requirements

All contributions must:
- Pass `pytest`
- Pass `pylint` (warnings allowed)
- Be scanned by `bandit`
- Build successfully via Docker

---

## Commit Message Format

```text
<type>: <short description>

Examples:
feat: add secure hashing example
docs: improve README explanation
ci: add container scanning step
