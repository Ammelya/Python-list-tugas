Python-list-dasar

Program menampilkan Data dan NIlai Mahasiswa dengan ketentuan :

> Ketentuan nilai : tugas : 30%, uts : 35%, uas : 35%
> Input pada program ini adalah : Nama, NIM, Nilai Tugas, Nilai UTS, Nilai UAS, dan Nilai Akhir.
> Untuk ketentuan nilai akhir dihitung dari perhitungan semua nilai yang meliputi NIlai Tugas + Nilai UTS + Nilai UAS.
> Tampilkan Table Nilai Mahasiswa

Langkah pertama untuk membuat dan menampilkan data dan Tabel Nilai Mahasiswa adalah alangkah baiknya kita harus menginstall lebih dahulu  Package (PIP) dan module Texttable. Dapat di download pada \\https://pypi.python.org/pypi/texttable/0.8.4.
Fungsinya adalah agar kita dapat membuat output Tabel kita dengan rapi dan sesuai dengan inputan kita.

Setelah kita menginstall package dan Texttable itu artinya kita sudah bisa menggunakan library texttable dan dapat menginport texttable dari modul texttable pada text editor IDLE kita.
1. Import module Textbale pada text editor IDLE seperti berikut :

    from texttable import Texttable
    table = Texttable()
Dan jika saat kita run tidak terjadi error, itu artinya module Texttable sudah terinstall dan dapat difungsikan.

2. Membuat list dengan menggunakan simbol []

  jawab = "y"
   no = 0
  nm = []
  nim = []
  tgs = []
  uts = []
  uas = []

  Fungsi dari list diatas adalah untuk mendeklarasikan elemen yang akan kita gunakan pada saat mendeklarasikan perintah berikutnya.

3. Membuat perulangan yaitu dengan perulangan "While" artinya adalah perintah untuk mengulang perintah dengan jawaban "Yes" or "No".
    while (jawab == "y"):
    
      nm.append(input("Masukan Nama\t : "))
      nim.append(input("Masukan NIM\t : "))
      tgs.append(input("Nilai Tugas\t : "))
      uts.append(input("Nilai UTS\t : "))
      uas.append(input("Nilai UAS\t : "))
      jawab = input("Tambah Data (y/t)?")
      no+=1
      
Fungsi dari "append()" adalah untuk menambahkan sebuah item yang akan kita input dari belakang.

4. Lalu kita menggunakan perintah "for" fungsinya adalah sama dengan "While" yaitu sebagai sebuah perulangan. Tujuan utamanya adalah agar kita tidak perlu menuliskan perintah yang sama berulang-ulang. Dan kita dapat melakukan perulangan sesuai dengan range yang kita tentukan.

for i in range(no):
    tugas = int(tgs[i])
    n_uts = int(uts[i])
    n_uas = int(uas[i])
    akhir = (tugas*30/100) + (n_uts*35/100) + (n_uas*35/100)
    
5. Kemudian kita menuliskan sebuah perintah untuk menambahkan baris pada tabel yang kita butuhk dengan cara :

  table.add_rows([['No','Nama','NIM','TUGAS','UTS','UAS','AKHIR'],[i+1,nm [i],nim [i],tgs [i],uts [i],uas [i],akhir]])

  Untuk mengatur width tabel dapat menggunakan perintah :

  table.set_cols_width([2,15,15,5,5,5,5])

Hasil Output Tabel nilai dari program ini adalah dengan menggunakan module "Texttable". Untuk program yang digunakan adalah dengan Python 3.6 dengan OS Windows 10.
