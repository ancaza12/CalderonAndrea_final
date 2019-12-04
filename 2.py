import os
import numpy as np
import matplotlib.pyplot as plt
print("2 Ejercicio")
#https://github.com/ComputoCienciasUniandes/MetodosComputacionalesDatos/blob/master/hands_on/solar/monthrg.dat
import numpy as np

data = np.loadtxt('monthrg.dat')

def DFT(x):
    """
    Compute the discrete Fourier Transform of the 1D array x
    :param x: (array)
    """

    N = x.size
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    return np.dot(e, x)

plt.figure()
plt.scatter(data[3481:,0],data[3481:,4])
plt.plot(data[3481:,1],data[3481:,4])
plt.savefig("solar.png")
