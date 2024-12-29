// OVERLOADING. NAMA METHOD SAMA DIBEDAKAN OLEH PARAMETER

package com.mycompany.lathitung_overloading;

public class clshitung_overloading {
    //membuat method fungsi
    public double hasil(int a, int b)
    {
        return a+b;
    }        
    public double hasil(double a, int b, int c)
    {
        return a+b*c;
    }
    public double hasil(int a, double b, int c, int d)
    {
        return a+b+c+d;
    }
}
