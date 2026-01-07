
---

```markdown
# Release Notes

## v1.0.2
**Release Date:** December 2025

### Added
- Secure hashing using SHA-256 and HMAC-SHA256
- Version reporting via `get_version()`
- Improved Docker security (non-root execution)

### Intentionally Vulnerable (Educational)
- `eval()` for RCE demonstration
- `pickle.loads()` for unsafe deserialization
- Hardcoded secret for secret-scanning demos
- Weak cryptography using MD5

### CI/CD
- Automated linting (Pylint)
- Static security analysis (Bandit)
- Functional testing (Pytest)
- Docker image published to GHCR

---

## v1.0.1
- Initial secure hashing feature
- CI pipeline integration
- First GHCR container release
