// MENCARI NILAI TERBESAR DAN NILAI TERKECIL SUATU ARRAY (pelajari lagi)

package com.mycompany.nilaiterbesarterkecil_array;
import java.util.Scanner;

public class Nilaiterbesarterkecil_array {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("masukkan jumlah elemen array: ");
        int jumlahelemen= input.nextInt();
        //membuat objek array
        int[] array = new int[jumlahelemen];
        //memasukkan nilai kedalam array
        for (int i = 0 ; i < jumlahelemen ; i++)
        {
            System.out.print("masukkan nilai ke-" + (i+1) + ": ");
            array[i]= input.nextInt();
        }
        //mencari nilai terbesar terkecil
        int nilaiterbesar = cariterbesar(array);
        int nilaiterkecil = cariterkecil(array);
        //menampilkan hasil
        System.out.println("nilai terbesar dalam array: " + nilaiterbesar);
        System.out.println("nilai terkecil dalam array: " + nilaiterkecil);
    }
    //metode uuntuk mencari nilai terbesar dalam array
    private static int cariterbesar(int[] array)
    {
        int terbesar = array[0];
        for (int nilai : array)
        {
            if (nilai > terbesar)
            {
                terbesar = nilai;
            }
        }
        return terbesar;
    }
    //metode untuk mencari nilai terkecil dalam array
    private static int cariterkecil(int[] array)
    {
        int terkecil = array[0];
        for (int nilai : array)
        {
            if (nilai < terkecil)
            {
                terkecil = nilai;
            }
        }
        return terkecil;
    }
}
