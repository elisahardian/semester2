
package com.mycompany.latdokter_teksscanner;


public class clsdokter_teksscanner {
    //mendeklarasikan atribut
    String idDokter;
    String nama;
    int gaji;
    
    //membuat method dengan fungsi
    public float tunjangan()
    {
        return gaji*10/100;
    }
    //membuat method dengan fungsi
    public float totalGaji()
    {
        return tunjangan() + gaji;
    }
    
}
