#Import Library
from prettytable import PrettyTable
from datetime import datetime

#------------------------------------------------------------

#MEMBUAT LIST

#Inventori Produk (terisi dengan sample)
inventory = [
    {'product_id': 'P1', 'product_name': 'FFXIV DPS Lanyard', 'category': 'Lanyard', 'cost_price': 18000, 'sell_price': 40000, 'stock': 45},
    {'product_id': 'P2', 'product_name': 'FFXIV Tank Lanyard', 'category': 'Lanyard', 'cost_price': 18000, 'sell_price': 40000, 'stock': 30},
    {'product_id': 'P3', 'product_name': 'FFXIV Healer Lanyard', 'category': 'Lanyard', 'cost_price': 18000, 'sell_price': 40000, 'stock': 20},
    {'product_id': 'P4', 'product_name': 'Themis Keychain', 'category': 'Keychain', 'cost_price': 12000, 'sell_price': 25000, 'stock': 50},
    {'product_id': 'P5', 'product_name': 'Venat Keychain', 'category': 'Keychain', 'cost_price': 12000, 'sell_price': 25000, 'stock': 45},
    {'product_id': 'P6', 'product_name': 'Job Stone Stickers', 'category': 'Sticker', 'cost_price': 5000, 'sell_price': 10000, 'stock': 100},
    {'product_id': 'P7', 'product_name': 'Ishgard Print', 'category': 'Prints', 'cost_price': 15000, 'sell_price': 30000, 'stock': 40},
    {'product_id': 'P8', 'product_name': 'Crystarium Print', 'category': 'Prints', 'cost_price': 15000, 'sell_price': 30000, 'stock': 35}
]

#Daftar Event (terisi dengan sample)
events_list = ["Comifuro 22", "AFA Indonesia 2026", "Cocoma 4", "Online Store"]

#Daftar Transaksi
transactions = []

#Recycle Bin
deleted_products = []

#------------------------------------------------------------

#HELPER FUNCTIONS: Validasi Input

#Validasi Input Int
def get_int_input(message):
    while True:
        try:
            value = int(input(message))
            if value < 0:
                print("Mohon masukkan angka positif!")
                continue
            return value
        except ValueError:
            print("Input tidak valid! Mohon masukkan angka yang benar.")

#Validasi Input String
def get_string_input(message):
    while True:
        value = input(message).strip() #.strip untuk menghilangkan spasi
        if value == "":
            print("Input tidak boleh kosong! Silakan coba lagi.")
        else:
            return value

#Validasi Y/N (konfirmasi)
def confirmation(message):
    while True:
        confirm = input(message).strip().upper()
        
        if confirm == 'Y':
            return True
        elif confirm == 'N':
            return False
        else:
            print("Input tidak valid. Ketik Y untuk ya atau N untuk tidak.")

#------------------------------------------------------------

#PRODUCT MANAGEMENT - CRUD

#Helper Function - Membuat Product ID
def generate_product_id():
    #Untuk memastikan bahwa tidak ada double ID, fungsi generate product_id juga memerhatikan produk pada recycle bin
    all_ids = []

    #Tambahkan ID dari inventory & Recycle Bin
    for product in inventory:
        all_ids.append(product['product_id'])
    for product in deleted_products:
        all_ids.append(product['product_id'])

    #Ekstrak angka dari semua ID (all_ids)
    numbers = []
    for product_id in all_ids:
        number = int(product_id[1:])
        numbers.append(number)

    #Generate ID berikutnya (ID tertinggi + 1)
    highest_number = max(numbers)
    new_ID = highest_number + 1

    return f"P{new_ID}"

#Helper Function - Memilih produk berdasarkan ID (mengembalikan index produk)
def select_product(message="Masukkan ID Produk"):
    while True:
        product_id = get_string_input(f"\n{message}: ").upper()
        
        #Cari produk berdasarkan ID
        product_index = None
        for index, product in enumerate(inventory):
            if product['product_id'] == product_id:
                product_index = index
                break
        
        if product_index is None:
            print("Produk tidak ditemukan! Silakan coba lagi. Misal, 'P1'")
            continue
        else:
            return product_index

