class Mahasiswa:
  nama = ""
  nim = 0

  def perkenalan(self): # self untuk memanggil atribut dirinya sendiri
    print(f"hellow, saya {self.nama}")

  def sapa(self, nama):
    print(f"halo {nama}, aku {self.nama}")

mahasiswa = Mahasiswa()
mahasiswa.nama = "Annas"
mahasiswa.perkenalan()
mahasiswa.sapa("Purwo")