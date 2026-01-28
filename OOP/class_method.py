class AkunBank:
  no = ""
  saldo = 0
  active = True

  def __init__(self, no, saldo):
    self.no = no
    self.saldo = saldo

  @classmethod
  def disabled(cls, no, balance = 0):
    result = cls(no, balance)
    result.active = False
    return result

akun1 = AkunBank("1", 1000)
akun2 = AkunBank.disabled("2", 3000)

print(f"Bank: {akun1.no}, saldo: {akun1.saldo}, status: {akun1.active}")
print(f"Bank: {akun2.no}, saldo: {akun2.saldo}, status: {akun2.active}")