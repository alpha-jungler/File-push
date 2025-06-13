
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Kirtan", "Lizen", "Ranjit", "Arbin", "Sabal", "Aryan", "Arohan", "Roshan"])
y = np.array([17, 16, 18, 15, 17, 18, 15, 19])

plt.bar(x, y, width=0.1, color='indigo')
plt.show()
