

package com.mycompany.latluasbangun_banyakbentuk;
//import library
import java.util.Scanner;

public class Latluasbangun_banyakbentuk {

    public static void main(String[] args) {
        
        Scanner input = new Scanner (System.in);    
        //instansiasi kelas menjadi objek
        clsinduk_bangun_banyakbentuk objBangun = new clsinduk_bangun_banyakbentuk();
        clsturunan_segi3_banyakbentuk objSegiTiga = new clsturunan_segi3_banyakbentuk();
        clsturunan_segi4_banyakbentuk objSegiEmpat = new clsturunan_segi4_banyakbentuk();
        
        System.out.printf("masukkan nilai x: ");
        objBangun.setNiaiX(input.nextInt());
        System.out.printf("masukkan nilai y: ");
        objBangun.setNilaiY(input.nextInt());
        System.out.println("luas bangun: ");
        System.out.println("luas segiempat: "+ objSegiEmpat.hitung(objBangun.getNilaiX(), objBangun.getNilaiY()));
        System.out.println("luas segitiga: "+ objSegiTiga.hitung(objBangun.getNilaiX(), objBangun.getNilaiY()));
        
        
    }
}
