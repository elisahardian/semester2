
package com.mycompany.lat_methodstaticfinal;

public class cls_methodstaticfinal {
    //membuat variabel static final
    public static final int BESAR_TUNJANGAN = 10;
    //mendeklarasikan atribut
    static String idDokter;
    static String nama;
    static int gaji;
    //membuat static method dengan fungsi
    public static float tunjangan(int Gaji)
    {
        return Gaji/100 *BESAR_TUNJANGAN;
    }
    //membuat static method dengan fungsi
    public static float total_gaji(int Gaji)
    {
        return Gaji + tunjangan(Gaji);
    }
    
}
