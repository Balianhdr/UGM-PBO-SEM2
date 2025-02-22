class Tas:
    def __init__(self, nama, ukuran, warna, harga):
        self.nama = nama
        self.ukuran = ukuran
        self.warna = warna
        self.harga = harga

    def deskripsi(self):
        return f"Tas: {self.nama}, Ukuran: {self.ukuran}, Warna: {self.warna}, Harga: Rp{self.harga}"

tas1 = Tas("Ransel Sekolah", "Medium", "Merah", 200000)
tas2 = Tas("Tas Laptop", "Large", "Hitam", 350000)

print(tas1.deskripsi())
print(tas2.deskripsi())
