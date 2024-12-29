// LATIHAN DOKTER. PROSEDUR, PRIVATE, PARAMETER
// ini main program 

package com.mycompany.latdokter_oop_prosedur_private_param;
//import library scanner
import java.util.Scanner;

public class Latdokter_Oop_Prosedur_Private_Param {

    public static void main(String[] args) {
        //instansiasi library kelas Scanner
        Scanner input = new Scanner(System.in);
        //instansiasi kelas menjadi objek
        clsdokter_prosedur_private_param objDokter = new clsdokter_prosedur_private_param();
        System.out.print("ID Dokter\t: ");
        objDokter.setId(input.nextLine());
        System.out.print("Nama Dokter\t: ");
        objDokter.setNama(input.nextLine());
        System.out.print("Gaji\t\t: ");
        objDokter.setGaji(input.nextInt());  
        objDokter.tunjangan(objDokter.getGaji());
        objDokter.total_gaji(objDokter.getGaji());
    }
}
