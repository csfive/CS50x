# Harvard CS50x

[中文](./README.md) · English

Learning Harvard [CS50x](https://cs50.harvard.edu/x/) from scratch to internalize computational thinking, C and memory management, data structures, Python, SQL, and web fundamentals. Study notes live at [CS Five](https://csfive.netlify.app/) ([csfive/home](https://github.com/csfive/home)), and week directories are created as each module starts. The previous 2022 attempt is archived on the [`2022`](https://github.com/csfive/CS50x/tree/2022) branch.

## Progress

| Week | Topic | Pset | Code | Status |
| --- | --- | --- | --- | --- |
| 0 | [Scratch](https://cs50.harvard.edu/x/weeks/0/) | [Pset 0](https://cs50.harvard.edu/x/psets/0/) | — | ⏭️ |
| 1 | [C](https://cs50.harvard.edu/x/weeks/1/) | [Pset 1](https://cs50.harvard.edu/x/psets/1/) | [01-c](./01-c) | ✅ |
| 2 | [Arrays](https://cs50.harvard.edu/x/weeks/2/) | [Pset 2](https://cs50.harvard.edu/x/psets/2/) | [02-arrays](./02-arrays) | ✅ |
| 3 | [Algorithms](https://cs50.harvard.edu/x/weeks/3/) | [Pset 3](https://cs50.harvard.edu/x/psets/3/) | — | ⬜ |
| 4 | [Memory](https://cs50.harvard.edu/x/weeks/4/) | [Pset 4](https://cs50.harvard.edu/x/psets/4/) | — | ⬜ |
| 5 | [Data Structures](https://cs50.harvard.edu/x/weeks/5/) | [Pset 5](https://cs50.harvard.edu/x/psets/5/) | — | ⬜ |
| 6 | [Python](https://cs50.harvard.edu/x/weeks/6/) | [Pset 6](https://cs50.harvard.edu/x/psets/6/) | — | ⬜ |
| 7 | [SQL](https://cs50.harvard.edu/x/weeks/7/) | [Pset 7](https://cs50.harvard.edu/x/psets/7/) | — | ⬜ |
| 8 | [HTML, CSS, JavaScript](https://cs50.harvard.edu/x/weeks/8/) | [Pset 8](https://cs50.harvard.edu/x/psets/8/) | — | ⬜ |
| 9 | [Flask](https://cs50.harvard.edu/x/weeks/9/) | [Pset 9](https://cs50.harvard.edu/x/psets/9/) | — | ⬜ |
| 10 | [The End](https://cs50.harvard.edu/x/weeks/10/) | — | — | ⬜ |
| ✦ | [Final Project](https://cs50.harvard.edu/x/project/) | — | — | ⬜ |

## Build & Check

Local builds, runs, `style50` / `check50` checks, and submissions on macOS are handled by the root [`Makefile`](./Makefile) (linking Homebrew `libcs50`). Run `make` for help:

```bash
make r <name> [args...]   # Compile and run (e.g. make r caesar 13; use ARGS="-1" for flags)
make s <name>             # Run style50 style check
make c <name>             # Run check50 offline (-less/-more mapped automatically)
make c <name> UPDATE=1    # Refresh check50 checks online before testing
make sub <name>           # Submit to CS50 (submit50)
make clean                # Remove compiled binaries and .dSYM bundles for all .c files
```

## Resources

- [Course Home](https://cs50.harvard.edu/x/) · [CS50 Manual](https://manual.cs50.io/) · [C Style Guide](https://cs50.harvard.edu/x/style) · [Archived 2022 Branch](https://github.com/csfive/CS50x/tree/2022)

Course materials taught by David J. Malan ([CC BY-NC-SA 4.0](https://cs50.harvard.edu/x/license/)). This repository contains personal study code only.
