
package com.mycompany.latdokter_interface_pembungkusan;
import java.text.NumberFormat;
import java.util.Scanner;

public class Latdokter_interface_pembungkusan {

    public static void main(String[] args) {
        Scanner input = new Scanner (System.in);
        
        //instansiasi kelas menjadi objek
        clsdokter_interface_pembungkusan objDok = new clsdokter_interface_pembungkusan();
        
        //membuat format ribuan
        NumberFormat f = NumberFormat.getInstance();
        f.setMinimumIntegerDigits(0);
        f.setGroupingUsed(true);
        
        System.out.print("ID Dokter: ");
        objDok.id = input.nextLine();
        System.out.print("Nama: ");
        objDok.nama = input.nextLine();
        System.out.print("Gaji: ");
        objDok.gaji = input.nextInt();
        
        System.out.println();
        System.out.println("<<BERKAS DOKTER>>");
        System.out.println("ID Dokter: "+ objDok.id);
        System.out.println("Nama: "+ objDok.nama);
        System.out.println("Gaji: "+ f.format(objDok.gaji));
        System.out.println("Tunjangan: "+ f.format(objDok.tunjangan(objDok.gaji)));
        System.out.println("Total gaji: "+ f.format(objDok.total_gaji(objDok.gaji, objDok.tunjangan(objDok.gaji))));
        
        
    }
}
