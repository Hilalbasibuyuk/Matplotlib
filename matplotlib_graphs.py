import matplotlib.pyplot as plt
"""
# Stack plot
yil = [2010,2011,2012,2013,2014]

oyuncu1 = [8,3,6,11,4]
oyuncu2 = [9,2,5,12,13]
oyuncu3 = [2,6,1,7,9]

plt.plot([],[],color = "y", label = "oyuncu1")
plt.plot([],[],color = "b", label = "oyuncu2")
plt.plot([],[],color = "r", label = "oyuncu3")

plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3, colors=["y","b","r"])
plt.title("Yıllara göre atılan goller")
plt.xlabel("Yıl")
plt.ylabel("Gol sayısı")
plt.legend(loc = 2)
plt.show()
"""
"""
# Pasta dilimi şeklinde grafik (Pie grafiği)

goal_types = 'Penaltı','Kaleye çekilen şut','Serbest Vuruş'

goals = [16,25,7]
colors = ["g","r","b"]

plt.pie(goals,labels =goal_types,colors=colors, shadow=True, explode=(0.05,0.05,0.05),autopct="%1.1f%%") # shadow gölgelendirmedir, explode pasta dilimlerinin ayrıklığıdır. Autopct parametresi, her dilimin üzerine yüzdelik değeri ekler. "%1.1f%%" formatı, yüzde değerini bir ondalık basamak ile gösterir.
plt.show()

"""
"""
# Bar grafiği

plt.bar([0,0.25,1.25,2.25,3.25],[20,30,45,90,100],label = "BMW",width=.2) # width genişliği gösterir.
plt.bar([0,0.75,1.75,2.75,3.75],[60,50,45,20,60],label = "AUDI",width=.2)

plt.legend()
plt.xlabel("Gün")
plt.ylabel("Mesafe(km)")
plt.title("Araç bilgileri")
plt.show()

"""
"""
#Histogram Grafiği

yaslar = [20,13,25,62,95,23,52,20,14,61,15,19,23,27,24,20,28,45]
yas_gruplari = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(yaslar,yas_gruplari,histtype="bar",rwidth=0.8)

plt.xlabel("Yaş grupları")
plt.ylabel("Kişi sayısı")
plt.title("Yaş gruplandırma")
plt.show()

"""