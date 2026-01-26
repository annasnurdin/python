class Mahasiswa:
  nim = 0
  nama = ""

  def __init__(self, nama, nim): # constructor: fungsi awal yang otomatis dijalankan
    self.nama = nama
    self.nim = nim
  
  def __str__(self):
    return f"Mahasiswa: {self.nama} + {self.nim}"


mahasiswa = Mahasiswa("Annas", 123)
print(mahasiswa.nim)
print(mahasiswa.nama)

print(mahasiswa)