#Main & Helper Function - Menampilkan Inventori Produk (cRud)
def show_inventory():
    print("\nINVENTORI PRODUK")

    if len(inventory) == 0:
        print("Tidak ada produk di inventori!")
        return

    table = PrettyTable(["ID Produk", "Nama Produk", "Kategori", "Harga Modal", "Harga Jual", "Stok"])
    for p in inventory:
        table.add_row([p['product_id'], p['product_name'], p['category'], f"Rp {p['cost_price']:,}", f"Rp {p['sell_price']:,}", p['stock']])

    print(table)
    print(f"Total Produk: {len(inventory)}")

#Helper Function - Menampilkan detail 1 produk spesifik
def display_product_detail(product):
    print(f"ID: {product['product_id']}")
    print(f"Nama: {product['product_name']}")
    print(f"Kategori: {product['category']}")
    print(f"Harga Modal: Rp {product['cost_price']:,}")
    print(f"Harga Jual: Rp {product['sell_price']:,}")
    print(f"Stok: {product['stock']}")

#Main Function - Membuat produk baru (Crud)
def add_product():
    print("\nTAMBAH PRODUK BARU")
    show_inventory()

    #Auto-generate product ID
    product_id = generate_product_id()
    print(f"ID Produk Baru: {product_id}")

    #User mengisi detail produk baru
    product_name = get_string_input("Nama Produk: ")
    category = get_string_input("Kategori (Keychain/Sticker/Lanyard/Prints/Lainnya): ")
    cost_price = get_int_input("Harga Modal (Rp): ")
    sell_price = get_int_input("Harga Jual (Rp): ")
    stock = get_int_input("Stok Awal: ")

    #Membuat dictionary produk baru
    new_product = {
        'product_id': product_id,
        'product_name': product_name,
        'category': category,
        'cost_price': cost_price,
        'sell_price': sell_price,
        'stock': stock
    }

    #Menambahkan dictionary produk baru ke list Inventori Produk
    inventory.append(new_product)

    #Konfirmasi
    print("\nPRODUK BERHASIL DITAMBAHKAN!")

#Main Function - Update Inventori Produk (crUd)
def update_product():
    print("\nUPDATE PRODUK")
    show_inventory()

    if len(inventory) == 0:
        return

    #User memilih produk berdasarkan ID
    product_index = select_product("Masukkan ID Produk yang ingin diupdate")
    product = inventory[product_index]

    #Menampilkan detail produk yang dipilih
    print("\nDETAIL PRODUK SAAT INI:")
    display_product_detail(product)

    #Menu update
    while True:
        print("\nApa yang ingin diupdate?")
        print("1. Nama Produk")
        print("2. Kategori")
        print("3. Harga Modal")
        print("4. Harga Jual")
        print("5. Stok")
        print("6. Update Semua")
        print("0. Batal")

        choice = input("\nPilih opsi: ").strip()

        if choice == "1":
            product['product_name'] = get_string_input("Nama Produk Baru: ")
            print("Nama produk berhasil diupdate!")
            break

        elif choice == "2":
            product['category'] = get_string_input("Kategori Baru: ")
            print("Kategori berhasil diupdate!")
            break

        elif choice == "3":
            product['cost_price'] = get_int_input("Harga Modal Baru (Rp): ")
            print("Harga modal berhasil diupdate!")
            break

        elif choice == "4":
            product['sell_price'] = get_int_input("Harga Jual Baru (Rp): ")
            print("Harga jual berhasil diupdate!")
            break

        elif choice == "5":
            product['stock'] = get_int_input("Stok Baru: ")
            print("Stok berhasil diupdate!")
            break

        elif choice == "6":
            product['product_name'] = get_string_input("Nama Produk Baru: ")
            product['category'] = get_string_input("Kategori Baru: ")
            product['cost_price'] = get_int_input("Harga Modal Baru (Rp): ")
            product['sell_price'] = get_int_input("Harga Jual Baru (Rp): ")
            product['stock'] = get_int_input("Stok Baru: ")
            print("Semua data berhasil diupdate!")
            break

        elif choice == "0":
            print("Update dibatalkan.")
            return

        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

    print("\nDETAIL PRODUK SETELAH UPDATE:")
    display_product_detail(product)

