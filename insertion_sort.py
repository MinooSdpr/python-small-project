"""
Prompts the user to enter space-separated numbers, then sorts them using
the insertion sort algorithm while visualizing each step with a bar chart.

Visualization:
- Sky blue bars show the list at each step of the sorting process.
- Green bars represent the fully sorted list at the end.
"""


import matplotlib.pyplot as plt

numbers = input('Enter numbers and split it with space: ').split()
numbers = list(map(int, numbers))
n = len(numbers)

for i in range(1, n):
    key = numbers[i]
    j = i - 1

    while j >= 0 and numbers[j] > key:
        numbers[j + 1] = numbers[j]
        j -= 1
    numbers[j + 1] = key
    plt.bar(range(n), numbers, color='skyblue')
    plt.pause(0.5)
    plt.clf()

plt.bar(range(n), numbers, color='green')
plt.show()

print("Sorted numbers:", numbers)