from scipy.stats import norm
import numpy
from math import sqrt
from math import log
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy.optimize import curve_fit

x = [1.549,1.5348,1.5294,1.5212,1.5131,1.5049,1.4968,1.4914,1.4831,1.4750,1.4672]
y = [5,3.5,3.06,2.17,1.75,1.50,1.28,1.14,0.97,0.86,0.77]

print(len(x),len(y))

plt.scatter(x,y,s =13)
plt.title("")
#plt.xlim(0,2.9)
#plt.ylim(0,6)
plt.xlabel("Wire voltage (kV)")
plt.ylabel("Gas gain (signal amplitude) (V)")
plt.show()
