#--- 1. Deklarasi Data Mahasiswa ---
nim = "23010199"
nama_mahasiswa = "Ahmad Rian"
semester = 3
is_aktif = True # status regristasi ulang

#--- 2. Data nilai mentah (simulasi input dari Form Web / Database) ---
# Catatan: Iput dari Form seingkali terbaca sebagai string 
str_nilai_algortima = "85.5"
str_nilai_basis_data = "78.0"
str_nilai_pemrograman_web = "90.2"
sks_per_matkul = 3 # Integer 

# Tampilan Data Awal
print(f"Data Mahasiswa : {nama_mahasiswa} (NIM : {nim})")
print("Status Aktif :", is_aktif)