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
- Chapters 5-11 (if, dicts, input/while, functions, classes, files/exceptions/json,
  testing), covered 2026-09-27/28. Changed approach here: theory-first, since I
  already know C++. I skipped the book's basic exercises on purpose (5-1..5-11,
  most of 6-x through 11-x), so those are NOT done. Done: 6_synthesis_repos.py
  (dict aggregation, nested data, comprehensions). Scratch demos live in
  week-01/scratch_theory_*.py.
  - Ch5: `and`/`or` return an operand, not a bool; truthy/falsy values; chained
    comparisons (`1 < x < 10`); `==` compares value, `is` compares identity.
  - Ch6: dict = hash table (O(1) lookup, ~146x faster than list `in` at n=100k);
    keys must be hashable; `.keys()/.items()` are live views; mutating a dict
    while iterating raises RuntimeError; nested dict/list = JSON's data model.
  - Ch7: `input()` always returns str; `%` follows floor division (sign of the
    divisor), C++ truncates (sign of the dividend); no do-while.
  - Ch8: no overloading (a second `def` rebinds the name); args are passed by
    object reference; `*args`/`**kwargs`; default values are evaluated once at
    `def` time, so never use a mutable default (use None).
  - Ch9: `self` is an explicit parameter; no access control (`_x` convention,
    `__x` name mangling only avoids subclass collisions); instances are dicts;
    MRO via C3 linearization, `super()` = next class in the instance's MRO.
    Diagram: https://claude.ai/artifact/8qxBPdrbFZqSQ71n1LKWuD
  - Ch10: `with` = protocol-based cleanup (not RAII); gc.collect() only frees
    unreachable objects; EAFP over LBYL; `else` keeps `try` narrow; JSON round
    trips are lossy (tuple->list, int keys->str).
  - Ch11: `__name__ == '__main__'` guard; unittest makes a fresh TestCase per
    test; class-level `responses = []` is shared across instances (test caught it).
- Open items: Phase 1 milestone (a documented Python project on GitHub) is not
  done yet; book exercises for Ch5-11 skipped; try pytest.
- Status: Chapters 1-11 covered; Part II projects not started.
