
package com.mycompany.pernyataanreturn;

public class PernyataanReturn {

    static double LuasSegitiga(int alas, int tinggi)
    {
        double luas = 0.5 * alas * tinggi;
        return luas;
    }
    
    public static void main(String[] args) {
        int Alas = 4;
        int Tinggi = 4;
        System.out.println("alas segitiga: "+ Alas);
        System.out.println("tinggi segitiga: "+ Tinggi);
        System.out.println("luas segitiga: "+ LuasSegitiga(Alas, Tinggi));
    }
}

// RETURN untuk segera keluar dari fungsi perulangan