#Main Function - Delete Product
def delete_product():
    print("\nHAPUS PRODUK")
    show_inventory()

    if len(inventory) == 0:
        return

    #User memilih produk berdasarkan ID
    product_index = select_product("Masukkan ID Produk yang ingin dihapus")
    product = inventory[product_index]

    #Menampilkan detail produk yang dipilih
    print("\nPRODUK YANG AKAN DIHAPUS:")
    display_product_detail(product)

    #Proses penghapusan
    if confirmation("\nApakah Anda yakin ingin menghapus produk ini? (Y/N): "):
        deleted_product = inventory.pop(product_index)
        deleted_products.append(deleted_product)
        print(f"\nProduk '{product['product_name']}' telah terhapus!")
    else:
        print("Penghapusan dibatalkan.")

#------------------------------------------------------------

#EVENT MANAGEMENT - CRUD

#Helper Function - Memilih Event
def select_event(message="Pilih nomor event"):
    if len(events_list) == 0:
        return None

    while True:
        try:
            choice = int(input(f"\n{message} (1-{len(events_list)}): "))
            if 1 <= choice <= len(events_list):
                return events_list[choice - 1]
            else:
                print(f"Mohon pilih angka antara 1 dan {len(events_list)}")
        except ValueError:
            print("Input tidak valid! Mohon masukkan angka yang benar.")

#Main & Helper Function - Menampilkan Daftar Event (cRud)
def show_events():
    print("\nDAFTAR EVENT")

    if len(events_list) == 0:
        print("Belum ada event!")
        return

    table = PrettyTable(["No", "Nama Event"])

    for i, event in enumerate(events_list, 1):
        table.add_row([i, event])

    print(table)
    print(f"Total Event: {len(events_list)}")

#Main Function - Membuat Event baru (Crud)
def add_event():
    print("\nTAMBAH EVENT BARU")
    show_events()

    while True:
        event_name = get_string_input("Input nama event baru: ")
        if event_name in events_list:
            print(f"Event '{event_name}' sudah ada! Silakan masukkan nama event yang berbeda.") #cek duplikat
            continue
        else:
            break

    events_list.append(event_name)
    print(f"Event '{event_name}' berhasil ditambahkan!")

#Main Function - Update Event (crUd)
def update_event():
    print("\nUPDATE EVENT")
    show_events()

    #Pilih event menggunakan helper
    old_event = select_event("Pilih nomor event yang ingin diupdate")
    if old_event is None:
        return

    #Tampilkan event saat ini
    print(f"\nEvent saat ini: {old_event}")

    #User mengupdate nama event
    while True:
        new_event_name = get_string_input("Nama event baru: ")
        
        #Cek duplikat nama event
        if new_event_name == old_event:
            print("Nama event sama dengan sebelumnya. Tidak ada perubahan.")
            return
        elif new_event_name in events_list:
            print(f"Event '{new_event_name}' sudah ada! Silakan masukkan nama event yang berbeda.")
            continue
        else:
            break

    event_index = events_list.index(old_event)
    events_list[event_index] = new_event_name

    print(f"\nEvent berhasil diupdate dari '{old_event}' menjadi '{new_event_name}'!")

#Main Function - Delete Event (permanen, tidak ada recycle bin)
def delete_event():
    print("\nHAPUS EVENT")
    show_events()

    #Pilih event menggunakan helper
    event_name = select_event("Pilih nomor event yang akan dihapus")

    if event_name is None:
        return

    #Tampilkan detail event
    print("\nEVENT YANG AKAN DIHAPUS:")
    print(f"Nama Event: {event_name}")

    #Konfirmasi penghapusan
    if confirmation("\nApakah Anda yakin ingin menghapus event ini? (Y/N): "):
        events_list.remove(event_name)
        print(f"\nEvent '{event_name}' berhasil dihapus!")
    else:
        print("Penghapusan dibatalkan.")

