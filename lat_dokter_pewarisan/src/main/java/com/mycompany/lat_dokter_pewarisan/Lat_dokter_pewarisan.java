

package com.mycompany.lat_dokter_pewarisan;
import java.util.Scanner;

public class Lat_dokter_pewarisan {

    public static void main(String[] args) {
        Scanner input = new Scanner (System.in);
        
        //instansiasi kelas menjadi objek
        cls_spesialis_pewarisan objSpe = new cls_spesialis_pewarisan();
        
        System.out.println("kelas induk dokter");
        System.out.print("masukkan id\t: ");
        objSpe.setId(input.nextLine());
        System.out.print("masukkan nama\t: ");
        objSpe.setNama(input.nextLine());
        System.out.print("masukkan gaji\t: ");
        objSpe.setGaji(input.nextInt());
        System.out.printf("tunj.dokter\t: %.2f\n", objSpe.tunjangan(objSpe.getGaji()));
        System.out.println();
        System.out.println("kelas anak spesialis");
        System.out.printf("tunj.spesialis\t: ");
        objSpe.setTunSpesialis(input.nextInt());
        System.out.printf("uang makan\t: %.2f\n", objSpe.uang_makan(objSpe.getGaji()));
        System.out.printf("total gaji\t: %.2f\n", objSpe.total_gaji(objSpe.getGaji(), objSpe.tunjangan(objSpe.getGaji()), objSpe.getTunSpesialis(), objSpe.uang_makan(objSpe.getGaji())));
        
    }
}
