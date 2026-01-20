first_name = "Annas"
last_name = "Nurdin"

full_name = first_name + " [" + last_name + "]"
print(full_name)

uppercase_name = full_name.upper()
print(uppercase_name)

full_name = f"{first_name} [{last_name}]" # bisa format seperti ini
print(full_name)

umur = 21
pesan = f"Umur kamu: {umur}" # auto conversion to string

print(pesan)