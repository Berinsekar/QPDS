import matplotlib.pyplot as plt

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Create horizontal bar chart
plt.barh(languages, popularity, color=['blue', 'green', 'red', 'purple', 'orange', 'cyan'])

# Add title and labels
plt.title('Popularity of Programming Languages')
plt.xlabel('Popularity')
plt.ylabel('Programming Languages')

# Display the plot
plt.show()
