command = ""

while command != "stop":

  command = input("Masukkan perintah: ")
  
  if command == "stop":
    break
  if command != "+" and command != "*" and command != "/" and command != "-":
    print("Masukkan + - * / atau stop untuk berhenti")
    continue

  a = int(input("Angka pertama: "))
  b = int(input("Angka kedua: "))
  
  if command == "+":
    result = a + b
  elif command == "-": # pakai elif, kalau if semua, setiap baris if akan di cek
    result = a - b
  elif command == "*": # kalau pakai elif, ketika masuk di if-nya, program fokus disitu dan loncat ke bawah 
    result = a * b
  else:
    result = a / b
  
  print(f"Result = {result}")

print("End Program")