import matplotlib.pyplot as plt
import numpy as np
Xpoint=np.array([0, 250, 180, 360])
Ypoint=np.array([1, 145, 280 , 345])
plt.subplot(2, 1, 1)
plt.plot(Xpoint, Ypoint)

Xpoint=np.array([0, 250, 180, 360])
Ypoint=np.array([1, 145, 280 , 345])
plt.subplot(2, 1, 2)
plt.plot(Xpoint, Ypoint)
plt.show()