class Motor:
    def suara(self):
        return "Brrrmm"

class Mobil:
    def suara(self):
        return "Vroom Vroom"

def suara_kendaraan(kendaraan):
    print(kendaraan.suara())

motor = Motor()
mobil = Mobil()

suara_kendaraan(motor)  
suara_kendaraan(mobil)  
