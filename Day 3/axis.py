import matplotlib.pyplot as plt

# Line 1 data
x1 = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]

# Line 2 data
x2 = [1, 2, 3, 4, 5]
y2 = [1, 4, 6, 8, 10]

# Plotting the lines
plt.plot(x1, y1, label='Line 1', color='blue', linewidth=2)
plt.plot(x2, y2, label='Line 2', color='green', linewidth=4)

# Adding title and labels
plt.title('Two Lines with Different Widths and Colors')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Adding legend
plt.legend()

# Displaying the plot
plt.show()
