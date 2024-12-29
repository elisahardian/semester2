// LATIHAN NON OBJEK. PROSEDUR, TANPA PARAMETER. 

package com.mycompany.lat_nonobj_prosedur_tanpaparam;
import java.util.Scanner;

public class Lat_Nonobj_Prosedur_Tanpaparam {
    //membuat prosedur tanpa parameter.. non obj gapake class jadi bikinnya disini.
    static void HitungLuas()
    {
        //instansiasi library kelas Scanner
        Scanner input = new Scanner(System.in);
        //deklaras variabel
        int alas, tinggi;
        double Luas;
        System.out.print("masukkan alas: ");
        alas = input.nextInt();
        System.out.print("masukkan tinggi: ");
        tinggi = input.nextInt();
        Luas = 0.5 * alas * tinggi;
        System.out.printf("luas segitiga: %.2f ", Luas);
    }
    
    public static void main(String[] args) {
        //memanggil prosedur
        HitungLuas();
    }
}
