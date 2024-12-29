// LATIHAN METHOD STATIC DENGAN IMPORT
//ini main program

package com.mycompany.lat_methodstatic_import;
import java.util.Scanner;
//import atribut dan method static
 // ini nama package dan nama kelas.. com.mycompany.lat_methodstatic_import , dan cls_methodstatic_import
import static com.mycompany.lat_methodstatic_import.cls_methodstatic_import.idDokter;
import static com.mycompany.lat_methodstatic_import.cls_methodstatic_import.nama;
import static com.mycompany.lat_methodstatic_import.cls_methodstatic_import.gaji;
import static com.mycompany.lat_methodstatic_import.cls_methodstatic_import.tunjangan;
import static com.mycompany.lat_methodstatic_import.cls_methodstatic_import.total_gaji;

public class Lat_methodstatic_import {

    public static void main(String[] args) {
        //membuat scanner
        Scanner input = new Scanner(System.in);
        System.out.println("<<masukkan data>>");
        System.out.print("ID Dokter\t: ");
        idDokter = input.nextLine();
        System.out.print("Nama Dokter\t: ");
        nama = input.nextLine();
        System.out.print("Gaji\t\t: ");
        gaji = input. nextInt();
        //menampilkan data
        System.out.println();
        System.out.println("<<menampilkan data>>");
        System.out.println("ID Dokter\t: "+ idDokter);
        System.out.println("Nama Dokter\t: "+ nama);
        System.out.println("Gaji\t\t: "+ gaji);
        System.out.printf("Tunjangan\t: %.2f\n",+ tunjangan(gaji));
        System.out.printf("Total Gaji\t: %.2f\n",+ total_gaji(gaji));
    }
}
