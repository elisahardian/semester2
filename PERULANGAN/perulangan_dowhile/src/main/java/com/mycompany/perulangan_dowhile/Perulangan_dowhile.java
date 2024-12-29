
package com.mycompany.perulangan_dowhile;

public class Perulangan_dowhile {

    public static void main(String[] args) {
        int i = 0;
        do
        {
            System.out.println("pengulangan ke- "+ i);
            i = i+1;
        }
        while (i<5);
    }
}

// do while akan melakukan terlebih dahulu, lalu mencek apakah memenuhi persyaratan atau tidak
//OUTPUT : akan mengulang sebanyak 5 kali, dari angka 0 sebagai nilai awal(i=0), sampai angka 4 terakhir, karena yang i<5
// dengan pencacahan +1, setiap perulangan nilai ditambah 1, i=i+1