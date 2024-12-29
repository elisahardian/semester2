
package com.mycompany.lat_methodstaticfinal;
import java.util.Scanner;

public class Lat_methodstaticfinal {

    public static void main(String[] args) {
        //membuat scanner
        Scanner input = new Scanner (System.in);
        System.out.println("<<MEMASUKKAN DATA>>");
        System.out.print("ID Dokter: ");
        cls_methodstaticfinal.idDokter = input.nextLine();
        System.out.print("Nama: ");
        cls_methodstaticfinal.nama = input.nextLine();
        System.out.print("Gaji: ");
        cls_methodstaticfinal.gaji = input.nextInt();
        
        //menampilkan data
        System.out.println("<<MENAMPILKAN DATA>>");
        System.out.println("ID Dokter: "+ cls_methodstaticfinal.idDokter);
        System.out.println("Nama Dokter: "+ cls_methodstaticfinal.nama);
        System.out.println("Gaji: "+ cls_methodstaticfinal.gaji);
        System.out.printf("Tunjangan: %.2f\n", + cls_methodstaticfinal.tunjangan(cls_methodstaticfinal.gaji));
        System.out.printf("Total gaji: %.2f\n", + cls_methodstaticfinal.total_gaji(cls_methodstaticfinal.gaji));
        
    }
}
