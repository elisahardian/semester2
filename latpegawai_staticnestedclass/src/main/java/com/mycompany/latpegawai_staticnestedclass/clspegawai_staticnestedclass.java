
package com.mycompany.latpegawai_staticnestedclass;

//kelas luar / outer class
public class clspegawai_staticnestedclass {
    //kelas dalam / inner class
    static class Tetap
    {
        //mendeklarasikan atribut
        private String id;
        private String nama;
        int gaji;
        
        //property method
        public void setID(String id)
        {
            this.id = id;
        }
        public String getID()
        {
            return id;
        }
        public void setNama(String nama)
        {
            this.nama=nama;
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
    
        // membuat method
        public float tunjangan()
        {
            return getGaji()*10/100;
        }
        public float total()
        {
            return getGaji() + tunjangan();
        }
    
    }      // close inner class definition
}       // close top level class definition
