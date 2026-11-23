# 1. Konversi dari string ke interger
str_angka = "100"
int_angka = int(str_angka)
print("Hasil Penjualan (100 + 50):", int_angka + 50)

# 2. Konversi darai Float ke Interger (Angka dibelakang koma dihilangkan)
ipk_float = 3.96 
ipk_int = int(ipk_float)
print("Float ke Int:", ipk_int) # output 3 

# 3. Konversi dari Integer ke String 
tahun = 2026
pesan = "Tahun saat ini:" + str(tahun)
print(pesan)

# 4. Konversi dari List ke Set (Menghapus elemen duplikat)
daftar_buah = ["Apel", "Jeruk", "Apel", "Pisang", "Jeruk"]
buah_unik = set(daftar_buah)
print("Buah Unik:", buah_unik)