// LATIHAN NON OBJEK. PROSEDUR, PARAMETER

package com.mycompany.lat_nonobj_prosedur_param;
import java.util.Scanner;

public class Lat_Nonobj_Prosedur_Param {
    //membuat prosedur dengam parameter
    static void HitungLuas(int alas, int tinggi)
    {
        //deklarasi variabel
        double Luas;
        Luas = 0.5 * alas * tinggi;
        System.out.printf("luas segitiga: %.2f ", Luas);
    }
    
    public static void main(String[] args) {
        //deklarasi variabel
        int alas, tinggi;
        //instansiasi library kelas scanner
        Scanner input = new Scanner(System.in);
        System.out.print("masukkan alas: ");
        alas = input.nextInt();
        System.out.print("masukkan tinggi: ");
        tinggi = input.nextInt();
        //memanggil prosedur
        HitungLuas(alas, tinggi);
    }
}
