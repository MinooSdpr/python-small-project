"""
Prompts the user to input a sequence of space-separated numbers, sorts them
using the bubble sort algorithm, and visualizes each step using a bar chart.

Visualization:
- Sky blue bars represent the current state of the list after each comparison.
- Real-time updates illustrate how elements bubble up to their correct position.
- The algorithm stops early if no swaps occur in a pass (optimized bubble sort).
"""

import matplotlib.pyplot as plt


numbers = input('Enter numbers and split it with space: ').split()
numbers = list(map(int, numbers))
n = len(numbers)

for i in range(n - 1):
    swapped = False
    for j in range(n - 1 - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swapped = True

        # Show current comparison step
        plt.bar(range(n), numbers, color='skyblue')
        plt.pause(0.2)
        plt.clf()

    if not swapped:
        break

plt.bar(range(n), numbers, color='green')
plt.show()
print("Sorted numbers:", numbers)