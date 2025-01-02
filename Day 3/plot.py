import matplotlib.pyplot as plt

# Data for plots
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [2, 3, 5, 7, 11]
y3 = [2, 4, 6, 8, 10]
y4 = [1, 2, 3, 4, 5]

# Create a figure and subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Plot 1
axs[0, 0].plot(x, y1, label='y1', color='blue', linewidth=2)
axs[0, 0].set_title('Plot 1')
axs[0, 0].legend()

# Plot 2
axs[0, 1].plot(x, y2, label='y2', color='green', linewidth=2)
axs[0, 1].set_title('Plot 2')
axs[0, 1].legend()

# Plot 3
axs[1, 0].plot(x, y3, label='y3', color='red', linewidth=2)
axs[1, 0].set_title('Plot 3')
axs[1, 0].legend()

# Plot 4
axs[1, 1].plot(x, y4, label='y4', color='purple', linewidth=2)
axs[1, 1].set_title('Plot 4')
axs[1, 1].legend()

# Adding titles and labels
fig.suptitle('Multiple Plots Example')

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Display the plots
plt.show()
