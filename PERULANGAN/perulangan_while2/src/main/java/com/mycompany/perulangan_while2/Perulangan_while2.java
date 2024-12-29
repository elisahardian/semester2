//non objek. paradigma terstruktur

package com.mycompany.perulangan_while2;
import java.util.Scanner;

public class Perulangan_while2 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String jawab="y";
        int angka;
        while (jawab.equals("y")||jawab.equals("Y"))
        {
            System.out.print("masukkan angka: ");
            angka=input.nextInt();
            System.out.print("coba lagi[y/t]: ");
            jawab=input.next().toUpperCase();
        }
    }
}
