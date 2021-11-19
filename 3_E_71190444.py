masuk_daftar_nama=str(input("Masukkan daftar siswa :"));
daftar_nama1=[]
kata_depan_besar2=masuk_daftar_nama.title()
daftar_nama1.append(kata_depan_besar2)
print("Daftar Siswa : ",daftar_nama1)
masuk_siswa_ditambah=str(input("Masukkan siswa yang ingin ditambahkan :"));
sinta= 'SINTA'
nama = 12
kata_besar= masuk_siswa_ditambah.upper()
kata_depan_besar=masuk_daftar_nama.title()
if kata_besar == sinta:
    print("Siswa atas nama",kata_besar,"sudah berada dalam daftar siswa")
elif nama == 12:
    daftar_nama=[]
    daftar_nama.append(kata_depan_besar)
    daftar_nama.append(kata_besar)
    print("Hasil penambahan pada daftar siswa : ",daftar_nama)
