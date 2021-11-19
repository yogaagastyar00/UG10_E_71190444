suhu_tubuh=float(input("Masukkan suhu tubuh Anda :"));
suhu=50
if suhu_tubuh > suhu:
    print("Anda bukan Manusia :)");
elif suhu_tubuh <= 32:
    print("Anda kedinginan! Silahkan cari sesuatu yang hangat!");
elif suhu_tubuh <= 37.5:
    print("Suhu Anda normal!");
elif suhu_tubuh == 36:
    print("Suhu Anda normal!");
else:
    print("Anda demam! Jangan berpergian ke tempat fasilitas Umum.")
