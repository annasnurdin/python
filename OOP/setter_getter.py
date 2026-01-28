class Produk:
  _name = ""

  def set_name(self, name):
    if name == "":
      raise ValueError("Nama tidak boleh kosong")
    self._name = name
  
  def get_name(self):
    return self._name
  
produk1 = Produk()
produk1.set_name("TV LED")
print(produk1.get_name())