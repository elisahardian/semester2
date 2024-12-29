//ini kelas
package com.mycompany.lat_dokter;

public class Dokter {
    //mendeklarasikan atribut
    String idDokter;
    String nama;
    int gaji;
    //membuat method dengan fungsi
    public float tunjangan()
    {
        return gaji/100*10;
    }
    
    //membuat method dengan fungsi
    public float totalGaji()
    {
        return gaji+tunjangan();
    }
}
