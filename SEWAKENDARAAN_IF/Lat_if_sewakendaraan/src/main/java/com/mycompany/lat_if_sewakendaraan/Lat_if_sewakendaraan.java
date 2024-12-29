//INI MAIN PROGRAM. PRIVATE, FUNGSI, NON PARAM

package com.mycompany.lat_if_sewakendaraan;
import java.util.Scanner;

public class Lat_if_sewakendaraan {

    public static void main(String[] args) {
        Scanner input = new Scanner (System.in);
        //instansiasi kelas menjadi objek
        cls_sewakendaraan objSewa = new cls_sewakendaraan();
        
        System.out.printf("masukkan id penyewa\t: ");
        objSewa.setIdpenyewa(input.nextLine());
        System.out.printf("masukkan nama\t: ");
        objSewa.setNama(input.nextLine());
        System.out.printf("masukkan alamat\t: ");
        objSewa.setAlamat(input.nextLine());
        System.out.printf("masukkan no ktp\t: ");
        objSewa.setNoktp(input.nextLine());
        System.out.printf("masukkan no telepon\t: ");
        objSewa.setNotelepon(input.nextLine());
        System.out.printf("masukkan jenis kendaraan\t: ");
        objSewa.setJeniskendaraan(input.nextLine());
        System.out.printf("masukkan no plat\t: ");
        objSewa.setNoplat(input.nextLine());
        System.out.printf("masukkan lama sewa\t: ");
        objSewa.setLamasewa(input.nextInt());
        System.out.printf("masukkan biaya sewa\t: ");
        objSewa.setBiayasewa(input.nextInt());
        
        System.out.print("\nTotal sewa\t: "+ objSewa.totalsewa());
        System.out.print("\nPotongan harga\t: "+ objSewa.potonganharga());
        System.out.print("\nPPN\t: "+ objSewa.ppn());
        System.out.print("\njumlah bayar\t: "+ objSewa.jumlahbayar());
        
    }
}

// LALU KERJAKAN LOOP YG LATIHAN MANDIRI