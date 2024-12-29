

package com.mycompany.fibonancci;
import java.util.Scanner;

public class Fibonancci {
    
    public static int Fibbo(int n)
    {
        int c;
        if (n==0)
            return 0;
        if (n==1)
            return 1;
        else
            c= Fibbo(n-1) + Fibbo(n-2);
            return c;
    }

    public static void main(String[] args) {
        int n, t, i;
        Scanner input = new Scanner (System.in);
        System.out.print("Batas deret fibonancci: ");
        n= input.nextInt();
        for (i=0 ; i<=n ; i++)
        {
            t=Fibbo(i);
            System.out.print(t + " ");
        }    
            
    }
}
