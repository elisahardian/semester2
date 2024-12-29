// INI CLASS. PUBLIC, FUNGSI, NON PARAM

package com.mycompany.lat_sewakendaraan_if;

public class cls_sewakendaraan {
    //mendeklarasikan atribut
    public String idPenyewa;
    public String nama;
    public String alamat;
    public String noktp;
    public String notelp;
    public String jeniskendaraan;
    public String noplat;
    public int lamasewa;
    public int biayasewa;
    
    //membuat method dengan fungsi
    public float totalsewa()
    {
        return lamasewa*biayasewa;
    }
    //membuat method dengan fungsi
    public float potonganharga()
    {
        float totalsewa= totalsewa();
        float potongan=0;
        
        if (lamasewa >=7)
        {
            potongan = 0.05f * totalsewa;
        }
        else if (lamasewa >=5)
        {
            potongan = 0.03f * totalsewa;
        }
        else if (lamasewa >=3)
        {
            potongan = 0.02f * totalsewa;
        }
        return potongan;
    }
    public float ppn()
    {
        return 0.02f * totalsewa();
    }
    public float jumlahbayar()
    {
        return totalsewa() - potonganharga() + ppn();
    }
}
