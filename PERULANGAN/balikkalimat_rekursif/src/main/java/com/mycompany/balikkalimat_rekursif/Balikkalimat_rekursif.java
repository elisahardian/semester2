

package com.mycompany.balikkalimat_rekursif;
import java.util.*;

public class Balikkalimat_rekursif {

    public static void main(String[] args) {
        String teks, hasil = "";
        Scanner input = new Scanner(System.in);
        System.out.print("masukkan string\t: ");
        teks= input.nextLine();
        System.out.println("Hasil reverse\t: "+ recursive(teks));
    }
    
    private static String recursive(String teks)
    {
        if (teks.isEmpty())
        {
            return teks;
        }
        return recursive(teks.substring(1))+ teks.charAt(0);
    }
}
