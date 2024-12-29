//INI MAIN PROGRAM. PUBLIC, FUNGSI, NON PARAM

package com.mycompany.lat_sewakendaraan_if;
import java.util.Scanner;

public class Lat_sewakendaraan_if {

    public static void main(String[] args) {
        //membuat scanner
        Scanner input= new Scanner (System.in);
        //membuat objek
        cls_sewakendaraan objSewakendaraan = new cls_sewakendaraan();
        System.out.println("<<masukkan data>>");
        System.out.print("ID penyewa\t: ");
        objSewakendaraan.idPenyewa = input.nextLine();
        System.out.print("nama pegawai\t: ");
        objSewakendaraan.nama = input.nextLine();
        System.out.print("alamat\t: ");
        objSewakendaraan.alamat = input.nextLine();
        System.out.print("no ktp\t: ");
        objSewakendaraan.noktp = input.nextLine();
        System.out.print("no telepon\t: ");
        objSewakendaraan.notelp = input.nextLine();
        System.out.print("jenis kendaraan\t: ");
        objSewakendaraan.jeniskendaraan = input.nextLine();
        System.out.print("no plat\t: ");
        objSewakendaraan.noplat = input.nextLine();
        System.out.print("lama sewa\t: ");
        objSewakendaraan.lamasewa = input.nextInt();
        System.out.print("biaya sewa\t: ");
        objSewakendaraan.biayasewa = input.nextInt();
        
        //menampilkan data
        System.out.println("Total sewa\t: " + objSewakendaraan.totalsewa());
        System.out.println("Potongan harga\t: " + objSewakendaraan.potonganharga());
        System.out.println("Ppn\t: " + objSewakendaraan.ppn());
        System.out.println("Jumlah bayar\t: " + objSewakendaraan.jumlahbayar());

    }
}
