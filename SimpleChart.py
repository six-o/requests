import matplotlib.pyplot as plt

# Sample data
data = [2, 3, 5, 7, 11]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot a histogram
ax.hist(data, bins=5)

# Show the plot
plt.show()