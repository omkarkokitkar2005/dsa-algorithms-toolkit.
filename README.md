# DSA Algorithms Toolkit (Python)

A beginner-friendly Data Structures and Algorithms mini project. It provides a menu-driven program to practise searching, sorting, stack operations, and duplicate removal.

## Features
- Linear Search
- Binary Search (sorts input before searching)
- Bubble Sort
- Selection Sort
- Insertion Sort
- Balanced Brackets using a Stack
- Remove duplicate values while preserving their original order

## Requirements
- Python 3.9 or newer
- No external packages required

## Run the project
1. Download or clone this repository.
2. Open a terminal in this folder.
3. Run:

```bash
python main.py
```

On some computers, use `python3 main.py`.

## Example
Choose `3` for Bubble Sort and enter:

```text
Enter integers separated by spaces: 8 3 5 1
Sorted: [1, 3, 5, 8]
```

For balanced brackets, choose option `6` and enter `{[()]}`. The program prints `Balanced`.

## Complexity overview
| Algorithm / operation | Average time | Extra space |
|---|---:|---:|
| Linear Search | O(n) | O(1) |
| Binary Search | O(log n) | O(1) |
| Bubble Sort | O(n²) | O(1) |
| Selection Sort | O(n²) | O(1) |
| Insertion Sort | O(n²) | O(1) |
| Balanced Brackets (Stack) | O(n) | O(n) |
| Remove Duplicates (set) | O(n) average | O(n) |

Binary Search only works on sorted data. The program sorts the input first for that menu option, so total time includes sorting.

## Project structure
- `main.py` — all algorithms and menu
- `README.md` — project overview and instructions
- `DSA_Project_Report.pdf` — project report
- `LICENSE` — MIT license

## Future improvements
- Add linked lists, queues, trees, graphs, and hash tables
- Visualize algorithms step-by-step
- Add automated unit tests
- Add a graphical user interface

## License
MIT
