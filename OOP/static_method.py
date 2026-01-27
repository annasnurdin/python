class Perhitungan:

  @staticmethod # membuat method menjadi seperti fungsi biasa tanpa harus membuat instance objek, tapi dia tidak bisa akses property. 
  def tambah(a, b):
    return a + b
  
hasil_penjumlahan = Perhitungan.tambah(1, 1)
print(hasil_penjumlahan)