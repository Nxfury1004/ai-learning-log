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
- Chapter 4 (Working with Lists): done, exercises 4-1, 4-2, 4-3, 4-6, 4-8, 4-9,
  4-10, 4-11, 4-13 (4-4/4-5/4-7/4-12 skipped as repetitive; 4-14 is read-only; 4-15
  light PEP8 pass).
  - Loop variables in Python are NOT block-scoped -- `for x in list:` leaves `x`
    defined (holding its last value) even after the loop ends. This is *why*
    forgetting to indent a line doesn't always crash -- it just silently uses
    the loop's leftover value.
  - Huge one: list copying. `b = a` for a list does NOT copy it -- both names
    point at the same mutable object, so mutating via either name affects both.
    (Contrast with strings: reassigning never does this, because strings are
    immutable -- you can only replace them, never mutate them in place.)
    Correct copy: `b = a[:]` (full slice) or `a.copy()`.
  - range(a, b) and slicing [a:b] both exclude the end index -- same off-by-one
    convention throughout Python.
  - Tuples: immutable, can't reassign an item, but CAN reassign the whole
    variable to a new tuple.
- Status: in progress, starting Chapter 5 (if statements) next.
