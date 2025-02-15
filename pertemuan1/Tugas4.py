def is_prima(angka):

  if angka <= 1:
    return False
  for i in range(2, int(angka**0.5) + 1):
    if angka % i == 0:
      return False
  return True

bilangan = int(input("Masukkan bilangan: "))

if is_prima(bilangan):
  print(bilangan, "adalah bilangan prima")
else:
  print(bilangan, "bukan bilangan prima")
