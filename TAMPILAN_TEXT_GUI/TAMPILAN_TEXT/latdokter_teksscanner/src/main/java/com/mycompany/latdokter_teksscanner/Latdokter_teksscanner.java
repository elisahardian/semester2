

package com.mycompany.latdokter_teksscanner;
import java.util.Scanner;
        
public class Latdokter_teksscanner {

    public static void main(String[] args) {
        //instansiasi kelas library atau membuat scanner baru
        Scanner input = new Scanner(System.in);
        //instansiasi kelas menjadi objek
        clsdokter_teksscanner objDok = new clsdokter_teksscanner();
        
        System.out.print("ID Dokter: ");
        objDok.idDokter = input.nextLine();
        System.out.print("Nama: ");
        objDok.nama = input.nextLine();
        System.out.print("Gaji: ");
        objDok.gaji = input.nextInt();
        
        //menampilkan data
        System.out.println("<<MENAMPILKAN DATA>>\nBERKAS DOKTER");
        System.out.println("ID Dokter: "+ objDok.idDokter);
        System.out.println("Nama Dokter: "+ objDok.nama);
        System.out.println("Gaji Dokter: "+ objDok.gaji);
        System.out.printf("Tunjangan: %.2f\n", objDok.tunjangan());
        System.out.printf("Total gaji: %.2f\n", objDok.totalGaji());
        
    }
}
