import matplotlib.pyplot as plt
import numpy as np
Xpoint=np.array([5, 7, 8, 17, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
Ypoint=np.array([6, 9, 10, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63])
colors=np.array(["violet"])

plt.scatter(Xpoint, Ypoint, c=colors)
plt.show()


