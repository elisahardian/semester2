//ini main program
package com.mycompany.lat_dokter;
import javax.swing.JOptionPane;

public class Lat_Dokter {

    public static void main(String[] args) {
        //membuat objek
        Dokter objDokter = new Dokter();
        //membuat kotak dialog dengan showInputDialog()
        objDokter.idDokter = JOptionPane.showInputDialog("id Dokter: ");
        objDokter.nama = JOptionPane.showInputDialog("Nama Dokter: ");
        String mGaji = JOptionPane.showInputDialog("Gaji: ");
        objDokter.gaji = Integer.parseInt(mGaji);
        
        //menampilkan data
        System.out.println();
        System.out.println("<<Menampilkan Data>>");
        System.out.println("Berkas Dokter");
        System.out.println("id Dokter\t: " + objDokter.idDokter);
        System.out.println("Nama Dokter\t: " + objDokter.nama);
        System.out.println("Gaji Dokter\t: " + objDokter.gaji);
        System.out.printf("Tunjangan\t: %.2f\n", + objDokter.tunjangan());
        System.out.printf("Total Gaji\t: %.2f\n", + objDokter.totalGaji());
    }
}
