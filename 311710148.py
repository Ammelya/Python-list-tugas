from texttable import Texttable
table = Texttable()
jawab = "y"
no = 0
nm = []
nim = []
tgs = []
uts = []
uas = []

while (jawab == "y"):
    nm.append(input("Masukan Nama\t : "))
    nim.append(input("Masukan NIM\t : "))
    tgs.append(input("Nilai Tugas\t : "))
    uts.append(input("Nilai UTS\t : "))
    uas.append(input("Nilai UAS\t : "))
    jawab = input("Tambah Data (y/t)?")
    no+=1
    
for i in range(no):
    tugas = int(tgs[i])
    n_uts = int(uts[i])
    n_uas = int(uas[i])
    akhir = (tugas*30/100) + (n_uts*35/100) + (n_uas*35/100)

    table.add_rows([['No','Nama','NIM','TUGAS','UTS','UAS','AKHIR'],[i+1,nm [i],nim [i],tgs [i],uts [i],uas [i],akhir]])

    table.set_cols_width([2,15,15,5,5,5,5])
print (table.draw())
