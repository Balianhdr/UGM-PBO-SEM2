class Kendaraan:
    def bergerak(self):
        pass  

class Motor(Kendaraan):
    def bergerak(self):
        return "Motor berjalan di jalan raya dengan dua roda."

class Mobil(Kendaraan):
    def bergerak(self):
        return "Mobil melaju di jalan dengan empat roda."

def jalankan_kendaraan(kendaraan):
    print(kendaraan.bergerak())

motor = Motor()
mobil = Mobil()

jalankan_kendaraan(motor)
jalankan_kendaraan(mobil)
