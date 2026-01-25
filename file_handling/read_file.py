# fungsi read membaca seluruh file lalu disimpan dalam memory
# ini berbahaya karena kalau semakin filenya besar, semakin memakan memory

print(" == Menampilkan Nama Per Baris == ")

file = open("daftar_nama.txt", "r")

for line in file:
  data = line.strip() # ambil tiap baris
  print(data)

file.close()

print("== Selesai ==")