"""
#perulangan while berhenti apabila syarat tidak terpenuhi untuk melakukan proses pengulangan

i=0
while i <= 6:
    print("loop ke: ", i)
    i = i + 1
"""

#menggunakan perintah while untuk menunggu konfirmasi dari pengguna
jawab = "y"
while jawab == "y":
    nama=str(input("masukkan data nama\t: "))
    print()
    jawab=str(input("mau coba lagi [y/t]\t: ").lower())

