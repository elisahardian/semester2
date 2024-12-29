
package com.mycompany.lathitung_prosedur_param;


public class Lathitung_prosedur_param {
    
    //membuat prosedur
    static void tambah(int a, int b)
    {
        int hasil;
        hasil = a+b;
        System.out.print("hasil: "+ hasil);
    }
    
    public static void main(String[] args) {
        int nilaia, nilaib;
        nilaia=100;
        nilaib=200;
        //memanggil prosedur
        tambah(nilaia, nilaib);
    }
}
