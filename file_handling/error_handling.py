print(" == Menampilkan Nama Per Baris == ")

try:
  with open("404_not_found.txt", "r") as file:
    for line in file:
      data = line.strip()
      print(data)
except FileNotFoundError:
  print("File tidak ditemukan")


print("== Selesai ==")