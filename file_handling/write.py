print(" == membuat file baru == ")

file = open("daftar_nama.txt", "w")

while True:
  nama = input("Masukkan nama: ")
  if nama == "":
    break

  file.write(nama + "\n")
  print(nama, " berhasil disimpan")

file.close()
print("file daftar_nama.txt sudah selesai dibuat")