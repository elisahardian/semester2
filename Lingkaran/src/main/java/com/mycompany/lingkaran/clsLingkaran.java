//ini class
package com.mycompany.lingkaran;

public class clsLingkaran {
    //deklarasi atribut
    double jari, phi=3.14; //jika tidak disebutkan private/protected maka otomatis menjadi public
    //buat method fungsi
    public double keliling(double jari)
    {
        return 2 * phi * jari;
    }
}
