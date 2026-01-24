def cetak_list(*inilist): # ini jadi bertipe list
  for item in inilist:
    print(item)

cetak_list(1,2,3,4,"annas", "purwo")

def cetak_dict(**dictionary):
  for key, value in dictionary.items():
    print(key, value)

cetak_dict(nama = "Annas", umur = "25")

