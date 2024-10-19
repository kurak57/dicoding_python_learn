import random

# Variabel nama dan tugas
nama_nama = ["Andi", "Budi", "Citra", "Dewi", "Eko", "Fina"]
tugas_tugas = [
    "Menyapu", "Membersihkan papan tulis", "Menyiram tanaman", "Mengatur buku di perpustakaan",
    "Merapikan meja", "Membuang sampah", "Membersihkan jendela", "Mengelap meja", 
    "Mengatur kursi", "Mengecek alat tulis", "Menyusun buku di rak", 
    "Mengisi air minum", "Merawat tanaman", "Mengepel lantai"
]

# Mengacak nama dan tugas
random.shuffle(nama_nama)
random.shuffle(tugas_tugas)

# Menghitung jumlah tugas per orang (pembagian)
jumlah_tugas_per_orang = len(tugas_tugas) // len(nama_nama)  # Tugas yang bisa dibagi rata
sisa_tugas = len(tugas_tugas) % len(nama_nama)  # Tugas yang tersisa
# Membuat list of dictionaries dengan key 'nama' dan 'tugas'
penugasan = []
print(penugasan)
# Mengassign tugas-tugas ke setiap nama
start = 0
for i, nama in enumerate(nama_nama):
    # Menentukan jumlah tugas yang harus diberikan kepada nama ini
    jumlah_tugas = jumlah_tugas_per_orang + (1 if i < sisa_tugas else 0)
    # Assign tugas ke nama tersebut dan buat dictionary
    tugas_per_orang = tugas_tugas[start:start + jumlah_tugas]
    print("ini start",start)
    print(tugas_per_orang)
    penugasan.append({
        "nama": nama,
        "tugas": tugas_per_orang
    })
    
    # Update posisi awal untuk tugas berikutnya
    start += jumlah_tugas

# # Output contoh
# for item in penugasan:
#     print(item)
