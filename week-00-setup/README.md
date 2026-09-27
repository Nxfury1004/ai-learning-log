# Week 0 — Setup & Orientation

No book needed this week. Goal: remove all environment friction before Phase 1 starts.

## Checklist
- [x] Install Python 3.12
- [x] Install Git
- [x] Install VS Code + the Python extension
- [x] Set up this repo (`ai-learning-log`) with a weekly folder structure
- [ ] Learn command-line basics: `cd`, `dir`/`ls`, creating/moving files, running a script
- [ ] Create a GitHub account (if you don't have one) and push this repo to it
- [x] Set up a virtual environment workflow (`.venv`): created, activated, packages installed
- [x] Install Jupyter (`pip install jupyterlab`) and confirm it runs
- [ ] (Optional) Install Anki — used starting Phase 3

## Notes
Python was already present via a Microsoft Store alias that doesn't actually work — the real
interpreter installed by winget lives at
`C:\Users\<you>\AppData\Local\Programs\Python\Python312\python.exe` and is reachable via the
`py` launcher command. Use `py` instead of `python` in this environment.

Virtual environment lives in `.venv/` at the repo root (gitignored). To use it:
```
.venv\Scripts\activate      # activate (PowerShell: .venv\Scripts\Activate.ps1)
pip install <package>
pip freeze > requirements.txt
```
Installed packages are pinned in `requirements.txt` at the repo root.

## Still to do
- Learn command-line basics (`cd`, `dir`, moving/creating files, running a script)
- Create a GitHub account and push this repo there
- (Optional) install Anki for Phase 3 onward
