# SMILES for Indies
## Sistem Manajemen Inventori dan Laporan Ekonomi Seller Indie

---

## Deskripsi Program

Sistem manajemen inventori sederhana yang dirancang khusus untuk indie seller yang berjualan merchandise di berbagai event seperti Comifuro, AFA Indonesia, Cocoma, dan online store. Program ini membantu mengelola produk, event, dan transaksi penjualan dengan fitur recycle bin untuk keamanan data.

---

## Fitur Utama

### Manajemen Produk (CRUD Lengkap)
* **Lihat Produk**: Menampilkan semua produk dalam inventori dengan informasi lengkap
* **Tambah Produk**: Menambahkan produk baru pada inventori dengan fitur auto-generate Product ID
* **Update Produk**: Edit nama, kategori, harga, atau stok secara satuan, ataupun edit semua data suatu produk secara langsung
* **Hapus Produk**: Soft delete dengan recycle bin (produk dapat di-restore)

### Manajemen Event (CRUD Lengkap)
* **Lihat Event**: Menampilkan daftar semua event saat ini
* **Tambah Event**: Menambahkan event baru dalam list
* **Update Event**: Edit nama event (contoh: fix typo "Comifro" → "Comifuro")
* **Hapus Event**: Penghapusan permanen dengan konfirmasi

### Manajemen Transaksi (Star Feature!)
* **Proses Penjualan**:
  * Pilih produk yang ingin dijual berdasarkan ID
  * Pilih event tempat terjadinya transaksi
  * Validasi stok otomatis (mencegah overselling)
  * Warning stok rendah (≤5 unit)
  * Auto-generate ID transaksi
  * Perhitungan otomatis: revenue, profit, update stok
* **Lihat Riwayat**:
  * Semua transaksi
  * Filter berdasarkan event
  * Filter berdasarkan produk
  * Ringkasan lengkap: total transaksi, item terjual, pendapatan, profit

### Recycle Bin
* **Lihat Recycle Bin**: Daftar produk yang dihapus
* **Restore Produk**: Kembalikan produk ke inventory dengan ID yang sama

---

## Cara Menggunakan Program

### Instalasi & Setup

1. **Install Python** (versi 3.6 atau lebih baru)

2. **Install Library yang Dibutuhkan:**
```bash
pip install prettytable
```

3. **Jalankan Program:**
```bash
python "Capstone 2 - Nadya_Luthfiyah.py"
```

---

## Panduan Penggunaan

### Main Menu
```
MANAJEMEN PRODUK
  1. Lihat Semua Produk
  2. Tambah Produk Baru
  3. Update Produk
  4. Hapus Produk

MANAJEMEN EVENT
  5. Lihat Semua Event
  6. Tambah Event Baru
  7. Update Event
  8. Hapus Event

PENJUALAN & TRANSAKSI
  9. Proses Penjualan
  10. Lihat Riwayat Penjualan

RECYCLE BIN
  11. Lihat Recycle Bin
  12. Restore produk dari Recycle Bin

  0. Keluar
```

### 1. Lihat Semua Produk
Menampilkan tabel inventori produk dengan informasi: ID, Nama, Kategori, Harga Modal, Harga Jual, dan Stok.

### 2. Tambah Produk Baru
1. Program menampilkan inventory saat ini
2. Program auto-generate ID produk baru (contoh: P9)
3. Input data produk: Nama, Kategori, Harga Modal, Harga Jual, Stok Awal
4. Produk ditambahkan ke inventory

### 3. Update Produk
1. Masukkan ID produk yang ingin diupdate
2. Program menampilkan detail produk saat ini
3. Pilih field yang ingin diupdate:
   - Nama Produk
   - Kategori
   - Harga Modal
   - Harga Jual
   - Stok
   - Update Semua
4. Input data baru
5. Program menampilkan detail produk setelah update

