def hitung_keliling_luas(jari_jari):

  pi = 3.14
  keliling = 2 * pi * jari_jari
  luas = pi * jari_jari * jari_jari
  return keliling, luas

jari_jari = float(input("Masukkan jari-jari lingkaran: "))

keliling, luas = hitung_keliling_luas(jari_jari)

print("Keliling lingkaran:", keliling)
print("Luas lingkaran:", luas)
