
package com.mycompany.latdokter_classbuffereader;


public class clsdokter_classbuffereader {
    //mendeklarasikan atribut
    String idDokter;
    String nama;
    int gaji;
    //membuat methode dengan fungsi
    public float tunjangan()
    {
        return gaji*10/100;
    }
    //membuat methode dengan fungsi
    public float totalGaji()
    {
        return tunjangan()+gaji;
    }
    
}
