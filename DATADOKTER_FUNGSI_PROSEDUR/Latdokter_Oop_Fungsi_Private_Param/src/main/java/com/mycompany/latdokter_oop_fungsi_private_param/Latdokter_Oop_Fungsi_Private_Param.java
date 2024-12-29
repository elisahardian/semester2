// LATIHAN DOKTER. FUNGSI, PRIVATE, PARAMETER
// ini main program 

package com.mycompany.latdokter_oop_fungsi_private_param;
import java.util.Scanner;

public class Latdokter_Oop_Fungsi_Private_Param {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        //instansiasi kelas menjadi objek
        clsdokter_fungsi_private_param objDokter = new clsdokter_fungsi_private_param();
        System.out.print("ID Dokter\t: ");
        objDokter.setId(input.nextLine());
        System.out.print("Nama Dokter\t: ");
        objDokter.setNama(input.nextLine());
        System.out.print("Gaji\t\t: ");
        objDokter.setGaji(input.nextInt());
        System.out.printf("Tunjangan\t: %.2f \n", objDokter.tunjangan(objDokter.getGaji()));
        System.out.printf("Total Gaji\t: %.2f \n", objDokter.total_gaji(objDokter.getGaji()));
    }
}
