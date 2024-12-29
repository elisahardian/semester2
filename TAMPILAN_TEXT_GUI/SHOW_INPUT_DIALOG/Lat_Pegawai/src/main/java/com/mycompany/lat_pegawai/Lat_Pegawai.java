//ini main program
package com.mycompany.lat_pegawai;
import javax.swing.JOptionPane;

public class Lat_Pegawai {

    public static void main(String[] args) {
        //membuat objek
        Pegawai objPegawai = new Pegawai();
        //membuat kotak dialog dengan showInputDialog()
        objPegawai.idPegawai = JOptionPane.showInputDialog("Id Pegawai: ");
        objPegawai.nama = JOptionPane.showInputDialog("Nama Pegawai: ");
        String mGaji = JOptionPane.showInputDialog("Gaji: ");
        objPegawai.gaji = Integer.parseInt(mGaji);
        
        //menampilkan data
        
        JOptionPane.showMessageDialog(null, "Id Pegawai: " + objPegawai.idPegawai + "\nNama Pegawai: " +objPegawai.nama + "\nGaji: " + mGaji + "\nTunjangan: " + objPegawai.tunjangan() + "\nTotal Gaji: " + objPegawai.totalGaji());
        
        }
    }
