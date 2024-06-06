import matplotlib as plt
import numpy as np



# Step 2: Plot the first 5,000 cubic numbers
x_5000 = np.arange(1, 5001)
y_5000 = x_5000**3

plt.figure(figsize=(10, 5))
plt.plot(x_5000, y_5000, marker='o', markersize=1)
plt.title('First 5,000 Cubic Numbers')
plt.xlabel('Number')
plt.ylabel('Cube of Number')
plt.grid(True)
plt.show()

# Step 3: Apply a colormap to the cubes plot
# Create a colormap
cmap = plt.get_cmap('viridis')
norm = plt.Normalize(y_5000.min(), y_5000.max())

# Create a scatter plot with colormap
plt.figure(figsize=(10, 5))
scatter = plt.scatter(x_5000, y_5000, c=y_5000, cmap=cmap, norm=norm, s=1)
plt.title('First 5,000 Cubic Numbers with Colormap')
plt.xlabel('Number')
plt.ylabel('Cube of Number')
plt.colorbar(scatter, label='Cube Value')
plt.grid(True)
plt.show()
