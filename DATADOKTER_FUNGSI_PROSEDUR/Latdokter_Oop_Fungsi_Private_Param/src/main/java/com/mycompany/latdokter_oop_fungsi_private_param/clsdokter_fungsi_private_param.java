// LATIHAN DOKTER. FUNGSI, PRIVATE, PARAMETER
//ini class

package com.mycompany.latdokter_oop_fungsi_private_param;

public class clsdokter_fungsi_private_param { //nama kelas yg ini akan diinstansiasi di main program menjadi objek 
    //deklarasi atribut
    private String id;
    private String nama;
    private int gaji;
    //membuat property method
    public void setId(String id)
    {
        this.id = id;
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
    
    //membuat method dengan fungsi
    public double tunjangan(int gaji)
    {
        return 0.1 * gaji;
    }
    public double total_gaji(int gaji)
    {
        return (0.1 * gaji) + gaji;
    }
    
}
