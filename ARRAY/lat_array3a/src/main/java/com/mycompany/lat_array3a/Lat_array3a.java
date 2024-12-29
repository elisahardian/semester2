//panjang array mau minta dari input user.

package com.mycompany.lat_array3a;
import javax.swing.JOptionPane;
import java.util.Scanner;

public class Lat_array3a {

    public static void main(String[] args) {
        int n;
        Scanner input = new Scanner(System.in);
        System.out.print("panjang array: ");
        n=input.nextInt();
        
        
        Float[] NilaiArray = new Float[n];
        for (int i = 0 ; i < n ; i++)
        {
            String bilangan = JOptionPane.showInputDialog("Masukan elemen array ke: " + i);
            System.out.println("Index ke " + i + " : " + bilangan);
            NilaiArray[i]=Float.parseFloat(bilangan);
        }
        //menampilkan nilai array
        System.out.println();
        for (int i = 0 ; i < n ; i++)
            System.out.println("Elemen ke : " + i + " nilainya " + NilaiArray[i]);
    }
}