#------------------------------------------------------------

#TRANSACTION MANAGEMENT

#A. PROSES PENJUALAN

#Helper Function - Membuat Transaction ID
def generate_transaction_id():
    if len(transactions) == 0:
        return "T1"

    last_id = transactions[-1]['transaction_id']
    number = int(last_id[1:])
    new_number = number + 1

    return f"T{new_number}"

#Main Function - Memproses Transaksi
def process_sale():
    print("\nPROSES PENJUALAN")
    show_inventory()

    if len(inventory) == 0:
        print("\nTidak ada produk untuk dijual!")
        return

    #User memilih produk menggunakan helper
    product_index = select_product("Masukkan ID Produk yang ingin dijual")
    product = inventory[product_index]

    #Tampilkan detail produk
    print("\nDETAIL PRODUK:")
    print(f"Nama: {product['product_name']}")
    print(f"Kategori: {product['category']}")
    print(f"Harga Jual: Rp {product['sell_price']:,}")
    print(f"Stok Tersedia: {product['stock']}")

    if product['stock'] <= 5:
        print(f"\nPERINGATAN STOK RENDAH! Hanya tersisa {product['stock']} unit!")

    #User memilih jumlah yang ingin dijual
    print("\nMasukkan jumlah yang ingin dijual:")
    while True:
        quantity = get_int_input("Jumlah: ")

        if quantity == 0:
            print("Jumlah harus lebih dari 0!")
        elif quantity > product['stock']:
            print(f"Stok tidak cukup! Stok tersedia: {product['stock']}")
        else:
            break

    #User memilih event
    print("\nPILIH EVENT")
    show_events()
    event_name = select_event()

    if event_name is None:
        print("Tidak ada event tersedia! Silakan tambah event terlebih dahulu.")
        return

    #Memproses dan mencatat transaksi
    transaction_id = generate_transaction_id()
    inventory[product_index]['stock'] -= quantity

    revenue = product['sell_price'] * quantity
    profit = (product['sell_price'] - product['cost_price']) * quantity

    current_date = datetime.now().strftime("%Y-%m-%d")

    transaction = {
        'transaction_id': transaction_id,
        'product_id': product['product_id'],
        'product_name': product['product_name'],
        'quantity_sold': quantity,
        'sell_price': product['sell_price'],
        'cost_price': product['cost_price'],
        'revenue': revenue,
        'profit': profit,
        'event_name': event_name,
        'date': current_date
    }

    transactions.append(transaction)

    #Menampilkan informasi transaksi
    print("\nPENJUALAN BERHASIL!")
    print(f"ID Transaksi: {transaction_id}")
    print(f"Produk: {product['product_name']}")
    print(f"Jumlah: {quantity}")
    print(f"Harga Satuan: Rp {product['sell_price']:,}")
    print(f"Pendapatan: Rp {revenue:,}")
    print(f"Profit: Rp {profit:,}")
    print(f"Event: {event_name}")
    print(f"Tanggal: {current_date}")
    print(f"Sisa Stok: {inventory[product_index]['stock']}")

# B. LIHAT RIWAYAT TRANSAKSI

#Helper Function - Tampilkan Transaksi (dalam tabel)
def display_transactions_table(transactions_list):
    table = PrettyTable(["ID Transaksi", "Produk", "Jumlah", "Harga", "Pendapatan", "Profit", "Event", "Tanggal"])

    for t in transactions_list:
        table.add_row([t['transaction_id'], t['product_name'], t['quantity_sold'], f"Rp {t['sell_price']:,}", f"Rp {t['revenue']:,}", f"Rp {t['profit']:,}", t['event_name'], t['date']])

    return table

