niu = input("Masukkan NIU (6 digit): ")
nilai_tugas = float(input("Masukkan nilai tugas: "))
nilai_laporan = float(input("Masukkan nilai laporan: "))
rata_rata = (nilai_tugas + nilai_laporan) / 2
print(f"Rata-rata nilai tugas dan laporan: {rata_rata}")

if rata_rata < 40:
    print("Nilai akhir: K (Rata-rata di bawah 40)")
else:
    nilai_ujian = float(input("Masukkan nilai ujian: "))
    
    nilai_akhir = (nilai_tugas * 0.25) + (nilai_laporan * 0.25) + (nilai_ujian * 0.5)
    print(f"Nilai akhir: {nilai_akhir}")

    if 80 <= nilai_akhir <= 100:
        print("Nilai huruf: A")
    elif 70 <= nilai_akhir < 80:
        print("Nilai huruf: B")
    elif 60 <= nilai_akhir < 70:
        print("Nilai huruf: C")
    elif 50 <= nilai_akhir < 60:
        print("Nilai huruf: D")
    else:
        print("Nilai huruf: E")
