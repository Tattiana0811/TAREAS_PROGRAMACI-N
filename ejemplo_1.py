import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10*np.pi,10*np.pi,1000)
#np,linspace (donde inicia, donde termina, cantidad de veces generado )
y=np.sinc(x)

fig,ax=plt.subplots()

ax.plot(x,y,linestyle='-',linewidth=2, label= 'ejemplo1', color='b')

ax.set_title('Ejemplo 1')
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')

plt.show()

