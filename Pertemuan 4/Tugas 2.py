class Orang:
    def __init__(self, nama_depan, nama_belakang, nomer_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomer_id = nomer_id

    def tampilkan_info(self):
        print("Nama Depan:", self.nama_depan)
        print("Nama Belakang:", self.nama_belakang)
        print("Nomor ID:", self.nomer_id)

class Mahasiswa(Orang):
    SARJANA = "Sarjana"
    MASTER = "Master"
    DOKTOR = "Doktor"

    def __init__(self, nama_depan, nama_belakang, nomer_id, jenjang):
        super().__init__(nama_depan, nama_belakang, nomer_id)
        self.jenjang = jenjang
        self.matkul = []

    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Jenjang:", self.jenjang)
        print("Mata Kuliah:", ", ".join(self.matkul))
