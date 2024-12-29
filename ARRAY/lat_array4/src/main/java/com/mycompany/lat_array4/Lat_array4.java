// ARRAY 2 DIMENSI

package com.mycompany.lat_array4;


public class Lat_array4 {

    public static void main(String[] args) {
        int[][] bilangan = {{10, 20, 30, 40, 50},{11, 12, 13, 14, 15},{12, 13, 14, 15, 16},{13, 14, 15, 16, 17}};
        //menampilkan nilai matriks
        for (int i = 0 ; i < 4 ; i++)
        {
            for (int j = 0 ; j < 5 ; j++)
            System.out.print(bilangan[i][j] + " ");
            System.out.println();
        }
    }
}
