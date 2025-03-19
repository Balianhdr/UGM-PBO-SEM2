class Motor:
    def __init__(self, merek, kecepatan):
        self.merek = merek
        self.kecepatan = kecepatan

    def __add__(self, motor_lain):
        return Motor(f"{self.merek} & {motor_lain.merek}", self.kecepatan + motor_lain.kecepatan)

    def __str__(self):
        return f"{self.merek} (Kecepatan: {self.kecepatan} km/jam)"

motor1 = Motor("Honda", 80)
motor2 = Motor("Yamaha", 90)
motor3 = motor1 + motor2
print(motor3)
