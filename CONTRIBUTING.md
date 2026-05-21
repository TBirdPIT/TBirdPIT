# Contributing

Thanks for contributing.

## Workflow

1. Create a feature branch from `main`.
2. Keep PRs focused and small when possible.
3. Add or update tests for behavior changes.
4. Run quality checks before opening a PR.

## Local quality gates

```bash
python -m pip install -r requirements-dev.txt
pre-commit run --all-files
pytest
```

## Style standards

- Use type hints for public functions.
- Add docstrings for non-trivial behavior.
- Prefer explicit error handling with clear messages.
- Keep logs structured and secret-safe.

## Commit message style

Use conventional prefixes when possible:

- `feat:` new functionality
- `fix:` bug fix
- `docs:` documentation only
- `chore:` maintenance tasks
