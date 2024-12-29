
package com.mycompany.pernyataanbreak;

public class PernyataanBreak {

    public static void main(String[] args) {
        int i;
        for (i=0; i<10; i++)
        {
            System.out.println("pengulangan ke-"+i);
            if (i==5)
                break;
        }
    }
}

// OUTPUT: akan muncul nilai 0 sampai 5, karena, dimulai dari angka 0 (i=0), sampai angka 9 (i<10),
// tapi karena ada break pada i == 5 maka tidak dilanjutkan programnya dan selesai sampai di i = 5 saja