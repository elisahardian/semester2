// ARRAY 1 DIMENSI

package com.mycompany.lat_array3;
import javax.swing.JOptionPane;

public class Lat_array3 {

    public static void main(String[] args) {
        Float[] NilaiArray = new Float[5];
        for (int i = 0 ; i < 5 ; i++)
        {
            String bilangan = JOptionPane.showInputDialog("Masukan elemen array ke: " + i);
            System.out.println("Index ke " + i + " : " + bilangan);
            NilaiArray[i]=Float.parseFloat(bilangan);
        }
        //menampilkan nilai array
        System.out.println();
        for (int i = 0 ; i < 5 ; i++)
            System.out.println("Elemen ke : " + i + " nilainya " + NilaiArray[i]);
    }
}
