// LATIHAN DOKTER. PROSEDUR, PRIVATE, PARAMETER
//ini class

package com.mycompany.latdokter_oop_prosedur_private_param;

public class clsdokter_prosedur_private_param {
    //deklarasi atribut
    private String id;
    private String nama;
    private int gaji;
    //property method id
    public void setId(String newValue)
    {
        id = newValue;
    }
    public String getId()
    {
        return id;
    }    
    //property method nama
    public void setNama(String newValue)
    {
        nama = newValue;
    }
    public String getNama()
    {
        return nama;
    }       
    //property method gaji
    public void setGaji(int newValue)
    {
        gaji = newValue;
    }
    public int getGaji()
    {
        return gaji;
    }

    //membuat method dengan prosedur
    void tunjangan(int gaji) // void untuk menyatakan tidak memerlukan nilai balikan. menandakan prosedur
    //public void tunjangan(int gaji) //mau pake public sebelum void juga bisa. public untuk memberitahu bisa diakses secara public
    //static void tunjangan(int gaji) // jangan pake static. jika pake static objek tidak bisa diakhses ke main program
    {
        float tunjangan;
        tunjangan = gaji * 1 / 10;
        System.out.printf("Tunjangan\t: %.2f \n", tunjangan);
    }
    void total_gaji(int gaji) // void untuk menyatakan tidak memerlukan nilai balikan. menandakan prosedur
    //public void total_gaji(int gaji) //mau pake public sebelum void juga bisa. public untuk memberitahu bisa diakses secara public
    //static void total_gaji(int gaji)  //  jangan pake static. jika pake static objek tidak bisa diakhses ke main program
    {
        float total_gaji;
        total_gaji = (gaji * 1 / 10) + gaji;
        System.out.printf("Total Gaji\t: %.2f \n", total_gaji);
    }
}
