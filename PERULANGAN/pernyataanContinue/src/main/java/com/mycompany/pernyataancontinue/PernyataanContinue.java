
package com.mycompany.pernyataancontinue;

public class PernyataanContinue {

    public static void main(String[] args) {
        int i;
        for (i=0; i<10 ; i++)
        {
            if (i==5)
                continue;
                System.out.println("pengulangan ke-" + i);
        }
    }
}

// OUTPUT: akan muncul angka 0 sampai 9,tapi angka 5 tidak ada. dimulai dari angka 0 (i=0), sampai angka 9 (i<10),
// tapi karena ada continue pada i == 5 maka tidak dilanjutkan tahap selanjutnya yaitu system.out.println,
// sehingga angka 5 tersebut belum di print tapi sudah harus memulai dari awal lagi (tahap yg print di skip, langsung mulai dari awal lagi)
