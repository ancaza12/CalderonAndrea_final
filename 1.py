##https://github.com/ComputoCienciasUniandes/FISI2028-201920/blob/master/ejercicios/14/valores.txt
##Codigo tomado del repositorio de Jaime Forero
import numpy as np
import matplotlib.pyplot as plt

filein = open('valores.txt', "r")
texto = filein.readlines()
filein.close()

def proba_s(s, x):
    p = 1/(s*np.sqrt(2*np.pi))* np.exp(-(1*x**2)/(2*s**2))
    return p

def likelihood(x_data, n_points=100000):
    s = np.linspace(1E-2,4.0, n_points)
    l = np.ones(n_points)
    for x in x_data:
        l = l * proba_s(s, x)
    return s, l

def plot_likelihood(x_data):  
    s,l = likelihood(x_data)
    prome= np.mean(x_data)
    desvi= np.std(x_data)
    plt.plot(s, l/l.max())
    plt.xlabel(r'$s$')
    plt.ylabel(r'P($s$|x)')
    label = 'prom = {}'.format(prome), 'desv = {}'.format(desvi)
    plt.title(label)

plt.figure()
plt.ylim(0,1)
#plt.subplots_adjust(hspace=1)
#plt.subplots_adjust(wspace=1)
datos = np.array([2.031331588946557076, 5.886777538940683563, 2.195744759275823021, 6.821886748452244298, 8.793952398085184141e-01, 2.951577398416659559, 4.454332895499525158, -1.804396045394615955, -5.841925974092386120, -1.113495627653518838])
# _ = plt.hist(datos[:i+1], bins=40, density=True)
for i in range(len(datos)):
#     plt.subplot(5,2,i+1)
    _ = plt.hist(datos[:i+1], bins=40, density=True)
    print(datos[:i+1])
    plot_likelihood(datos[:i+1])
plt.savefig("sigma.png")
