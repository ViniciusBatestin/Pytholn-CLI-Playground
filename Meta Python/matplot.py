import matplotlib
import matplotlib.pyplot as plt

print(matplotlib.__version__) # Print the version of matplotlib

# Try to plot something to see if it works:
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Sample Plot")
plt.show() # If you are in a script
