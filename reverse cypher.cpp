#include <iostream>
#include <string>

using namespace std;

int main() {
    string pesan;
    getline(cin, pesan);
    cout << "Masukkan pesan: " << pesan << endl;
    cout << "" << endl;

    int ckey;
    cin >> ckey;
    cout << "Masukkan Key Caesar Cipher: " << ckey << endl;
    cout << "" << endl;

    cout << "Hasil Enkripsi dengan Reverse Cipher: ";
    int indeks = pesan.length() - 1;
    while (indeks >= 0) {
        cout << pesan[indeks];
        indeks-=1;
    }
}
