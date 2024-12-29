// LATIHAN METHOD STATIC
//static = tidak perlu instansiasi kelas menjadi objek bisa langsung dipakai. 
//ini class

package com.mycompany.lat_methodstatic;

public class cls_methodstatic {
    //mendeklarasikan atribut static
    static String idDokter;
    static String nama;
    static int gaji;
    //membuat static method dengan fungsi
    public static float tunjangan(int Gaji)
    {
        return Gaji / 100 * 10;
    }
    //membuat static method dengan fungsi
    public static float total_gaji(int Gaji)
    {
        return Gaji + tunjangan(Gaji);
    }
    
}
