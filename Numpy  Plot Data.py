from matplotlib import pyplot as plt
import numpy as np
a = np.array([56, 87, 54, 56, 39, 55, 54, 76, 98, 51, 75, 99, 98, 39, 34, 32, 87])
plt.hist(a, bins=[0, 20, 40, 60, 80, 100])
plt.title("Graff Manipulation")
plt.show()