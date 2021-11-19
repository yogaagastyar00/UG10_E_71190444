print("===== Kalkulator Akar dan Pangkat =====");
print("Pilihan menu :");
print("1. Pangkat 2 (Kuadrat)");
print("2. Pangkat 3 (Kuadrat)");
print("3. Akar Kuadrat");
masukan_menu=int(input("Masukkan menu yang anda pilih : "));
if masukan_menu == 1:
    bil=int(input("Masukkan bilangan yang ingin di pangkatkan : "));
    rumus=bil ** 2
    print("Hasil dari pemangkatan bilangan",bil,"dengan 2 (Kuadrat) adalah",rumus)
elif masukan_menu == 2:
    bil2=int(input("Masukkan bilangan yang ingin di pangkatkan : "));
    rumus2=bil2 ** 3
    print("Hasil dari pemangkatan bilangan",bil2,"dengan 3 (Kubik) adalah",rumus2)
elif masukan_menu == 3:
    bil3=int(input("Masukkan bilangan yang ingin di akarkan : "));
    rumus3= bil3 ** (1.0/2)
    print("Hasil akar kuadrat dari bilangan",bil3,"adalah",rumus3)
else:
    print("Pilihan menu yang dimasukkan tidak sesuai!")
