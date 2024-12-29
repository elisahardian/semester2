// LATIHAN METHOD NON STATIC
//ini class
package com.mycompany.lat_methodnonstatic;

public class cls_methodnonstatic {
    //mendeklarasikan atribut nonstatic
    public String idDokter;
    public String nama;
    public int gaji;
    //membuat non static method dengan fungsi
    public float tunjangan(int Gaji)
    {
        return Gaji / 100 * 10; 
    }
    //membuat non static method dengan fungsi
    public float total_gaji(int Gaji)
    {
        return Gaji + tunjangan(Gaji);
    }
    
}
