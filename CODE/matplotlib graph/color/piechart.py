import matplotlib.pyplot as plt
import numpy as np
y=np.array([35, 25, 15, 25])
mylabels=["Apple", "Mango", "Banana", "Orange"]
plt.pie(y, labels=mylabels)
plt.show()