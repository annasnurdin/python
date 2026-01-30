class Hewan:

  def __init__(self, nama):
    self.nama = nama
  
  def suara(self):
    return "Suara Hewan"
  
class Anjing(Hewan):
  def suara(self):
    return "Asuuuuw"

class Kucing(Hewan):
  def suara(self):
    return "Meyong"

class Sapi(Hewan):
  def suara(self):
    return "Emooh"

list_hewan = [
  Anjing("Purwo"),
  Kucing("Karin"),
  Sapi("Annas")
]

for hewan in list_hewan:
  print(hewan.suara())

