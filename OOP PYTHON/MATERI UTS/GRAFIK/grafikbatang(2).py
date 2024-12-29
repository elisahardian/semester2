#2
# GRAFIK BATANG DARI KECIL(atas) KE BESAR(bawah) 


import matplotlib.pyplot as plt
#data yang akan digunakan untuk grafik batang horizontal
categories = ['kategori1', 'kategori 2', 'kategori 3', 'kategori 4', 'kategori 5', 'kategori 6', 'kategori 7', 'kategori 8', 'kategori 9', 'kategori 10']
values= [10,25,15,30,60,70,100,20,50,150]
sortedvalues= sorted(values, reverse = True)
sortedcategories= sorted(categories, reverse = True)
colors= ['green', 'pink', 'darkblue', 'orange', 'lightblue', 'yellow', 'grey', 'purple', 'red', 'brown']

#membuat grafik batang horizontal
plt.barh(sortedcategories, sortedvalues, color=colors)
#menambahkan label pada sumbu x dan y 
plt.xlabel('nilai')
plt.ylabel('kategori')
#menampilkan jumlah data diatas setiap batang
for i, value in enumerate (sortedvalues):
    plt.text(value, i, str(value), va='center')
#menampilkan grafik
plt.show()
