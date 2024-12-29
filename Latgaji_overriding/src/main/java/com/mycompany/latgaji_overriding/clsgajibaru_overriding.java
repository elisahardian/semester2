
package com.mycompany.latgaji_overriding;


public class clsgajibaru_overriding extends clsgajilama_overriding { // JANGAN LUPA DI EXTENDS
    //method tunjangan dengan gaji baru
    @Override
    public void tunjangan()
    {
        int gaji = 15000000;
        System.out.println("tunjangan baru: "+ gaji*10/100);
    }
}
