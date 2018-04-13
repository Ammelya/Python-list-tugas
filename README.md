# Python-list-dasar

##Menampilkan program Data Mahasiswa, seperti :
<ol>
   <li><b> Nama Mahasiswa </b></li>
   <li><b> NIM </b></li>
   <li><b> Nilai Tugas </b></li>
   <li><b> Nilai UTS </b></li>
   <li><b> Nilai UAS </b></li>
   <li>dan <b>Nilai Akhir Mahasiswa</b></li>
   <li>Menampilkan dalam bentuk <b> Tabel</b></li>
    <ol>Hasil Output Tabel nilai dari program ini adalah dengan menggunakan module "Texttable".</ol>
    <ol>Untuk program yang digunakan adalah dengan Python 3.6 dengan OS Windows 10.</ol>
</ol>
<hr/>

<ol>Untuk ketentuan nilai akhir dihitung dari perhitungan semua nilai yang meliputi NIlai Tugas + Nilai UTS + Nilai UAS.</ol>

# Langkah untuk membuat program Data Mahasiswa ini adalah sebagai berikut :
<ol>
   <li><b> Pertama : </b> Install lebih dahulu program Python :<b> https://www.python.org/</b></li>
   <li><b> Kedua : </b> Install PIP (Package) dan module Texttable</li>
   <li><b> Ketiga : </b> Buatlah file : python.py yang berisi program tentang Data Mahasiswa</li>
   <li><b> Keempat </b> Untuk menampilkan Data dalam bentuk Tabel : maka jangan lupa untuk menggunakan module :Texttable pada file :python.py yang kita buat</li>
   <li><b> Jalankan file : python.py yang sudah dibuat </b></li>
</ol>
<hr/>


>Setelah kita menginstall package dan Texttable itu artinya kita sudah bisa menggunakan library texttable dan dapat mengiport texttable dari modul texttable pada text editor IDLE kita.
<o1>
<li>1. Import module Textbale pada text editor IDLE seperti berikut :</li>

    from texttable import Texttable
    table = Texttable()
    
    Dan jika saat kita run tidak terjadi error, itu artinya module Texttable sudah terinstall dan dapat difungsikan.

<li>2. Membuat list dengan menggunakan simbol []</li>
    
    jawab = "y"
    no = 0
    nm = []
    nim = []
    tgs = []
    uts = []
    uas = []

    Fungsi dari list diatas adalah untuk mendeklarasikan elemen yang akan kita gunakan pada saat mendeklarasikan perintah berikutnya.

<li>3. Membuat perulangan yaitu dengan perulangan "While" artinya adalah perintah untuk mengulang perintah dengan jawaban "Yes" or "No".
    while (jawab == "y"):</li>
    
      nm.append(input("Masukan Nama\t : "))
      nim.append(input("Masukan NIM\t : "))
      tgs.append(input("Nilai Tugas\t : "))
      uts.append(input("Nilai UTS\t : "))
      uas.append(input("Nilai UAS\t : "))
      jawab = input("Tambah Data (y/t)?")
      no+=1
      
    Fungsi dari "append()" adalah untuk menambahkan sebuah item yang akan kita input dari belakang.

<li>4. Lalu kita menggunakan perintah "for" fungsinya adalah sama dengan "While" yaitu sebagai sebuah perulangan. Tujuan utamanya adalah agar kita tidak perlu menuliskan perintah yang sama berulang-ulang. Dan kita dapat melakukan perulangan sesuai dengan range yang kita tentukan.</li>

    for i in range(no):
    tugas = int(tgs[i])
    n_uts = int(uts[i])
    n_uas = int(uas[i])
    akhir = (tugas*30/100) + (n_uts*35/100) + (n_uas*35/100)
    
<li>5. Kemudian kita menuliskan sebuah perintah untuk menambahkan baris pada tabel yang kita butuhk dengan cara :</li>

    table.add_rows([['No','Nama','NIM','TUGAS','UTS','UAS','AKHIR'],[i+1,nm [i],nim [i],tgs [i],uts [i],uas [i],akhir]])

    Untuk mengatur width tabel dapat menggunakan perintah :

    table.set_cols_width([2,15,15,5,5,5,5]
