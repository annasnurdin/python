# fungsi open harus di close. kalau ada error di tengah jalan, file open tidak ter close
# cara yang aman menggunakan with statement

print(" == Menampilkan Nama Per Baris == ")

with open("daftar_nama.txt", "r") as file:
  for line in file:
    data = line.strip() # ambil tiap baris
    print(data)

print("== Selesai ==")