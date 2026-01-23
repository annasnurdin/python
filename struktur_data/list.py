kosong = []
print(kosong)

angka = [1,2,3,4] # index dari 0
print(angka)

nama = ["annas", "purwo", "karin"]
print(nama)
print(nama[0])
nama[0] = "nurdin"
print(nama[0])
nama.append("annas")
nama.remove("purwo")
print(nama)
print(len(nama))

for i in range(len(nama)):
  print(str(i), f"- {nama[i]}")
mix = [1,"annas", 2, True]
print(mix)
mix.pop()
print(mix)