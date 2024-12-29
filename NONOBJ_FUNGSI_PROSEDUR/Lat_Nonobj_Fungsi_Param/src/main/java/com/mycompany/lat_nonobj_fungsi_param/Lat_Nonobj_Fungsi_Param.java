// LATIHAN NON OBJEK. FUNGSI, PARAMETER

package com.mycompany.lat_nonobj_fungsi_param;
import java.util.Scanner;

public class Lat_Nonobj_Fungsi_Param {
    //membuat fungsi dengan param
    static double HitungLuas(int alas, int tinggi)
    {
        return 0.5 * alas * tinggi;
    } 
    public static void main(String[] args) {
        //instansiasi library kelas scanner
        Scanner input = new Scanner(System.in);
        //deklarasi variabel
        int alas, tinggi;
        System.out.print("masukkan alas: ");
        alas = input.nextInt();
        System.out.print("masukkan tinggi: ");
        tinggi = input.nextInt();
        System.out.printf("luas segitiga: %.2f ", HitungLuas(alas, tinggi));
    }
}
