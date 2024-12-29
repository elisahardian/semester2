//FUNGSI, PRIVATE, PARAMETER

//ini class
package com.mycompany.segitiga;
        
public class clssegitiga {
    //deklarasikan atribut private
    private int alas;
    private int tinggi;
    //propertu method set get
    public void setAlas(int alas)
    {
        this.alas=alas;
    }
    public int getAlas()
    {
        return alas;
    }        
    public void setTinggi(int tinggi)
    {
        this.tinggi=tinggi;
    }
    public int getTinggi()
    {
        return tinggi;
    }
    //buat method dengan fungsi dan dengan parameter
    public double luas(int alas, int tinggi)
    {
        return 0.5 * alas * tinggi;
    }
        
}