#Helper Function - Display summary dengan perhitungan otomatis
def display_summary(transactions_list):
    #Hitung total
    total_items = 0
    total_revenue = 0
    total_profit = 0

    for t in transactions_list:
        total_items += t['quantity_sold']
        total_revenue += t['revenue']
        total_profit += t['profit']

    #Tampilkan ringkasan
    print(f"\nTotal Transaksi: {len(transactions_list)}")
    print(f"Total Item Terjual: {total_items}")
    print(f"Total Pendapatan: Rp {total_revenue:,}")
    print(f"Total Profit: Rp {total_profit:,}")

#Helper Function - Menampilkan riwayat transaksi berdasarkan event
def filter_by_event():
    print("\nFILTER BERDASARKAN EVENT")

    if len(transactions) == 0:
        print("Belum ada transaksi!")
        return

    #Menampilkan event yang digunakan dalam transaksi
    events_in_transactions = []
    for t in transactions:
        if t['event_name'] not in events_in_transactions:
            events_in_transactions.append(t['event_name'])

    if len(events_in_transactions) == 0:
        print("Belum ada transaksi!")
        return

    print("\nEvent yang tersedia:")
    for i, event in enumerate(events_in_transactions, 1):
        print(f"  {i}. {event}")

    #User memilih event
    while True:
        try:
            choice = int(input(f"\nPilih nomor event (1-{len(events_in_transactions)}): "))
            if 1 <= choice <= len(events_in_transactions):
                break
            else:
                print(f"Mohon pilih angka antara 1 dan {len(events_in_transactions)}")
        except ValueError:
            print("Input tidak valid! Mohon masukkan angka yang benar.")

    selected_event = events_in_transactions[choice - 1]

    #Filter transaksi
    filtered = []
    for t in transactions:
        if t['event_name'] == selected_event:
            filtered.append(t)

    #Tampilkan list transaksi yang telah di-filter beserta summary-nya
    print(f"\nTRANSAKSI DI: {selected_event}")

    table = display_transactions_table(filtered)
    print(table)

    display_summary(filtered)

#Helper Function - Menampilkan berdasarkan produk
def filter_by_product():
    print("\nFILTER BERDASARKAN PRODUK")

    if len(transactions) == 0:
        print("Belum ada transaksi!")
        return

    #Menampilkan produk yang terjual (ada pada transaksi)
    products_sold = {}
    for t in transactions:
        if t['product_id'] not in products_sold:
            products_sold[t['product_id']] = t['product_name']

    if len(products_sold) == 0:
        print("Belum ada transaksi!")
        return

    print("\nProduk yang pernah terjual:")
    product_list = list(products_sold.items())

    for i, (pid, pname) in enumerate(product_list, 1):
        print(f"  {i}. [{pid}] {pname}")

    #User memilih produk
    while True:
        try:
            choice = int(input(f"\nPilih nomor produk (1-{len(product_list)}): "))
            if 1 <= choice <= len(product_list):
                break
            else:
                print(f"Mohon pilih angka antara 1 dan {len(product_list)}")
        except ValueError:
            print("Input tidak valid! Mohon masukkan angka yang benar.")

    selected_id, selected_name = product_list[choice - 1]

    #Filter transaksi
    filtered = []
    for t in transactions:
        if t['product_id'] == selected_id:
            filtered.append(t)

    #Tampilkan list transaksi yang telah di-filter beserta summary-nya
    print(f"\nRIWAYAT PENJUALAN: {selected_name}")

    table = display_transactions_table(filtered)
    print(table)

    display_summary(filtered)

#Main Function - Menampilkan Riwayat Transaksi
def view_transactions():
    while True:
        print("\nRIWAYAT PENJUALAN - PILIHAN TAMPILAN")
        print("1. Lihat Semua Transaksi")
        print("2. Filter Berdasarkan Event")
        print("3. Filter Berdasarkan Produk")
        print("0. Kembali ke Menu Utama")

        choice = input("\nPilih opsi: ").strip()

        if choice == "1":
            print("\nSEMUA TRANSAKSI")
            
            if len(transactions) == 0:
                print("Belum ada transaksi!")
            else:
                table = display_transactions_table(transactions)
                print(table)
                
                display_summary(transactions)
                
        elif choice == "2":
            filter_by_event()
        elif choice == "3":
            filter_by_product()
        elif choice == "0":
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

