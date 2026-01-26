class Rekening:
  id = 0
  saldo = 0

  def __init__(self, id, saldo = 0):
    if saldo < 0:
      raise ValueError("Saldo tidak boleh kurang dari 0")
    self.id = id
    self.saldo = saldo

annas = Rekening(123, 0)
# purwo = Rekening(1212, -5) // ini error
