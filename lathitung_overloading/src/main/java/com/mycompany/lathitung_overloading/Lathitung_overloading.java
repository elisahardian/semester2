
package com.mycompany.lathitung_overloading;


public class Lathitung_overloading {

    public static void main(String[] args) {
        //instansiasi kelas menjadi objek
        clshitung_overloading objHitung = new clshitung_overloading();
        System.out.println("hasil a+b= "+ objHitung.hasil(10, 5));
        System.out.println("hasil a+b*c= "+ objHitung.hasil(10, 5, 2));
        System.out.println("hasil a+b+c+d= "+objHitung.hasil(10, 5, 2, 4));
        
    }
}
