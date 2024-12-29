// LATIHAN NON OBJEK/ FUNGSI TANPA PARAMETER

package com.mycompany.lat_nonobj_fungsi_tanpaparam;
//import library scanner
import java.util.Scanner;

public class Lat_Nonobj_Fungsi_Tanpaparam {
    //membuat fungsi tanpa parameter
    static double HitungLuas()
    {
        //instansiasi library kelas Scanner
        Scanner input = new Scanner(System.in);
        //deklarasi variabel
        int alas, tinggi;
        System.out.print("masukkan alas: ");
        alas = input.nextInt();
        System.out.print("masukkan tinggi: ");
        tinggi = input.nextInt();
        return 0.5 * alas * tinggi;
    }
    
    public static void main(String[] args) {
        System.out.printf("luas segitiga: %.2f ", HitungLuas());
    }
}
