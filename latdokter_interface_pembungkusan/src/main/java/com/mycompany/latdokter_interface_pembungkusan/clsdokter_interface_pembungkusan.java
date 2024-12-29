
package com.mycompany.latdokter_interface_pembungkusan;


public class clsdokter_interface_pembungkusan implements interfacedokter_interface_pembungkusan { // jangan lupa diimplements
    // atribut
    public String id;
    public String nama;
    public int gaji;
    
    @Override
    public double tunjangan(int mGaji)
    {
        return mGaji/100*10;
    }
    @Override
    public double total_gaji(int mGaji, double mTunjangan)
    {
        return mGaji + tunjangan(mGaji);
    }
    
}
