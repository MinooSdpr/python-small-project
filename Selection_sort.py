"""
Prompts the user to input a sequence of space-separated numbers, sorts them
using the selection sort algorithm, and visualizes each step using a bar chart.

The bar chart updates in real-time to show the progression of the sort.
"""
import matplotlib.pyplot as plt


numbers = input('Enter numbers and split it with space: ').split()
numbers = list(map(int, numbers))
n = len(numbers)

for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if numbers[j] < numbers[min_index]:
            min_index = j
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    # Visualize the current state of the list
    plt.bar(range(n), numbers, color='skyblue')
    plt.pause(0.5)
    plt.clf()

plt.bar(range(n), numbers, color='green')
plt.show()

print("Sorted numbers:", numbers)