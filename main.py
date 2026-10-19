"""DSA Algorithms Toolkit - beginner-friendly command-line project.
Demonstrates searching, sorting, and basic data-structure operations.
"""
from typing import List

def linear_search(arr: List[int], target: int) -> int:
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

def binary_search(arr: List[int], target: int) -> int:
    """Binary search requires arr to be sorted."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def bubble_sort(arr: List[int]) -> List[int]:
    result = arr[:]
    n = len(result)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result

def selection_sort(arr: List[int]) -> List[int]:
    result = arr[:]
    for i in range(len(result)):
        min_idx = i
        for j in range(i + 1, len(result)):
            if result[j] < result[min_idx]:
                min_idx = j
        result[i], result[min_idx] = result[min_idx], result[i]
    return result

def insertion_sort(arr: List[int]) -> List[int]:
    result = arr[:]
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result

def is_balanced_brackets(text: str) -> bool:
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack

def unique_values(arr: List[int]) -> List[int]:
    seen = set()
    output = []
    for value in arr:
        if value not in seen:
            seen.add(value)
            output.append(value)
    return output

def read_numbers() -> List[int]:
    raw = input("Enter integers separated by spaces: ").strip()
    if not raw:
        return []
    try:
        return [int(item) for item in raw.split()]
    except ValueError:
        print("Please enter integers only.")
        return []

def main():
    while True:
        print("\n" + "=" * 44)
        print("          DSA ALGORITHMS TOOLKIT")
        print("=" * 44)
        print("1. Linear Search")
        print("2. Binary Search (sorts input first)")
        print("3. Bubble Sort")
        print("4. Selection Sort")
        print("5. Insertion Sort")
        print("6. Check Balanced Brackets (Stack)")
        print("7. Remove Duplicate Values")
        print("8. Exit")
        choice = input("Choose an option (1-8): ").strip()

        if choice == "8":
            print("Thanks for using DSA Algorithms Toolkit!")
            break
        if choice == "6":
            expression = input("Enter brackets/text, e.g. {[()]}: ")
            print("Balanced" if is_balanced_brackets(expression) else "Not balanced")
            continue
        if choice not in {"1", "2", "3", "4", "5", "7"}:
            print("Invalid option. Choose 1-8.")
            continue

        numbers = read_numbers()
        if choice == "1":
            target = int(input("Number to search for: "))
            index = linear_search(numbers, target)
            print(f"Found at index {index}" if index != -1 else "Not found")
        elif choice == "2":
            sorted_numbers = sorted(numbers)
            target = int(input("Number to search for: "))
            index = binary_search(sorted_numbers, target)
            print("Sorted list:", sorted_numbers)
            print(f"Found at index {index} in the sorted list" if index != -1 else "Not found")
        elif choice == "3":
            print("Sorted:", bubble_sort(numbers))
        elif choice == "4":
            print("Sorted:", selection_sort(numbers))
        elif choice == "5":
            print("Sorted:", insertion_sort(numbers))
        elif choice == "7":
            print("Unique values:", unique_values(numbers))

if __name__ == "__main__":
    main()
