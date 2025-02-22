class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def tampilkan_info(self):
        print(f"Nama: {self.nama}, Umur: {self.umur} tahun")

def main():
    nama = input("Masukkan nama: ")
    umur = input("Masukkan umur: ")
    manusia = Manusia(nama, umur)
    manusia.tampilkan_info()

if __name__ == "__main__":
    main()
