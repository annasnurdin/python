class Kendaraan:
  merk = ""
  tahun = ""

  def __init__(self, merk, tahun):
    self.merk = merk
    self.tahun = tahun

  def info(self):
    return f"Merk: {self.merk} | Tahun: {self.tahun}"
  
  def nyalakan(self):
    print(f"{self.info()} dinyalakan")

class Mobil(Kendaraan): # apply class parent
  
  def __init__(self, merk, tahun, jumlah_roda):
    super().__init__(merk, tahun)
    self.jumlah_roda = jumlah_roda

  def klakson(self):
    print(f"Mobil {self.info()} punya klakson") # self ini sudah termasuk method di parentnya
  
xenia = Mobil("Xenia", "2019", 4)
xenia.klakson()
print(xenia.jumlah_roda)