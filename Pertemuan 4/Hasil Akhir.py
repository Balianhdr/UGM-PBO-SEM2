# Kelas Orang
class Orang:
    def __init__(self, nama_depan, nama_belakang, nomer_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomer_id = nomer_id

# Kelas Mahasiswa (turunan dari kelas Orang)
class Mahasiswa(Orang):
    class Jenjang:
        SARJANA = "SARJANA"
        MASTER = "MASTER"
        DOKTOR = "DOKTOR"

    def __init__(self, nama_depan, nama_belakang, nomer_id, jenjang):
        super().__init__(nama_depan, nama_belakang, nomer_id)
        self.jenjang = jenjang
        self.matkul = []

    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)

# Kelas Karyawan (turunan dari kelas Orang)
class Karyawan(Orang):
    class StatusKaryawan:
        TETAP = "TETAP"
        TDK_TETAP = "TDK_TETAP"

    def __init__(self, nama_depan, nama_belakang, nomer_id, status_karyawan):
        super().__init__(nama_depan, nama_belakang, nomer_id)
        self.status_karyawan = status_karyawan

# Kelas Dosen (turunan dari kelas Karyawan)
class Dosen(Karyawan):
    def __init__(self, nama_depan, nama_belakang, nomer_id, status_karyawan):
        super().__init__(nama_depan, nama_belakang, nomer_id, status_karyawan)
        self.matkul_diajar = []

    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)

# Membuat objek Mahasiswa
bowo = Mahasiswa("Bowo", "Nugroho", "987654", Mahasiswa.Jenjang.SARJANA)
bowo.enrol("Basis Data")

# Membuat objek Dosen
rizki = Dosen("Rizki", "Setiabudi", "456789", Karyawan.StatusKaryawan.TETAP)
rizki.mengajar("Statistik")

# Kelas Pelajar
class Pelajar:
    def __init__(self):
        self.matkul = []

    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)

# Kelas Pengajar
class Pengajar:
    def __init__(self):
        self.matkul_diajar = []

    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)

# Kelas Asdos (multiple inheritance)
class Asdos(Orang, Pelajar, Pengajar):
    def __init__(self, nama_depan, nama_belakang, nomer_id):
        Orang.__init__(self, nama_depan, nama_belakang, nomer_id)
        Pelajar.__init__(self)
        Pengajar.__init__(self)

# Membuat objek Asdos
uswatun = Asdos("Uswatun", "Hasanah", "456456")
uswatun.enrol("Big Data")
uswatun.mengajar("Kecerdasan Artifisial")

# Menampilkan hasil
print(f"Mahasiswa: {bowo.nama_depan} {bowo.nama_belakang}, ID: {bowo.nomer_id}, Jenjang: {bowo.jenjang}, Matkul: {bowo.matkul}")
print(f"Dosen: {rizki.nama_depan} {rizki.nama_belakang}, ID: {rizki.nomer_id}, Status: {rizki.status_karyawan}, Matkul Diajar: {rizki.matkul_diajar}")
print(f"Asdos: {uswatun.nama_depan} {uswatun.nama_belakang}, ID: {uswatun.nomer_id}, Matkul: {uswatun.matkul}, Matkul Diajar: {uswatun.matkul_diajar}")
