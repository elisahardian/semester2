// BUKAN OOP ????

package com.mycompany.lat_bilanganprima;
import java.util.Scanner;

public class Lat_bilanganprima {

    public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
        int bil, awal, akhir;
        
        System.out.println("PROGRAM JAVA MENAMPILKAN DERET BILANGAN PRIMA");
        System.out.print("Mulai dari : ");
        awal=input.nextInt();
        System.out.print("Sampai : ");
        akhir=input.nextInt();
        System.out.println("----------------------------------------------");
        for (int i=awal; i<=akhir; i++){
            bil=0;
            for (int j=1 ; j<=i ; j++){
                if (i%j == 0){
                    bil=bil+1;
                }
            }
            if (bil==2){
                System.out.print(i + " ");
            }             
        }    
   }
}


        
