# import matplotlib.pyplot as plt
# import numpy as np
# Xpoint=np.array([0, 250])
# Ypoint=np.array([0, 350])
# Zpoint=np.array([0, 200])
# plt.plot(Xpoint, Ypoint, Zpoint, marker='x', color='b', linestyle='dotted')
# plt.title("MNO")
# plt.xlabel("low")
# plt.ylabel("high")
# plt.grid(axis='y')
# plt.show()
import matplotlib.pyplot as plt
import numpy as np
Xpoint=np.array([0, 25.6, 18.4, 36.3])
Ypoint=np.array([3.5, 21.5, 28.7, 34.5])
plt.title('ABC')
plt.xlabel('MNO')
plt.ylabel('XYZ')
plt.grid()
plt.plot(Xpoint, Ypoint, marker='o', color='violet', linestyle='dashed')
plt.show()