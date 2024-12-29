
package com.mycompany.lat_dokter_pewarisan;


public class cls_spesialis_pewarisan extends clsinduk_dokter_pewarisan {
    //deklarasi atriuut
    private int tunSpesialis;
    
    //membuat property method
    public void setTunSpesialis(int tunSpesialis)
    {
        this.tunSpesialis = tunSpesialis;
    }
    public int getTunSpesialis()
    {
        return tunSpesialis;
    }
    
    //membuta method
    public float uang_makan (int gaji)
    {
        return gaji/100 * 10;
    }
    public double total_gaji (int gaji, float tunjangan, float tunSpesialis, float uangMakan)
    {
        return gaji + tunjangan + tunSpesialis + uangMakan;
    }
    
}
