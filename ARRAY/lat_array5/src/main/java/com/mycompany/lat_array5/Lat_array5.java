// ARRAY 2 DIMENSI
// elemen array dimasukkan lewat keyboard

package com.mycompany.lat_array5;
import javax.swing.JOptionPane;

public class Lat_array5 {

    public static void main(String[] args) {
        int[][] x = new int[4][4]; // mau diisi [4][] juga bisa
        x[0] = new int[1];
        x[1] = new int[2];
        x[2] = new int[3];
        x[3] = new int[4];
        int i, j;
        for (i = 0 ; i < 4 ; i++)
        {
            for (j = 0 ; j < i + 1 ; j++)
            {
                String bilangan = JOptionPane.showInputDialog("masukkan nilai: ");
                x[i][j]=Integer.parseInt(bilangan);
            }
        }
        //menampilkan nilai matriks
        for (i = 0 ; i < 4 ; i++) 
        {
            for (j = 0 ; j < i + 1 ; j++)
            System.out.print(x[i][j] + " ");
            System.out.println();
        }
        System.exit(0);
    }
}
