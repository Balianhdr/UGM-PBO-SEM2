class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi  

    def luas(self):
        return self.sisi ** 2

    def keliling(self):
        return 4 * self.sisi

sisi_persegi = input("Masukkan panjang sisi persegi: ")

if sisi_persegi.replace('.', '', 1).isdigit() and float(sisi_persegi) >= 0:
    sisi_persegi = float(sisi_persegi)

    persegi1 = Persegi(sisi_persegi)

    print(f"Luas persegi dengan sisi {sisi_persegi} adalah: {persegi1.luas()}")
    print(f"Keliling persegi dengan sisi {sisi_persegi} adalah: {persegi1.keliling()}")
else:
    print("Input tidak valid. Pastikan Anda memasukkan angka positif.")
