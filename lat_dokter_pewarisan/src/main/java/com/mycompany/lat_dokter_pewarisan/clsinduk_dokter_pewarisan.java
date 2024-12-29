
package com.mycompany.lat_dokter_pewarisan;


public class clsinduk_dokter_pewarisan {
    //deklarasi atribut
    private String id;
    private String nama;
    private int gaji;
    
    //property method
    public void setId(String id)
    {
        this.id=id;
    }
    public String getId()
    {
        return id;
    }
    public void setNama(String nama)
    {
        this.nama = nama;
    }
    public String getNama()
    {
        return nama;
    }
    public void setGaji(int gaji)
    {
        this.gaji = gaji;
    }
    public int getGaji()
    {
        return gaji;
    }
    
    //method tunjangan
    public float tunjangan (int gaji)
    {
        return this.gaji/100*10;
    }
}
