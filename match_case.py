hari = input("Masukkan hari: ").lower()

match hari:
  case "senin" | "selasa" | "rabu" | "kamis" | "jumat":
    print("Working")
  case "sabtu" | "minggu":
    print("Hari Libur")
  case _: # untuk karakter atau inputan yang lain
    print("Hari tidak valid!")