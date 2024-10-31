import numpy as np
import matplotlib.pyplot as plt

fig= plt.figure(figsize=(10,6))
ax= fig.add_subplot(111,projection='3d')


x_list= np.arange(-5,5,0.01)
#np.arange(iniciar, detener, espacio entre los valores)
y_list= np.arange(-1,1,0.01)
X,Y=np.meshgrid(x_list,y_list)
#np.meshgrip es una tupla donde se organizan los valores en una matriz
z=-3*((X/10)**2-(Y/20)**2)

ax.plot_surface(X,Y,z, cmap='inferno',alpha=0.8)

ax.set_title('Ejemplo 2')
ax.set_xlabel('Eje x')

ax.set_ylabel('Eje y')

ax.set_zlabel('Eje z')


plt.show()