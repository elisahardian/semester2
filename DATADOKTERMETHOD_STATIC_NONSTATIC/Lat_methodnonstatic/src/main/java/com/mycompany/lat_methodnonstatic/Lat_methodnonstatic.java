// LATIHAN METHOD NON STATIC
//ini main program

package com.mycompany.lat_methodnonstatic;
import java.util.Scanner;

public class Lat_methodnonstatic {

    public static void main(String[] args) {
        //membuat scanner
        Scanner input = new Scanner(System.in);
        //instansiasi kelas menjadi objek
        cls_methodnonstatic objDok = new cls_methodnonstatic();
        System.out.println("<<masukkan data>>");
        System.out.print("ID Dokter\t: ");
        objDok.idDokter = input.nextLine();
        System.out.print("Nama Dokter\t: ");
        objDok.nama = input.nextLine();
        System.out.print("Gaji\t\t: ");
        objDok.gaji = input.nextInt();
        //menampilkan data
        System.out.println();
        System.out.println("ID Dokter\t: "+ objDok.idDokter);
        System.out.println("Nama Dokter\t: "+ objDok.nama);
        System.out.println("Gaji\t\t: "+ objDok.gaji);
        System.out.printf("Tunjangan\t: %.2f\n",+ objDok.tunjangan(objDok.gaji));
        System.out.printf("Total Gaji\t: %.2f\n",+ objDok.total_gaji(objDok.gaji));
        
    }
}
