// OVERRIDING = METHOD SAMA, PARAMETER SAMA, BEDA DALAM PENGIMPLEMENTASIANNYA/PERNYATAANNYA. BERKAITAN DGN PEWARISAN

package com.mycompany.latnama_overriding;


public class Latnama_overriding {

    public static void main(String[] args) {
        //instansiasi kelas menjadi objek
        clsnamapanggilan_overriding obj_panggilan = new clsnamapanggilan_overriding();
        clsnamaasli_overriding obj_namaasli = new clsnamaasli_overriding();
        //memanggil method Namanya() pada kelas clsnamapanggilan_overriding
        obj_panggilan.Namanya();
        //memanggil method Namanya() pada kelas clsnamaasli_overriding
        obj_namaasli.Namanya();
        
    }
}
