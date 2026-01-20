trying = 1
secret_number = 0
limit = 3

while trying <= limit:
  input_num = int(input("Tebak Angka: "))

  if secret_number == input_num:
    print("Done: ", secret_number)
    break # menutup perulangan
  
  trying += 1
