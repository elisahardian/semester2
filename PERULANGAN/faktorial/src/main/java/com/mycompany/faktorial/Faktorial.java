/*
package com.mycompany.faktorial;

public class Faktorial {

    public static void main(String[] args) {
        long batas = 10;
        long mfaktorial = 1;
        for (int i = 0 ; i <= batas ; i++)
        {
            mfaktorial = 1;
            for (int faktor = 2 ; faktor <= i ; faktor++ )
                mfaktorial *= faktor;
                System.out.println(i + "! adalah " + mfaktorial);
        }
    }
}

*/

/*
// FAKTORIAL ITERATIF

package com.mycompany.faktorial;
import java.util.Scanner;

public class Faktorial {

    public static void main(String[] args) 
    {   
        int n;
        Scanner input = new Scanner(System.in);
        System.out.print("masukkan bilangan: ");
        n = input.nextInt();
        cari_faktorial(n);
    }
    
    //prosedur menghitung faktorial
    static void cari_faktorial(int n)
    {
        int faktorial=1;
        for (int x=n ; x>=1; x--)
        {
            faktorial = x*faktorial;
        }
        System.out.println(n+"! adalah "+ faktorial);
    }
}
*/



// FAKTORIAL REKURSIF

package com.mycompany.faktorial;
import java.util.Scanner;

public class Faktorial {

    public static void main(String[] args) 
    {
        int n_bilangan, n;
        Scanner input = new Scanner (System.in);
        System.out.print("Masukkan bilangan: ");
        n_bilangan = input.nextInt();
        n = faktorial(n_bilangan);
        System.out.println(n_bilangan + "! adalah " + n);   
    }    
    
    //fungsi menghitung faktorial
    static int faktorial(int n)
    {
        if (n==0)
        {
            return 1;
        }
        return n * faktorial(n-1);
    }
    
}


