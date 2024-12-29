//ini main progream
package com.mycompany.lingkaran;
import java.util.Scanner;

public class Lingkaran {

    public static void main(String[] args) {
        Scanner input = new Scanner (System.in);
        //instansiasi kelas menjadi objek
        clsLingkaran objLing = new clsLingkaran();
        System.out.print("masukkan jari-jari: ");
        objLing.jari = input.nextDouble();
        //System.out.println("keliling lingkaran: " + String.format("%.2f", objLing.keliling(objLing.jari))); //bisa juga gini. pake format string
        System.out.printf("keliling lingkaran: %.2f\n", objLing.keliling(objLing.jari)); //bisa gini. angsung pake printf
        
    }
}
