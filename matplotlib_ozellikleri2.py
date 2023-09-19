import matplotlib.pyplot as plt
import numpy as np

"""
x = np.linspace(-10,9,100)
y = x**3
z = x**2

figure = plt.figure()

axes_cube = figure.add_axes([0.1,0.1,0.8,0.8]) # [0.1, 0.1, 0.9, 0.9] değerleri, eksenin sol alt köşesini %10 sola ve %10 yukarı kaydırırken,
                                          # genişliği ve yüksekliği çizim alanının %80'ine kadar alır.

axes_cube.plot(x,y,"b")
axes_cube.set_xlabel("X ekseni")
axes_cube.set_ylabel("Y ekseni")
axes_cube.set_title("Cube")

axes_square = figure.add_axes([0.6,0.2,0.25,0.25])

axes_square.plot(x,z,"r")
axes_square.set_xlabel("X ekseni")
axes_square.set_ylabel("Y ekseni")
axes_square.set_title("Square")

"""
"""
x = np.linspace(-10,9,100)
y = x**3
z = x**2

figure = plt.figure()
axes = figure.add_axes([0,0,1,1])
axes.plot(x,y,label ="Cube")
axes.plot(x,z,label ="Square")
axes.legend(loc = 1) # Sağ altta çizgilerin label'ını gösterir.Loc 1 ise sağ üst vs.

"""
"""
x = np.linspace(-10,9,100)
y = x**3
z = x**2

fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(4,4)) # figsize grafiğin boyutunu belirler. nrows 2 satır, ncols 1 sütun olsun diyor.
axes[0].plot(x,y)
axes[0].set_title("Cube")

axes[1].plot(x,z)
axes[1].set_title("Square")

plt.tight_layout() 
fig.savefig("firstfigure.png") # png olarak kaydettik. Bunu pdf olarak da yapabiliriz.(sonuna ".pdf" yazarak)

"""
plt.show()