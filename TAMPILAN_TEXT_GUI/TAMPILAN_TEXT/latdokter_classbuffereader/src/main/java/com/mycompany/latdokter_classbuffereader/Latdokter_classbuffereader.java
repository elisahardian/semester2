
package com.mycompany.latdokter_classbuffereader;
//import library
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Latdokter_classbuffereader {

    public static void main(String[] args) {
        //membuat scanner baru
        InputStreamReader isr = new InputStreamReader(System.in);
        //membuat objek bufferreaader
        BufferedReader br = new BufferedReader(isr);
        //membuat objek
        clsdokter_classbuffereader objDokter = new clsdokter_classbuffereader();
        
        System.out.print("ID Dokter: ");
        objDokter.idDokter = br.readLine();// gatau kenapa error
        System.out.print("Nama: ");
        objDokter.nama = br.readLine();
        System.out.print("Gaji: ");
        objDokter.gaji = Integer.parseInt(br.readLine());
        
        //menampilkan data
        System.out.println("ID Dokter: "+ objDokter.idDokter);
        System.out.println("Nama: "+ objDokter.nama);
        System.out.println("Gaji: "+objDokter.gaji);
        System.out.printf("Tunjangan: %.2f\n"+ objDokter.tunjangan());
        System.out.printf("Total gaji: %.2f\n"+objDokter.totalGaji());
        
    }
}
