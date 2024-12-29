# PROGRAM OOP. DAFTAR BILANGAN PRIMA
# dari sendiri. coba lagi

class bilanganprima:
    def __init__(self, batas):
        self.batas= batas
    def apakahprima(self, angka):
        if angka < 2:
            return False
        for i in range(2, int(angka**0.5)+1):
            if angka%i ==0:
                return False
            return True
        def prima(self):
            primes=[angka for angka in range(self.batas + 1) if self.apakahprima(angka)]
            return primes
def main():
    batas= int(input("masukkan batas bilangan prima: "))
    bilangan_prima = bilanganprima(batas)
    angkaprima=bilangan_prima.primes()
    print(f"bilangan prima dari 0 sampi {batas}: ")
    print(angkaprima)

if __name__ == "__main__":
    main()