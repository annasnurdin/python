angka_tebakan = 9

while True:
  tebakan = int(input("Tebak: "))
  if tebakan == angka_tebakan:
    print("Benar")
    break # untuk menghentikan perulangan while nya
  else:
    print("Salah, coba lagi!")