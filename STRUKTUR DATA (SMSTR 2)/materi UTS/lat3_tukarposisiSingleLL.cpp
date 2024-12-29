//TUKAR POSISI BERDASARKAN INPUTAN USER

#include <iostream>
#include <vector>

using namespace std;

int main() {
    //List awal
    vector <int> my_list = {42, 57, 23, 51};
    
    //menampilkan list saat ini
    cout <<"list saat ini: ";
    for (int x : my_list) {
        cout <<x <<" ";
    }
    cout<< endl;
    
    //Meminta input dari pengguna
    int pos1, pos2;
    cout<<"masukkan posisi elemen pertama yang akan ditukar (0-based): ";
    cin >> pos1;
    cout<<"masukkan posisi elemen kedua yang akan ditukar (0-based): ";
    cin >> pos2;
    
    //validasi input posisi
    if (pos1 < 0 || pos1 >= my_list.size() || pos2 < 0 || pos2 >= my_list.size()) {
        cout <<"Posisi yang dimasukkan tidak valid." <<endl;
        return 1;
    }
    
    //Menukar posisi elemen
    swap(my_list[pos1], my_list[pos2]);
    
    //Menampilkan list setelah ditukar
    cout<<"List setelah ditukar: ";
    for (int x : my_list){
        cout << x <<" ";
    }
    cout << endl;
    
    return 0;
}