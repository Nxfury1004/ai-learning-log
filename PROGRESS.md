# Progress Log

One entry per week: what I covered, what I built, what confused me.

---

## Week 0 — Setup (started 2026-09-27)
- Installed Python 3.12 and Git via winget.
- Set up repo structure, README, .gitignore, requirements.txt.
- Created `.venv`, installed JupyterLab into it.
- VS Code already installed and in use.
- Pushed repo to GitHub: github.com/Nxfury1004/ai-learning-log
- Status: done.

## Week 1 — Python Fundamentals I (started 2026-09-27)
- Chapter 2 (Variables & Simple Data Types): done, all exercises 2-1 through 2-11.
  - Key concept that clicked: variables are labels/pointers, not boxes — reassigning
    one variable never affects another that previously pointed at the same value.
  - String methods (.upper/.lower/.title/.strip family) always return a new string;
    they never mutate the original (strings are immutable).
- Chapter 3 (Introducing Lists): done, exercises 3-1 through 3-9 and 3-11 (3-10 skipped
  as redundant -- already exercised every list function across other exercises).
  - del vs pop(): del just deletes; pop() deletes AND returns the value so you can use it.
  - sort()/reverse() mutate the list permanently; sorted() returns a new sorted list
    and leaves the original untouched.
  - Learned for-loops and while-loops early/out of order (Ch. 4 and Ch. 7 material)
    because they were the natural tool for looping through a list -- introduced inline
    rather than skipped.
- Working style: pair-programming -- write/run code together in this session live,
  not just read-then-quiz.
- Status: in progress, starting Chapter 4 next.
