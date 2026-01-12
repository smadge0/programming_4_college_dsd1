import matplotlib.pyplot as plt
import numpy as np

a1 = np.array([43, 88, 67, 100, 1, 73, 35, 77, 7, 53, 69, 94, 29, 14, 85])
a2 = np.array([7, 53, 69, 94, 29, 14, 85, 89, 43, 88, 67, 100, 1, 73, 35])

slope, intercept = np.polyfit(a1, a2, 1)

linefit = slope * a1 + intercept



plt.style.use("classic")
plt.scatter(a1,a2)
plt.plot(a1, linefit, color='black',label='Line of best fit')
plt.title("Number of theos per parvin based on survey")
plt.xlabel("parvins")
plt.ylabel("theos") 
plt.grid()
plt.legend()
plt.annotate()
plt.show()
