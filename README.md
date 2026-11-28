# Harvard CS50x

中文 · [English](./README.en.md)

从零开始学习哈佛 [CS50x](https://cs50.harvard.edu/x/)，系统补齐计算思维、C 与内存管理、数据结构、Python、SQL 与 Web 基础。学习笔记整理在 [CS Five](https://csfive.netlify.app/)（[csfive/home](https://github.com/csfive/home)），代码按周按需新建；之前的 2022 年学习记录归档在 [`2022`](https://github.com/csfive/CS50x/tree/2022) 分支。

## 进度

| 周 | 主题 | 作业 | 代码 | 状态 |
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

## 编译与检查

macOS 本地通过 Homebrew 链接 `libcs50` 编译，并配合 `style50` / `check50` 自检：

```bash
clang -Wall -Wextra -I/opt/homebrew/include -L/opt/homebrew/lib -lcs50 -lm hello.c -o hello
style50 hello.c
check50 cs50/problems/2026/x/me
```

## 资源

- [课程主页](https://cs50.harvard.edu/x/) · [CS50 Manual](https://manual.cs50.io/) · [C 风格指南](https://cs50.harvard.edu/x/style) · [旧版归档 (2022)](https://github.com/csfive/CS50x/tree/2022)

课程材料由 David J. Malan 讲授，遵循 [CC BY-NC-SA 4.0](https://cs50.harvard.edu/x/license/)；本仓库仅作个人自学记录。
