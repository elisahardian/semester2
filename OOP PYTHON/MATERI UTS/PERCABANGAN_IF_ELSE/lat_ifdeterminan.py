#import library math
import math
#membuat kelas
class Diskriminan:
    #membuat konstruktor
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
    #membuat method hitung nilai diskriminan
    def hitung(self, a,b, c):
        d=b*b-4*a*c
        print()
        print("nilai diskriminan:", d)
        if(d>0):
            x1=(-b + math.sqrt(d))/(2*a)
            x2=(-b - math.sqrt(d))/(2*a)
            print("disebut dengan kaar real")
            print("nilai x1= ", x1)
            print("nilai x2= ", x2)
        elif (d==0):
            x1=-b/(2*a)
            x2=x1
            print("nilai x1= ", x1)
            print("nilai x2= ", x2)
        else:
            r=-b/(2*a)
            #bagian imajiner
            i=math.sqrt(math.fabs(d))/(2*a)
            print("disebut dengan akar kompleks")
            print("nilai x1= ", r, "+", i)
            print("nilai x2= ", r, "-", i)
#blok main program
def main():
    #instansiasi kelas menajdi objek
    objDiskriminan= Diskriminan(None, None, None)
    objDiskriminan.a=int(input("masukkan nilai a:"))
    objDiskriminan.b=int(input("masukkan nilai b:"))
    objDiskriminan.c=int(input("masukkan nilai c:"))
    objDiskriminan.hitung(objDiskriminan.a, objDiskriminan.b, objDiskriminan.c)
main()