import matplotlib.pyplot as plt
import numpy as np

# Sample data
means_men = [22, 30, 35, 35, 26]
means_women = [25, 32, 30, 35, 29]
groups = ['G1', 'G2', 'G3', 'G4', 'G5']

# X-axis positions for men and women
x = np.arange(len(groups))
width = 0.35  # Width of the bars

# Create bar plot
fig, ax = plt.subplots()
bars1 = ax.bar(x - width/2, means_men, width, label='Men', color='blue')
bars2 = ax.bar(x + width/2, means_women, width, label='Women', color='orange')

# Add title and labels
ax.set_title('Scores by Group and Gender')
ax.set_xlabel('Group')
ax.set_ylabel('Scores')
ax.set_xticks(x)
ax.set_xticklabels(groups)

# Add legend
ax.legend()

# Display the plot
plt.show()
