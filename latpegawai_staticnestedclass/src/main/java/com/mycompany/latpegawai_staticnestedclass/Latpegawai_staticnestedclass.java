
package com.mycompany.latpegawai_staticnestedclass;


public class Latpegawai_staticnestedclass {

    public static void main(String[] args) {
        //instansiasi kelas dalam
        clspegawai_staticnestedclass.Tetap objPeg = new clspegawai_staticnestedclass.Tetap();
        
        //memasukkan nilai
        objPeg.setID("22222");
        objPeg.setNama("Reny");
        objPeg.setGaji(15000000);
        
        //mencetak nilai
        System.out.println("ID: "+ objPeg.getID());
        System.out.println("Nama: "+ objPeg.getNama());
        System.out.println("Gaji: "+ objPeg.getGaji());
        System.out.println("Tunjangan: "+ objPeg.tunjangan());
        System.out.printf("Total: %.2f\n ", objPeg.total());
        
    }
}
