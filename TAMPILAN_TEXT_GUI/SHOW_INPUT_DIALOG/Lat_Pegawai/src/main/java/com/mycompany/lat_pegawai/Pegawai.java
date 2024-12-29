//ini kelas
package com.mycompany.lat_pegawai;

public class Pegawai {
    //mendeklarasikan atribut
    String idPegawai;
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
        return gaji+tunjangan();
    }
}
