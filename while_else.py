password = "123"
percobaan = 0
max_percobaan = 3

while percobaan < max_percobaan:
  password_user = input("Masukkan password: ")
  percobaan += 1

  if password_user == password:
    print("Login berhasil")
    break
  else: 
    print(f"Password salah! Percobaan tersisa: {max_percobaan - percobaan}")
else:
  print("Terlalu banyak percobaan")

