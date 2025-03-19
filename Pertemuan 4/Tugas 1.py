class Orang:
    def __init__(self, nama_depan, nama_belakang, nomer_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomer_id = nomer_id

    def tampilkan_info(self):
        print("Nama Depan:", self.nama_depan)
        print("Nama Belakang:", self.nama_belakang)
        print("Nomor ID:", self.nomer_id)
