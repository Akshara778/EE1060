import numpy as np
import matplotlib.pyplot as plt
import math

alpha1 = 0.5
k = np.arange(-50,51,5)

Ck = np.zeros_like(k,dtype = float)

for i,k[i] in enumerate(k):
   if k[i]!=0:
       Ck[i] =  np.abs((20/(np.pi*k[i]))*np.sin(np.pi*k[i]*alpha1))
   else:
       Ck[i] = 10

plt.stem(k,Ck)
plt.xlabel(" k ")
plt.ylabel(" |C_k| ")
plt.title("Magnitude Spectrum for Alpha = 0.5")
plt.show()