#------------------------------------------------------------

#RECYCLE BIN

#Main Function - Read/Show Produk pada Recycle Bin
def view_recycle_bin():
    print("\nRECYCLE BIN")

    if len(deleted_products) == 0:
        print("Recycle bin kosong!")
        return

    table = PrettyTable()
    table.field_names = ["No", "ID Produk", "Nama Produk", "Kategori", "Harga Modal", "Harga Jual", "Stok"]

    for i, product in enumerate(deleted_products, 1):
        table.add_row([i, product['product_id'], product['product_name'], product['category'], f"Rp {product['cost_price']:,}", f"Rp {product['sell_price']:,}", product['stock']])

    print(table)
    print(f"Total Produk Terhapus: {len(deleted_products)}")

#Main Function - Restore produk ke inventori
def restore_product():
    print("\nRESTORE PRODUK")
    view_recycle_bin()

    if len(deleted_products) == 0:
        return

    #User memilih produk
    print("\nMasukkan nomor produk yang ingin di-restore")

    while True:
        try:
            choice = int(input(f"Pilih nomor produk (1-{len(deleted_products)}, 0 untuk batal): "))
            if choice == 0:
                print("Restore dibatalkan.")
                return
            elif 1 <= choice <= len(deleted_products):
                break
            else:
                print(f"Mohon pilih angka antara 1 dan {len(deleted_products)}")
        except ValueError:
            print("Input tidak valid! Mohon masukkan angka yang benar.")

    product_index = choice - 1
    restored_product = deleted_products.pop(product_index)

    #Tambahkan kembali ke inventori
    inventory.append(restored_product)

    #Konfirmasi
    print("\nPRODUK BERHASIL DI-RESTORE!")
    print(f"ID: {restored_product['product_id']}")
    print(f"Nama: {restored_product['product_name']}")
    print(f"Kategori: {restored_product['category']}")
    print(f"Stok: {restored_product['stock']}")

#------------------------------------------------------------

#MAIN MENU

def main_menu():
    while True:
        print("\nMANAJEMEN PRODUK")
        print("  1. Lihat Semua Produk")
        print("  2. Tambah Produk Baru")
        print("  3. Update Produk")
        print("  4. Hapus Produk")
        print("\nMANAJEMEN EVENT")
        print("  5. Lihat Semua Event")
        print("  6. Tambah Event Baru")
        print("  7. Update Event")
        print("  8. Hapus Event")
        print("\nPENCATATAN TRANSAKSI")
        print("  9. Proses Penjualan")
        print("  10. Lihat Riwayat Transaksi")
        print("\nRECYCLE BIN")
        print("  11. Lihat Recycle Bin")
        print("  12. Restore produk dari Recycle Bin")
        print("\n  0. Keluar")

        choice = input("\nMenu: ").strip()

        if choice == "1":
            show_inventory()
        elif choice == "2":
            add_product()
        elif choice == "3":
            update_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            show_events()
        elif choice == "6":
            add_event()
        elif choice == "7":
            update_event()
        elif choice == "8":
            delete_event()
        elif choice == "9":
            process_sale()
        elif choice == "10":
            view_transactions()
        elif choice == "11":
            view_recycle_bin()
        elif choice == "12":
            restore_product()
        elif choice == "0":
            print("\nTerima kasih telah menggunakan program ini!")
            print("Program ditutup.")
            break
        else:
            print("\nPilihan tidak valid! Silakan pilih menu yang tersedia.")

        #Jeda sebelum menampilkan menu lagi
        input("\nTekan Enter untuk melanjutkan...")

#------------------------------------------------------------

#PROGRAM START
print("Selamat datang di 'SMILES for Indies' (Sistem Manajemen Inventori dan Laporan Ekonomi Seller Indie)")
print("Silahkan pilih menu di bawah ini.")

main_menu()
