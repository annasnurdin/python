class BankAccount:
  __no = ""
  __saldo = 0

  def __init__(self, no):
    self.__no = no
  
  def get_balance(self):
    return self.__saldo
  
  def topup(self, amount):
    self.__saldo += amount
  
  def cashout(self, amount):
    if amount > self.__saldo:
      raise ValueError("Saldo tidak mencukupi")
    self.__saldo -= amount

akun_annas = BankAccount("idAnnas")
akun_annas.topup(10000)
print(f"Saldo: {akun_annas.get_balance()}")
akun_annas.cashout(1000)
print(f"Saldo: {akun_annas.get_balance()}")
