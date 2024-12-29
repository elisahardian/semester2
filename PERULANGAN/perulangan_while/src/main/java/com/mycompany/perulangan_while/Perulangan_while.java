
package com.mycompany.perulangan_while;


public class Perulangan_while {

    public static void main(String[] args) {
        int i = 0;
        while (i<5)
        {
            System.out.println("pengulangan ke-"+i);
            i = i + 1;
        }
    }
}

//OUTPUT : akan mengulang sebanyak 5 kali, dari angka 0 sebagai nilai awal(i=0), sampai angka 4 terakhir, karena yang i<5
// dengan pencacahan +1, setiap perulangan nilai ditambah 1, i=i+1