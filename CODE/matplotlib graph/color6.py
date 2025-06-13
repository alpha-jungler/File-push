import matplotlib.pyplot as plt
import numpy as np
Xpoint=np.array([0, 250])
Ypoint=np.array([0, 350])
Zpoint=np.array([0, 200])
plt.plot(Xpoint, Ypoint, Zpoint, marker='x', color='orange', linestyle='dashed')
plt.title("ABC")
plt.xlabel("high")
plt.ylabel("low")
plt.grid(axis='y')
plt.show()