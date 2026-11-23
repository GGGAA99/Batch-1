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



#--- 3. Konversi Tipe Data (Type Casting) ---
nilai_algo = float(str_nilai_algortima)
nilai_bd = float(str_nilai_basis_data)
nilai_web = float(str_nilai_pemrograman_web)

#--- 4. kalkulasi menggunakan Variabel ---
total_nilai = nilai_algo + nilai_bd + nilai_web
jumlah_matkul = 3 
rata_rata_nilai = total_nilai / jumlah_matkul
total_sks_diambil = jumlah_matkul * sks_per_matkul

# Penentuan status kelulusan semester (Boolean)
# Lulus jika rata_rata >= 75.0 dan status mahasiswa aktif
is_lulus_semester = (rata_rata_nilai >= 75.0) and is_aktif

print("\n--- HASIL EVALUASI AWAL ---")
print("Total Nilai          :", total_nilai)
print("Rata_Rata Nilai      :", round(rata_rata_nilai, 2))
print("Total SKS            :", total_sks_diambil)
print("Status Lulus         :", is_lulus_semester)