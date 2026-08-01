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
- `openai`, `ollama` (scraper_ai — local LLM at `localhost:1234`; both are imported at module top, so the script won't import without either)
- `customtkinter` (NoteApp GUI)

## Python version

3.10+ required (`match`/`case` syntax used in `经典计算器.py`).

## Directory layout

| Path | Purpose |
|------|---------|
| `./` | Root misc scripts |
| `小玩意儿~/` | Small tools (calculator, guess number, password gen, file organizer) |
| `Scraper爬？/` | Web scrapers (Douban Top250, Google Search, basic, AI-powered) |
| `NoteApp/` | CustomTkinter GUI memo app (persists to `data.json`) |

## Runtime side effects

- `scraper_ai.py` writes `quotes.txt` to the CWD; `douban_top250.py` writes CSV/JSON output
- `NoteApp/app.py` persists to `data.json` next to the script (or beside the exe when frozen)
- These are runtime-generated — don't commit them or treat them as source files

## Toolchain

No test runner, linter, formatter, type checker, pre-commit hooks, or CI. Nothing to run before committing.

## Style conventions

- Chinese comments throughout
- Mixed Chinese/English variable naming (e.g. `chioce`, `cont`)
- Casual/informal tone — match existing style when editing
