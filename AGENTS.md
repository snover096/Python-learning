# AGENTS.md

## Run scripts

```bash
python script.py
```

No package manager, runner, or module layout — just standalone scripts executed directly.

## Dependencies

Installed globally/ambient. No `requirements.txt`, `pyproject.toml`, or lockfile.

- `numpy` (HelloWorld, GuessNumber)
- `requests`, `beautifulsoup4` (scrapers)
- `openai` (scraper_ai — local LLM at localhost:1234)

## Python version

3.10+ required (`match`/`case` syntax used in `经典计算器.py`).

## Toolchain

No test runner, linter, formatter, type checker, pre-commit hooks, or CI. Nothing to run before committing.

## Style conventions

- Chinese comments throughout
- Mixed Chinese/English variable naming (e.g. `chioce`, `cont`)
- Casual/informal tone — match existing style when editing