#PROGRAM GRAFIK LINGKARAN 1

#import lingkaran matplotlib
import matplotlib.pyplot as plt #downlod librarynta
labels = ['Dokter', 'Guru', 'Pegawai Kantor', 'Pedagang', 'IT']
jumlah = [20, 10, 12, 11, 25]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'blue', 'green']
plt.title('Daftar profesi')
plt.pie(jumlah, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.show()
          