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


#--- 5. Tipe Data Koleksi ---
# List daftar mata kuliah yang diambil 
daftar_matkul = ["Algortima dan Pemrograman", "Basis Data", "Pemrograman Web"]

# Dictionary untuk menyimpan Nilai Mutu (KRS/KHS)
transkrip_nilai = {
    "Algoritma dan Pemrograman": 4.0,   # Nilai A
    "Basis Data": 3.0,                  # Nilai B
    "Pemrograman Web": 4.0              # Nilai A
}

print("\nDaftar Mata Kuliah Diambil :", daftar_matkul)
print("Detail Transkrip Mutu        :", transkrip_nilai)



#--- 6. Update Variabel Dinamis ---
# Mahasiswa mengambil 1 mata kuliah susulan
matkul_baru = "Jaringan Komputer"
nilai_matkul_baru_str = "88.0"
mutu_matkul_baru = 3.5 # Nilai AB

# A. Tambahkan ke List
daftar_matkul.append(matkul_baru)

# B. Tambahkan ke Dictionary
transkrip_nilai[matkul_baru] = mutu_matkul_baru

# C. Rekalkulasi Variabel Total & Rata_rata
nilai_jk = float(nilai_matkul_baru_str)
total_nilai = total_nilai +  nilai_jk 
jumlah_matkul = len(daftar_matkul)
rata_rata_terbaru = total_nilai / jumlah_matkul

# D. Hitung Indeks Prestasi Kumulatif (IPK) dari Dictionary Mutu
total_bobot_mutu = sum(transkrip_nilai.values())
ipk_sementara = total_bobot_mutu / jumlah_matkul

print("\n--- HASIL REKALKULASI SETELAH PENAMBAHAN MATKUL ---")
print("Daftar Matkul Terbaru    :", daftar_matkul)
print("Jumlah Matkul Total      :", jumlah_matkul)
print("Rata-rata Angka Baru     :", round(rata_rata_terbaru, 2))
print("IPK Sementara (Skala 4)  :", round(ipk_sementara, 2))