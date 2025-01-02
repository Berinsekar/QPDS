import matplotlib.pyplot as plt

# Specify the correct path to the text file
filename = 'C:/Users/joinw/AppData/Local/Programs/Python/Python312/test.txt'
x_values = []
y_values = []

with open(filename, 'r') as file:
    for line in file:
        x, y = map(int, line.split())
        x_values.append(x)
        y_values.append(y)

# Plotting the line graph
plt.plot(x_values, y_values, marker='o', linestyle='-')

# Adding labels and title
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.title('Line Graph Title')

# Display the plot
plt.show()
