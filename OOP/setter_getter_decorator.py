class Produk:
  _name = ""

  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, name):
    if name == "":
      raise ValueError("Nama tidak boleh kosong")
    self._name = name
  
produk1 = Produk()
produk1.name = "Laptops"
print(produk1.name)