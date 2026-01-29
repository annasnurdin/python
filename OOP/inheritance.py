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
  def klakson(self):
    print(f"Mobil {self.info()} punya klakson") # self ini sudah termasuk method di parentnya


xenia = Mobil("Xenia", "2019")
xenia.klakson()