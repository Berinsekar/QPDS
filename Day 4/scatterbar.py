import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(0)  # For reproducibility
x = np.random.randn(100)
y = np.random.randn(100)

# Create scatter plot
plt.scatter(x, y, color='blue', alpha=0.5)

# Add title and labels
plt.title('Random Distribution Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Display the plot
plt.show()
