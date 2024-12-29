//MENCARI RATA RATA DARI ARRAY KONSEP PBO (pelajari lagi)

package com.mycompany.nilairatarata_array;
import java.util.Scanner;

public class Nilairatarata_array {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("masukkan jumlah elemen array: ");
        int jumlahelemen = input.nextInt();
        //membuat objek array
        int[] array = new int[jumlahelemen];
        //memasukan nilai kedalam array
        for (int i = 0 ; i < jumlahelemen ; i++)
        {
            System.out.print("masukkan nilai ke-" + (i+1) + ": ");
            //scanner.nextInt();
            array[i] = input.nextInt();
        }
        //menghitung nilai rata rata
        double rata = hitungrata(array);
        //menampilkan hasil
        System.out.println("rata rata dalam array adalah: " + rata);
        
        }
    //metode untuk menghitung rata rata
    private static double hitungrata(int[] array)
    {
        int total = 0;
        //menjumlahkan semua elemen array
        for (int nilai : array)
        {
            total+=nilai;
        }
        //menghitung rata rata
        return (double) total / array.length;
    }        
}
