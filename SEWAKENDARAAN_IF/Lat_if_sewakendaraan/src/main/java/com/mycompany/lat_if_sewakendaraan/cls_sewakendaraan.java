// INI CLASS. PRIVATE, FUNGSI, NON PARAM

package com.mycompany.lat_if_sewakendaraan;

public class cls_sewakendaraan {
    //mendeklarasikan atribut
    private String idpenyewa;
    private String nama;
    private String alamat;
    private String noktp;
    private String notelepon;
    private String jeniskendaraan;
    private String noplat;
    private int lamasewa;
    private int biayasewa;
    //mengakses atribut dengan jangkauan nilai private
    //menggunakan property method
    public void setIdpenyewa(String idpenyewa)
    {
        this.idpenyewa = idpenyewa;
    }
    public String getIdpenyewa()
    {
        return idpenyewa;
    }
    public void setNama(String nama)
    {
        this.nama = nama;
    }
    public String getNama()
    {
        return nama;
    }
    public void setAlamat(String alamat)
    {
        this.alamat= alamat;
    }
    public String getAlamat()
    {
        return alamat;
    }
    public void setNoktp(String noktp)
    {
        this.noktp = noktp;
    }
    public String getNoktp()
    {
        return noktp;
    }
    public void setNotelepon(String notelepon)
    {
        this.notelepon = notelepon;
    }
    public String getNotelepon()
    {
        return notelepon;
    }
    public void setJeniskendaraan(String jeniskendaraan)
    {
        this.jeniskendaraan = jeniskendaraan;
    }
    public String getJeniskendaraan()
    {
        return jeniskendaraan;
    }
    public void setNoplat(String noplat)
    {
        this.noplat = noplat;
    }
    public String getNoplat()
    {
        return noplat;
    }
    public void setLamasewa(int lamasewa)
    {
        this.lamasewa = lamasewa;
    }
    public int getLamasewa()
    {
        return lamasewa;
    }
    public void setBiayasewa(int biayasewa)
    {
        this.biayasewa = biayasewa;
    }
    public int getBiayasewa()
    {
        return biayasewa;
    }
    
    
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