### 4. Hapus Produk
1. Masukkan ID produk yang ingin dihapus
2. Program menampilkan detail produk
3. Konfirmasi penghapusan (Y/N)
4. Produk dipindahkan ke Recycle Bin

### 5. Lihat Semua Event
Menampilkan tabel daftar event dengan nomor urut dan nama event.

### 6. Tambah Event Baru
1. Program menampilkan daftar event saat ini
2. Input nama event baru
3. Program mencegah duplikat event
4. Event ditambahkan ke daftar

### 7. Update Event
1. Pilih nomor event yang ingin diupdate
2. Program menampilkan nama event saat ini
3. Input nama event baru
4. Program mencegah duplikat event
5. Event berhasil diupdate

### 8. Hapus Event
1. Pilih nomor event yang ingin dihapus
2. Program menampilkan event yang akan dihapus
3. Konfirmasi penghapusan (Y/N)
4. Event dihapus permanen (tidak masuk recycle bin)

### 9. Proses Penjualan
1. Masukkan ID produk yang ingin dijual
2. Program menampilkan detail produk dan stok tersedia
3. Input jumlah yang ingin dijual
4. Pilih event tempat transaksi
5. Program memproses:
   - Auto-generate Transaction ID (T1, T2, T3...)
   - Update stok otomatis
   - Hitung revenue dan profit
   - Catat tanggal otomatis
6. Program menampilkan informasi transaksi lengkap

### 10. Lihat Riwayat Penjualan

**Sub-menu:**
1. **Lihat Semua Transaksi**: Menampilkan tabel semua transaksi dengan total pendapatan dan profit
2. **Filter Berdasarkan Event**: Menampilkan transaksi di event tertentu dengan ringkasan lengkap
3. **Filter Berdasarkan Produk**: Menampilkan riwayat penjualan produk tertentu dengan ringkasan lengkap

### 11. Lihat Recycle Bin
Menampilkan tabel produk yang terhapus dengan informasi lengkap.

### 12. Restore Produk dari Recycle Bin
1. Pilih nomor produk yang ingin di-restore
2. Produk dikembalikan ke inventory dengan ID yang sama
3. Program menampilkan konfirmasi dengan detail produk

### 0. Keluar
Program menampilkan pesan penutup dan berhenti.

---

## Data Initialization

Program sudah terisi dengan sample data:
* **8 produk** FFXIV-themed merchandise
* **4 event** (Comifuro 22, AFA Indonesia 2026, Cocoma 4, Online Store)
* **0 transaksi** (kosong di awal)
* **0 deleted products** (kosong di awal)

Silahkan gunakan menu **Delete Product** (4) dan **Delete Event** (8) jika ingin memulai menggunakan program dengan inventori produk dan daftar event yang masih kosong.

---

## FAQ

**Q: Apa yang terjadi jika saya update harga produk?**  
A: Harga di transaksi lama tetap menggunakan harga saat transaksi. Hanya transaksi baru yang menggunakan harga baru.

**Q: Apa yang terjadi jika saya update nama event?**  
A: Nama event di transaksi lama tetap menggunakan nama saat transaksi. Hanya transaksi baru yang menggunakan nama baru.

**Q: Bagaimana jika saya tidak sengaja hapus produk?**  
A: Produk masuk ke Recycle Bin dan bisa di-restore dengan ID yang sama.

**Q: Kenapa ID produk saya P1, P2, P5 (tidak ada P3-P4)?**  
A: P3 dan P4 mungkin sudah dihapus. Saat generate ID baru, program cek angka tertinggi dari inventory DAN recycle bin.

**Q: Apakah data tersimpan setelah program ditutup?**  
A: Tidak, data tersimpan di memory. Untuk menyimpan permanen perlu tambahkan file I/O atau database.

---

## Terima Kasih!

**Nama**: Nadya Luthfiyah  
**Project**: Capstone Module 1 - Python Programming  
**Tanggal**: Februari 2026
