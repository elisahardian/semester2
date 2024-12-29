// LATIHAN METHOD STATIC
//ini main program

package com.mycompany.lat_methodstatic;
import java.util.Scanner;

public class Lat_methodstatic {

    public static void main(String[] args) {
        //membuat scanner
        Scanner input = new Scanner(System.in);
        System.out.println("<<masukkan data>>");
        System.out.print("ID Dokter\t: ");
        cls_methodstatic.idDokter = input.nextLine(); // yg ini dari nama kelas. cls_methodstatic
        System.out.print("Nama Dokter\t: ");
        cls_methodstatic.nama = input.nextLine();
        System.out.print("Gaji\t\t: ");
        cls_methodstatic.gaji = input.nextInt();
        //menampilkan data
        System.out.println();
        System.out.println("<<menampilkan data>>");
        System.out.println("ID Dokter\t: "+ cls_methodstatic.idDokter); // yg ini dari nama kelas. cls_methodstatic
        System.out.println("Nama Dokter\t: "+ cls_methodstatic.nama);
        System.out.println("Gaji\t\t: "+ cls_methodstatic.gaji);
        System.out.printf("Tunjangan\t: %.2f\n", + cls_methodstatic.tunjangan(cls_methodstatic.gaji));
        System.out.printf("Total Gaji\t: %.2f\n", + cls_methodstatic.total_gaji(cls_methodstatic.gaji));
        
    }
}
