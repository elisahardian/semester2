// FUNGSI, PRIVATE, PARAMETER

//ini main program
package com.mycompany.segitiga;
import java.util.Scanner;

public class Segitiga {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        //instansiasi kelas menjadi objek
        clssegitiga objSegitiga = new clssegitiga();
        System.out.printf("masukkan alas: ");
        objSegitiga.setAlas(input.nextInt());
        System.out.printf("masukkan tinggi: ");
        objSegitiga.setTinggi(input.nextInt());
        System.out.printf("luas segitiga: %.2f \n", objSegitiga.luas(objSegitiga.getAlas(), objSegitiga.getTinggi()));
    }
}

