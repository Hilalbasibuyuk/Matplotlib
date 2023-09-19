import matplotlib.pyplot as plt
import numpy as np

"""
x = [1,2,3,4]
y = [1,4,9,11]

plt.plot(x,color = "red",linewidth = "1") # x grafiğini gösterir. Color çizgi rengini , linewidth çizgi kalınlığını ayarlar
plt.plot(y) # y grafiğini gösterir

plt.plot(x,y, color = "purple",linewidth = "7") # birbirlerine karşılık gelen x y değerlerini gösterir

#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html sitesinden şekillere çizgilere bakarak yapabiliriz
plt.plot(x,y,"o--r")

plt.axis([0,6,0,20]) # X'te 0-6 aralığına Y'de 0-20 aralığına kadar gösterir

plt.title("İstatistiksel Veriler") # Grafiğin başlığı
plt.xlabel("X ekseni") # X ekseni ismi
plt.ylabel("Y ekseni") # Y ekseni ismi

"""
"""
x = np.linspace(0,2,100)

plt.plot(x,x,label = "linear")
plt.plot(x,x**2, label = "quadratic")
plt.plot(x,x**3,label = "cubic")

plt.xlabel("x label")
plt.ylabel("y label")

plt.legend() # linear ,quadratic,cubic yazılarına denk gelen çizgileri sol üst köşede gösterir
plt.title("Simple plot")
plt.show()

"""
"""
x = np.linspace(0,4,100)
fig,axs = plt.subplots(2)

axs[0].plot(x,x)
axs[0].set_title("linear")

axs[1].plot(x,x**2)
axs[1].set_title("quadratic")

plt.tight_layout() # Başlıkla üst üste gelmesin diye kullandık.
plt.show()

"""
"""
x = np.linspace(0,5,100)
fig,axs = plt.subplots(2,2)
fig.suptitle("My first grafic")

axs[0,0].plot(x,x,color = "red")
axs[0,1].plot(x,x**2, color = "pink")
axs[1,0].plot(x,x**3, color = "purple")
axs[1,1].plot(x,x**4,color = "orange")

plt.show()

"""
"""
import pandas as pd

data = pd.read_csv(r"C:\Users\hilal\OneDrive\Belgeler\python_projeleri\python_projeleri\Numpy-Pandas\Nba.csv")

data = data.head(5).drop(["age"],axis = 1).groupby("team_abbreviation").sum()
data.plot(subplots=True) #Ayrı grafikler halinde gösterir özelliklere göre
plt.legend()
plt.show()

"""