"""
Modul ini adalah modul yang digunakan untuk menjalankan Sistem Self Service Cashier
"Super Cashier". Modul ini digunakan untuk Supermarket yang dimiliki Andi untuk 
meningkatkan pelayanan dan kemudahan berbelanja bagi customer yang berbelanja di supermarketnya

Code ini dibuat oleh Oktavio Reza Putra (Reza) untuk menyelesaikan Final Project Python untuk Materi
"Basic Python Programming & Python for Software Engineering" by Pacmann Academy (Pacmann AI)
"""
from tabulate import tabulate

class Transaction():
    """
    class Transaction adalah fitur super cashier yang akan digunakan customer
    untuk berbelanja di Supermarket Cak Andi
    
    Ada berbagai fitur (method) yang bisa digunakan antara lain:
    1. Sistem untuk menambahkan item dengan quantity (qty) dan price per item dengan method add_item()
    2. Sistem untuk Update nama Item dengan method update_item_name()
    3. Sistem untuk Update Quantity (qty) dengan method update_item_qty()
    4. Sistem untuk Update Price dengan method update_item_price()
    5. Sistem untuk Menghapus Item dengan method delete_item()s
    6. Sistem untuk melakukan Reset pada Order dengan method reset_transaction()
    7. Melakukan check pada Order dengan method check_order()
    8. Sistem untuk menghitung total price dan diskon dengan method total_price()
    9. Fitur Tambahan : Sistem untuk menapilkan Tabel Item Belanja seperti Nota Sederhana dengan method table_belanja()
    
    Return : Nota Item Belanja Customer
    """
    def __init__(self):
        print('🥰🙏🏼Selamat Datang di Supermarket Cak Andi 🙏🥰')
        print(' ')
        print(' ')
        print('Ini adalah Fitur Kasir Self-Service Kami, silakan Manfaatkan ini dengan Baik ya')        
        print('⋆｡‧˚ʚ🍓ɞ˚‧｡⋆')
        print(' ')
        print('Selamat Berbelanja dan Kepuasan Pelanggan adalah Tujuan Utama Kami ˚˖𓍢ִ໋🌷͙֒✧🩷˚.🎀༘⋆')
        print(' ')
        print(' ')
        print('Silakan Input Item Belanja yang Anda beli!')
        print('Jika sudah selesai, maka masukkan (input) Item Name dengan kata "Selesai"')
        print(' ')
        print(' ')
        print('⚠️Warning :')
        print('Kapasitas Input Item Belanja hanya 20 Jenis Item')
        print('Jika sudah mencapai 20 Jenis Item, Maka akan muncul Pertanyaan :')
        print('"Apakah Anda masih ingin melakukan Input Item Belanja Kembali?"')
        print(' ')
        print(' ')
        print(' ')
        self.list_item = []
        print('Jika anda ingin memasukkan Jenis Item Belanja kembali silakan ketik "Yes"')
    
    #Fitur Add Item Belanja---------------------------------Code by : Oktavio Reza Putra---------------------------------------------------------------------------------------------
    def add_item(self):
        """
        fitur (method) add_item() digunakan sebagai method untuk
        memasukkan item belanja customer
        
        1. batas input belanja hanya sampai 20 list item
        2. setelah selesai melakukan input item belanja, maka nama_item diisi "selesai"
        3. setelah itu customer diberikan fasilitas pilihan untuk melakukan :
            a. Sistem untuk Update nama Item dengan method update_item_name()
            b. Sistem untuk Update Quantity (qty) dengan method update_item_qty()
            c. Sistem untuk Update Price dengan method update_item_price()
            d. Sistem untuk Menghapus Item dengan method delete_item()
            e. Sistem untuk melakukan Reset pada Order dengan method reset_transaction()
            f. Melakukan check pada Order dengan method check_order()
            g. Sistem untuk menghitung total price dan diskon dengan method total_price() yang diarahkan secara otomatis
        """
        #ingin menginput item belanja untuk pertama kalinya?
        input_item = str(input('Input Item Belanja? (Yes/No) : '))
        print(' ')
        if input_item.lower() == 'yes': #jika ingin menginput item belanja untuk pertama kalinya
            while True:
                try:
                    nama_item = input('Item Name : ')
                    if nama_item.lower()=='selesai':
                        #jika input item sudah selesai maka nama_item harus diinput "selesai"
                        print('Terima kasih....Input Item Belanja Anda Sudah Selesai!')
                        print(' ')
                        
                        while True:
                            #ingin melakukan update?
                            update_confirmation = str(input('Apakah Anda ingin mengganti Nama Item, Jumlah Item, atau Harga per Item yang sudah dimasukkan? (Yes / No) : '))
                            if update_confirmation.lower() == 'yes':
                                while True:
                                    update_type = str(input('Bagian Mana yang ingin Anda Update? (Pilih Salah Satu : Item Name, Jumlah Item, Harga per Item) : '))
                                    if update_type.title() == 'Item Name':
                                        self.update_item_name()
                                        break
                                    elif update_type.title() == 'Jumlah Item':
                                        self.update_item_qty()
                                        break
                                    elif update_type.title() == 'Harga Per Item':
                                        self.update_item_price()
                                        break
                                    else:
                                        print(' ')
                                        print('⚠️Warning : ')
                                        print('Mohon Maaf! Input yang Anda masukkan Tidak Terdaftar dalam Fitur Kami 🙏')
                                        print('Silakan Coba Lagi! 🙏')
                                        print(' ')
                                break
                            elif update_confirmation.lower() == 'no':
                                while True:
                                    #ingin melakukan penghapusan item belanja yang sudah diinput?
                                    deletion_order_confirmation = str(input('Apakah anda Ingin Menghapus Salah Satu Item Belanja Anda? (Yes/No) : '))
                                    if deletion_order_confirmation.lower() == 'yes':
                                        self.delete_item()
                                        break
                                    elif deletion_order_confirmation.lower() == 'no':
                                        while True:
                                            #ingin melakukan cek order
                                            check_order_confirmation = str(input('Apakah anda Ingin Melakukan Pengecekan Item Belanja Anda? (Yes/No) : '))
                                            if check_order_confirmation.lower() == 'yes':
                                                self.check_order()
                                                break
                                            elif check_order_confirmation.lower() == 'no':
                                                while True:
                                                    #ingin melakukan reset order?
                                                    reset_order_confirmation = str(input('Apakah anda Ingin Reset Input Item Belanja Anda? (Yes/No) : '))
                                                    if reset_order_confirmation.lower() == 'yes':
                                                        self.reset_transaction()
                                                        break
                                                    elif reset_order_confirmation.lower() == 'no':
                                                        while True:
                                                            #ingin menginput lagi item belanja?
                                                            input_again_confirmation = str(input('Apakah anda Ingin Melakukan Input Kembali Item Belanja Anda? (Yes/No) : '))
                                                            if input_again_confirmation.lower() == 'yes':
                                                                self.add_item()
                                                                break
                                                            elif input_again_confirmation.lower() == 'no':
                                                                #jika tidak ingin melakukan input item lagi
                                                                #dan tidak ingin menggunakan fasilitas lainnya
                                                                #maka langsung diarahkan ke method total_price() untuk mendapatkan harga keseluruhan
                                                                #beserta diskonnya (jika masuk kriteria diskon)
                                                                print(' ')
                                                                self.total_price()
                                                                print('Note : Jika ada yang ingin diinput kembali silakan buat ID Transaksi Baru 🙏🥰')
                                                                break
                                                                                                     
                                                            else: #ketika input tidak tertulis Yes dan No, maka akan diulangi kembali
                                                                print(' ')
                                                                print('⚠️Warning : ')
                                                                print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                                                                print(' ')
                                                        break
                                                    else:
                                                        print(' ')
                                                        print('⚠️Warning : ')
                                                        print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                                                        print(' ')
                                                break       
                                            else:
                                                print(' ')
                                                print('⚠️Warning : ')
                                                print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                                                print(' ')
                                        break        
                                    else:
                                        print(' ')
                                        print('⚠️Warning : ')
                                        print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                                        print(' ')
                                break
                            else:
                                print(' ')
                                print('⚠️Warning : ')
                                print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                                print(' ')
                        break
                    
                    jumlah_item = int(input('Jumlah Item : '))
                    harga_per_satuan_item = int(input('Harga per Item Quantity : '))
                    total_harga_per_item = int(harga_per_satuan_item * jumlah_item)
                    print(' ')
                    
                    self.list_item.append([nama_item.upper(), jumlah_item, harga_per_satuan_item, total_harga_per_item])
                    
                    if len(self.list_item) == 20:
                        #batas nya hanya smapai 20 list item
                        #jika sudah melebihi batas input
                        #akan keluar notifikasi sebagai berikut:
                        print(' ')
                        print(f'Kapasitas Input Item Belanja sudah Mencapai Batas Maksimum : ({len(self.list_item)} Jenis Item)')
                        
                        #namun masih bisa mengisi input item belanja lagi
                        input_item_again = str(input('Apakah Anda masih ingin melakukan Input Item Belanja Kembali? (Yes/No) : '))
                        if input_item_again.lower() == 'yes':
                            print(' ')
                            self.add_item()
                        elif input_item_again.lower() == 'no':
                            break

                except ValueError:
                    #jika terjadi kesalahan input jumlah item atau harga per satuan item
                    #misalnya kosong atau diisi dengan tipe data lain
                    #maka akan diarahkan kembali untuk mengisi item belanja di method add_item()
                    print(' ')
                    print('⚠️Warning : ')
                    print('Input Jumlah Item, Harga per Satuan Item tidak boleh kosong')
                    print('atau diinput dengan nilai selain angka!')
                    print('Silakan Ulangi Kembali Input Item Belanja Anda! 🙏')
                    print(' ')
                    self.add_item()
                    
        elif input_item.lower()=='no': #jika tidak ingin menginput item belanja untuk pertama kalinya
            if self.list_item != []: #jika list sebelumnya sudah terisi?                     
                while True:
                    #ingin melakukan update?
                    update_confirmation = str(input('Apakah Anda ingin mengganti Nama Item, Jumlah Item, atau Harga per Item yang sudah dimasukkan? (Yes / No) : '))
                    if update_confirmation.lower() == 'yes':
                        while True:
                            update_type = str(input('Bagian Mana yang ingin Anda Update? (Pilih Salah Satu : Item Name, Jumlah Item, Harga per Item) : '))
                            if update_type.title() == 'Item Name':
                                self.update_item_name()
                                break
                            elif update_type.title() == 'Jumlah Item':
                                self.update_item_qty()
                                break
                            elif update_type.title() == 'Harga Per Item':
                                self.update_item_price()
                                break
                            else:
                                print(' ')
                                print('⚠️Warning : ')
                                print('Mohon Maaf! Input yang Anda masukkan Tidak Terdaftar dalam Fitur Kami 🙏')
                                print('Silakan Coba Lagi! 🙏')
                                print(' ')
                        break
                    elif update_confirmation.lower() == 'no': 
                        while True:
                            #ingin menghapus item belanja?
                            deletion_order_confirmation = str(input('Apakah anda Ingin Menghapus Salah Satu Item Belanja Anda? (Yes/No) : '))
                            if deletion_order_confirmation.lower() == 'yes':
                                self.delete_item()
                                break
                            elif deletion_order_confirmation.lower() == 'no':
                                while True:
                                    #ingin cek order?
                                    check_order_confirmation = str(input('Apakah anda Ingin Melakukan Pengecekan Item Belanja Anda? (Yes/No) : '))
                                    if check_order_confirmation.lower() == 'yes':
                                        self.check_order()
                                        break
                                    elif check_order_confirmation.lower() == 'no':
                                        while True:
                                            #ingin reset order?
                                            reset_order_confirmation = str(input('Apakah anda Ingin Reset Input Item Belanja Anda? (Yes/No) : '))
                                            if reset_order_confirmation.lower() == 'yes':
                                                self.reset_transaction()
                                                break
                                            elif reset_order_confirmation.lower() == 'no':
                                                while True:
                                                    #ingin menginput lagi item belanja?
                                                    input_again_confirmation = str(input('Apakah anda Ingin Melakukan Input Kembali Item Belanja Anda? (Yes/No) : '))
                                                    if input_again_confirmation.lower() == 'yes':
                                                        self.add_item()
                                                        break
                                                    elif input_again_confirmation.lower() == 'no':
                                                        #jika tidak ingin melakukan input item lagi
                                                        #dan tidak ingin menggunakan fasilitas lainnya
                                                        #maka langsung diarahkan ke method total_price() untuk mendapatkan harga keseluruhan
                                                        #beserta diskonnya (jika masuk kriteria diskon)
                                                        print(' ')
                                                        self.total_price()
                                                        print('Note : Jika ada yang ingin diinput kembali silakan buat ID Transaksi Baru 🙏🥰')
                                                        break
                                                                                                     
                                                    else: #ketika input tidak tertulis Yes dan No, maka akan diulangi kembali
                                                        print(' ')
                                                        print('⚠️Warning : ')
                                                        print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                                                        print(' ')
                                                break
                                            else:
                                                print(' ')
                                                print('⚠️Warning : ')
                                                print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                                                print(' ')                              
                                        break
                                    else:
                                        print(' ')
                                        print('⚠️Warning : ')
                                        print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                                        print(' ')
                                break
                            else:
                                print(' ')
                                print('⚠️Warning : ')
                                print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                                print(' ')
                        break
                        
            elif self.list_item == []: #jika list sebelumnya kosong? atau tidak jadi mengisi untuk pertama kalinya
                self.table_belanja()
                pass
        
        else: #ketika input ingin input belanja tidak terisi yes atau no
            print('Input Salah! Silakan Ulangi Kembali! 🙏')
            self.add_item()            
    
    
    #Fitur Update Item Name-------------------------------------Code by : Oktavio Reza Putra----------------------------------------------------------------
    def update_item_name(self):
        print(' ')
        print(' ')
        print('🛍️ Fitur Update Item Name 🛍️')
        print('---------------------------------------------')
        
        #menampilkan tabel belanja yang sudah dinput
        self.table_belanja() 
        
        print(' ')
        #memasukkan nama item sebelumnya
        old_item = str(input('Nama Item Lama yang mau diganti : '))
        found = False
        for i in range(len(self.list_item)):
            #cek apakah ada di dalam nilai atribut list_item
            if old_item.upper() == self.list_item[i][0]:
                found = True #Jika Ada
                new_item = str(input('Input Item Baru : ')) #masukkan nama item baru yang ingin disimpan
                self.list_item[i][0] = new_item.upper() #menyimpan nama item yang baru, menggantikan nama item lama
                print(' ')

                while True:
                    #ingin melakukan update?
                    update_confirmation = str(input('Apakah Anda ingin mengganti Nama Item, Jumlah Item, atau Harga per Item yang sudah dimasukkan? (Yes / No) : '))
                    if update_confirmation.lower() == 'yes':
                        while True:
                            update_type = str(input('Bagian Mana yang ingin Anda Update? (Pilih Salah Satu : Item Name, Jumlah Item, Harga per Item) : '))
                            if update_type.title() == 'Item Name':
                                self.update_item_name()
                                break
                            elif update_type.title() == 'Jumlah Item':
                                self.update_item_qty()
                                break
                            elif update_type.title() == 'Harga Per Item':
                                self.update_item_price()
                                break
                            else:
                                print(' ')
                                print('⚠️Warning : ')
                                print('Mohon Maaf! Input yang Anda masukkan Tidak Terdaftar dalam Fitur Kami 🙏')
                                print('Silakan Coba Lagi! 🙏')
                                print(' ')
                        break
                    elif update_confirmation.lower() == 'no':
                        while True:
                            #ingin melakukan penghapusan item belanja yang sudah diinput?
                            deletion_order_confirmation = str(input('Apakah anda Ingin Menghapus Salah Satu Item Belanja Anda? (Yes/No) : '))
                            if deletion_order_confirmation.lower() == 'yes':
                                self.delete_item()
                                break
                            elif deletion_order_confirmation.lower() == 'no':
                                while True:
                                    #ingin melakukan cek order
                                    check_order_confirmation = str(input('Apakah anda Ingin Melakukan Pengecekan Item Belanja Anda? (Yes/No) : '))
                                    if check_order_confirmation.lower() == 'yes':
                                        self.check_order()
                                        break
                                    elif check_order_confirmation.lower() == 'no':
                                        while True:
                                            #ingin melakukan reset order?
                                            reset_order_confirmation = str(input('Apakah anda Ingin Reset Input Item Belanja Anda? (Yes/No) : '))
                                            if reset_order_confirmation.lower() == 'yes':
                                                self.reset_transaction()
                                                break
                                            elif reset_order_confirmation.lower() == 'no':
                                                while True:
                                                    #ingin menginput lagi item belanja?
                                                    input_again_confirmation = str(input('Apakah anda Ingin Melakukan Input Kembali Item Belanja Anda? (Yes/No) : '))
                                                    if input_again_confirmation.lower() == 'yes':
                                                        self.add_item()
                                                        break
                                                    elif input_again_confirmation.lower() == 'no':
                                                        #jika tidak ingin melakukan input item lagi
                                                        #dan tidak ingin menggunakan fasilitas lainnya
                                                        #maka langsung diarahkan ke method total_price() untuk mendapatkan harga keseluruhan
                                                        #beserta diskonnya (jika masuk kriteria diskon)
                                                        print(' ')
                                                        self.total_price()
                                                        print('Note : Jika ada yang ingin diinput kembali silakan buat ID Transaksi Baru 🙏🥰')
                                                        break
                                                                                                     
                                                    else: #ketika input tidak tertulis Yes dan No, maka akan diulangi kembali
                                                        print(' ')
                                                        print('⚠️Warning : ')
                                                        print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                                                        print(' ')
                                                break
                                            else:
                                                print(' ')
                                                print('⚠️Warning : ')
                                                print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                                                print(' ')
                                        break
                                    else:
                                        print(' ')
                                        print('⚠️Warning : ')
                                        print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                                        print(' ')
                                break
                            else:
                                print(' ')
                                print('⚠️Warning : ')
                                print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                                print(' ')
                        break
                    else:
                        print(' ')
                        print('⚠️Warning : ')
                        print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                        print(' ')
                break
                                      
        if found == False: #jika nama yang diinput salah maka harus melakukan input ulang!
            print('⚠️Warning : ')
            print('Input Nama Item Salah! 🙅')
            print('Penyebab : Nama Item sudah Diganti atau Tidak ada Dalam Input Item Belanja Anda 🥲')
            print('Silakan Ulangi! 🙏')
            self.update_item_name()
                                
    #Fitur Update Item Quantity---------------------------------Code by : Oktavio Reza Putra--------------------------------------------------------------------            
    def update_item_qty(self):
        print(' ')
        print(' ')
        print('🔖1️⃣ Fitur Update Item Quantity 1️⃣🔖')
        print('---------------------------------------------')
        #ditampilkan tabel input item belanja hasil input
        self.table_belanja()         
        print(' ')
        #input nama item sebelumnya yang ingin diganti jumlah item nya
        input_item = str(input('Nama Item yang ingin diganti Jumlah (Qty) Itemnya : '))
        found = False
        for i in range(len(self.list_item)):
            #apakah nama item yang dimasukkan di input_item ada di atribut list_item
            if input_item.upper() == self.list_item[i][0]:
                found = True
                new_qty = int(input('Input Jumlah (Qty) per Item Baru : '))
                self.list_item[i][1] = new_qty #menyimpan jumlah item baru
                self.list_item[i][3] = int(new_qty * self.list_item[i][2]) #dikalikan dengan harga per satuan item
                print(' ')

                while True:
                    #ingin melakukan update?
                    update_confirmation = str(input('Apakah Anda ingin mengganti Nama Item, Jumlah Item, atau Harga per Item yang sudah dimasukkan? (Yes / No) : '))
                    if update_confirmation.lower() == 'yes':
                        while True:
                            update_type = str(input('Bagian Mana yang ingin Anda Update? (Pilih Salah Satu : Item Name, Jumlah Item, Harga per Item) : '))
                            if update_type.title() == 'Item Name':
                                self.update_item_name()
                                break
                            elif update_type.title() == 'Jumlah Item':
                                self.update_item_qty()
                                break
                            elif update_type.title() == 'Harga Per Item':
                                self.update_item_price()
                                break
                            else:
                                print(' ')
                                print('⚠️Warning : ')
                                print('Mohon Maaf! Input yang Anda masukkan Tidak Terdaftar dalam Fitur Kami 🙏')
                                print('Silakan Coba Lagi! 🙏')
                                print(' ')
                        break
                    elif update_confirmation.lower() == 'no':
                        while True:
                            #ingin melakukan penghapusan item belanja yang sudah diinput?
                            deletion_order_confirmation = str(input('Apakah anda Ingin Menghapus Salah Satu Item Belanja Anda? (Yes/No) : '))
                            if deletion_order_confirmation.lower() == 'yes':
                                self.delete_item()
                                break
                            elif deletion_order_confirmation.lower() == 'no':
                                while True:
                                    #ingin melakukan cek order
                                    check_order_confirmation = str(input('Apakah anda Ingin Melakukan Pengecekan Item Belanja Anda? (Yes/No) : '))
                                    if check_order_confirmation.lower() == 'yes':
                                        self.check_order()
                                        break
                                    elif check_order_confirmation.lower() == 'no':
                                        while True:
                                            #ingin melakukan reset order?
                                            reset_order_confirmation = str(input('Apakah anda Ingin Reset Input Item Belanja Anda? (Yes/No) : '))
                                            if reset_order_confirmation.lower() == 'yes':
                                                self.reset_transaction()
                                                break
                                            elif reset_order_confirmation.lower() == 'no':
                                                while True:
                                                    #ingin menginput lagi item belanja?
                                                    input_again_confirmation = str(input('Apakah anda Ingin Melakukan Input Kembali Item Belanja Anda? (Yes/No) : '))
                                                    if input_again_confirmation.lower() == 'yes':
                                                        self.add_item()
                                                        break
                                                    elif input_again_confirmation.lower() == 'no':
                                                        #jika tidak ingin melakukan input item lagi
                                                        #dan tidak ingin menggunakan fasilitas lainnya
                                                        #maka langsung diarahkan ke method total_price() untuk mendapatkan harga keseluruhan
                                                        #beserta diskonnya (jika masuk kriteria diskon)
                                                        print(' ')
                                                        self.total_price()
                                                        print('Note : Jika ada yang ingin diinput kembali silakan buat ID Transaksi Baru 🙏🥰')
                                                        break
                                                                                                     
                                                    else: #ketika input tidak tertulis Yes dan No, maka akan diulangi kembali
                                                        print(' ')
                                                        print('⚠️Warning : ')
                                                        print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                                                        print(' ')
                                                break
                                            else:
                                                print(' ')
                                                print('⚠️Warning : ')
                                                print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                                                print(' ')
                                        break
                                    else:
                                        print(' ')
                                        print('⚠️Warning : ')
                                        print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                                        print(' ')
                                break
                            else:
                                print(' ')
                                print('⚠️Warning : ')
                                print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                                print(' ')
                        break
                    else:
                        print(' ')
                        print('⚠️Warning : ')
                        print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                        print(' ')
                break
                            
        if found == False: #jika nama yang diinput salah maka harus melakukan input ulang!
            print('⚠️Warning : ')
            print('Input Nama Item Salah! 🙅')
            print('Penyebab : Nama Item sudah Diganti atau Tidak ada Dalam Input Item Belanja Anda 🥲')
            print('Silakan Ulangi! 🙏')
            self.update_item_qty()                   
 

                                
    #Fitur Update Item Price---------------------------------Code by : Oktavio Reza Putra--------------------------------------------------------------------            
    def update_item_price(self):
        print(' ')
        print(' ')
        print('🏷️Fitur Update Item Price🏷️')
        print('---------------------------------------------')
        #ditampilkan tabel belanja hasil input
        self.table_belanja()
        print(' ')
        #input nama item yang ingin diganti harga per satua itemnya
        input_item = str(input('Nama Item yang ingin diganti Harga per Itemnya : '))           
        found = False
        for i in range(len(self.list_item)):
            #apakah item yang diinput ada di atribut list_item?
            if input_item.upper() == self.list_item[i][0]:
                found = True
                #jika ada maka masukkan harga per satuan item yang baru
                new_price = int(input('Input Harga per Item Baru : '))
                self.list_item[i][2] = new_price #masukkan harga per satuan item yang baru
                self.list_item[i][3] = int(new_price * self.list_item[i][1]) #dikalikan dengan jumlah item     
                print(' ')

                while True:
                    #ingin melakukan update?
                    update_confirmation = str(input('Apakah Anda ingin mengganti Nama Item, Jumlah Item, atau Harga per Item yang sudah dimasukkan? (Yes / No) : '))
                    if update_confirmation.lower() == 'yes':
                        while True:
                            update_type = str(input('Bagian Mana yang ingin Anda Update? (Pilih Salah Satu : Item Name, Jumlah Item, Harga per Item) : '))
                            if update_type.title() == 'Item Name':
                                self.update_item_name()
                                break
                            elif update_type.title() == 'Jumlah Item':
                                self.update_item_qty()
                                break
                            elif update_type.title() == 'Harga Per Item':
                                self.update_item_price()
                                break
                            else:
                                print(' ')
                                print('⚠️Warning : ')
                                print('Mohon Maaf! Input yang Anda masukkan Tidak Terdaftar dalam Fitur Kami 🙏')
                                print('Silakan Coba Lagi! 🙏')
                                print(' ')
                        break
                    elif update_confirmation.lower() == 'no':
                        while True:
                            #ingin melakukan penghapusan item belanja yang sudah diinput?
                            deletion_order_confirmation = str(input('Apakah anda Ingin Menghapus Salah Satu Item Belanja Anda? (Yes/No) : '))
                            if deletion_order_confirmation.lower() == 'yes':
                                self.delete_item()
                                break
                            elif deletion_order_confirmation.lower() == 'no':
                                while True:
                                    #ingin melakukan cek order
                                    check_order_confirmation = str(input('Apakah anda Ingin Melakukan Pengecekan Item Belanja Anda? (Yes/No) : '))
                                    if check_order_confirmation.lower() == 'yes':
                                        self.check_order()
                                        break
                                    elif check_order_confirmation.lower() == 'no':
                                        while True:
                                            #ingin melakukan reset order?
                                            reset_order_confirmation = str(input('Apakah anda Ingin Reset Input Item Belanja Anda? (Yes/No) : '))
                                            if reset_order_confirmation.lower() == 'yes':
                                                self.reset_transaction()
                                                break
                                            elif reset_order_confirmation.lower() == 'no':
                                                while True:
                                                    #ingin menginput lagi item belanja?
                                                    input_again_confirmation = str(input('Apakah anda Ingin Melakukan Input Kembali Item Belanja Anda? (Yes/No) : '))
                                                    if input_again_confirmation.lower() == 'yes':
                                                        self.add_item()
                                                        break
                                                    elif input_again_confirmation.lower() == 'no':
                                                        #jika tidak ingin melakukan input item lagi
                                                        #dan tidak ingin menggunakan fasilitas lainnya
                                                        #maka langsung diarahkan ke method total_price() untuk mendapatkan harga keseluruhan
                                                        #beserta diskonnya (jika masuk kriteria diskon)
                                                        print(' ')
                                                        self.total_price()
                                                        print('Note : Jika ada yang ingin diinput kembali silakan buat ID Transaksi Baru 🙏🥰')
                                                        break
                                                                                                     
                                                    else: #ketika input tidak tertulis Yes dan No, maka akan diulangi kembali
                                                        print(' ')
                                                        print('⚠️Warning : ')
                                                        print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                                                        print(' ')
                                                break
                                            else:
                                                print(' ')
                                                print('⚠️Warning : ')
                                                print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                                                print(' ')
                                        break
                                    else:
                                        print(' ')
                                        print('⚠️Warning : ')
                                        print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                                        print(' ')
                                break
                            else:
                                print(' ')
                                print('⚠️Warning : ')
                                print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                                print(' ')
                        break
                    else:
                        print(' ')
                        print('⚠️Warning : ')
                        print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                        print(' ')
                break
                         
        if found == False: #jika nama yang diinput salah maka harus melakukan input ulang!
            print('⚠️Warning : ')
            print('Input Nama Item Salah! 🙅')
            print('Penyebab : Nama Item sudah Diganti atau Tidak ada Dalam Input Item Belanja Anda 🥲')
            print('Silakan Ulangi! 🙏')
            self.update_item_price()                   
              
                
                
    #Fitur Menghapus List Item Belanja----------------------------Code by : Oktavio Reza Putra-------------------------------------------------------------------------                
    def delete_item(self):     
        print(' ')
        print(' ')
        print('-----------------------------------------------------------------------------------------')
        print('Fitur Delete Item')
        print('-----------------------------------------------------------------------------------------')
        #ditampilkan tabel belanja hasil input
        self.table_belanja()
        print(' ')
        #input item yang ingin dihapus
        input_item = str(input('Input Nama Item yang ingin Dihapus : '))
        found = False
        for i in range(len(self.list_item)):
            #mengecek apakah item yang dimasukkan ada di atribut list_item
            if input_item.upper() == self.list_item[i][0]:
                found = True
                #jika ada maka item yang dimasukkan akan dihapus beserta jumlah item, harga per satuan item 
                #dan total harga itemnya
                self.list_item.remove(self.list_item[i])
                print(' ')
                print('Terima kasih. Item yang Anda Input sudah Terhapus! 🙏')
                print(' ')

                while True:
                    #ingin melakukan update?
                    update_confirmation = str(input('Apakah Anda ingin mengganti Nama Item, Jumlah Item, atau Harga per Item yang sudah dimasukkan? (Yes / No) : '))
                    if update_confirmation.lower() == 'yes':
                        while True:
                            update_type = str(input('Bagian Mana yang ingin Anda Update? (Pilih Salah Satu : Item Name, Jumlah Item, Harga per Item) : '))
                            if update_type.title() == 'Item Name':
                                self.update_item_name()
                                break
                            elif update_type.title() == 'Jumlah Item':
                                self.update_item_qty()
                                break
                            elif update_type.title() == 'Harga Per Item':
                                self.update_item_price()
                                break
                            else:
                                print(' ')
                                print('⚠️Warning : ')
                                print('Mohon Maaf! Input yang Anda masukkan Tidak Terdaftar dalam Fitur Kami 🙏')
                                print('Silakan Coba Lagi! 🙏')
                                print(' ')
                        break
                    elif update_confirmation.lower() == 'no':
                        while True:
                            #ingin melakukan penghapusan item belanja yang sudah diinput?
                            deletion_order_confirmation = str(input('Apakah anda Ingin Menghapus Salah Satu Item Belanja Anda? (Yes/No) : '))
                            if deletion_order_confirmation.lower() == 'yes':
                                self.delete_item()
                                break
                            elif deletion_order_confirmation.lower() == 'no':
                                while True:
                                    #ingin melakukan cek order
                                    check_order_confirmation = str(input('Apakah anda Ingin Melakukan Pengecekan Item Belanja Anda? (Yes/No) : '))
                                    if check_order_confirmation.lower() == 'yes':
                                        self.check_order()
                                        break
                                    elif check_order_confirmation.lower() == 'no':
                                        while True:
                                            #ingin melakukan reset order?
                                            reset_order_confirmation = str(input('Apakah anda Ingin Reset Input Item Belanja Anda? (Yes/No) : '))
                                            if reset_order_confirmation.lower() == 'yes':
                                                self.reset_transaction()
                                                break
                                            elif reset_order_confirmation.lower() == 'no':
                                                while True:
                                                    #ingin menginput lagi item belanja?
                                                    input_again_confirmation = str(input('Apakah anda Ingin Melakukan Input Kembali Item Belanja Anda? (Yes/No) : '))
                                                    if input_again_confirmation.lower() == 'yes':
                                                        self.add_item()
                                                        break
                                                    elif input_again_confirmation.lower() == 'no':
                                                        #jika tidak ingin melakukan input item lagi
                                                        #dan tidak ingin menggunakan fasilitas lainnya
                                                        #maka langsung diarahkan ke method total_price() untuk mendapatkan harga keseluruhan
                                                        #beserta diskonnya (jika masuk kriteria diskon)
                                                        print(' ')
                                                        self.total_price()
                                                        print('Note : Jika ada yang ingin diinput kembali silakan buat ID Transaksi Baru 🙏🥰')
                                                        break
                                                                                                     
                                                    else: #ketika input tidak tertulis Yes dan No, maka akan diulangi kembali
                                                        print(' ')
                                                        print('⚠️Warning : ')
                                                        print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                                                        print(' ')
                                                break
                                            else:
                                                print(' ')
                                                print('⚠️Warning : ')
                                                print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                                                print(' ')
                                        break
                                    else:
                                        print(' ')
                                        print('⚠️Warning : ')
                                        print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                                        print(' ')
                                break
                            else:
                                print(' ')
                                print('⚠️Warning : ')
                                print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                                print(' ')
                        break
                    else:
                        print(' ')
                        print('⚠️Warning : ')
                        print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                        print(' ')
                break
                               
        if found == False: #jika nama yang diinput salah maka harus melakukan input ulang!
            print('⚠️Warning : ')
            print('Input Nama Item Salah! 🙅')
            print('Penyebab : Nama Item sudah Diganti atau Tidak ada Dalam Input Item Belanja Anda 🥲')
            print('Silakan Ulangi! 🙏')
            self.delete_item() 

        
        
    #Fitur Reset Transaction----------------------------------------Code by : Oktavio Reza Putra-------------------------------------------------------------    
    def reset_transaction(self):
        print(' ')
        print(' ')
        print('-----------------------------------------------------------------------------------------')
        print('Fitur Reset Transaction')
        print('-----------------------------------------------------------------------------------------')
        #menghapus semua item pada atribut list_item
        self.list_item.clear()
        
        #diberikan opsi untuk input kembali item belanja lagi
        confirmation_input = str(input('Ingin Melakukan Input kembali Item Belanja? (Yes / No) : '))
            
        if confirmation_input.lower() == 'yes':
            self.add_item()
            
        elif confirmation_input.lower() == 'no':
            self.table_belanja()
            
        else: #selain yes dan no tidak valid, maka harus kembali ke confirmation input
            print("Input tidak valid. Harap masukkan Yes atau No. 🙏")
            self.reset_transaction()
    
    #Fitur Cek Transaksi-------------------------------------------Code by : Oktavio Reza Putra----------------------------------------------------------                
    def check_order(self):
        print(' ')
        print(' ')
        print('-----------------------------------------------------------------------------------------')
        print('Fitur Check Order')
        print('-----------------------------------------------------------------------------------------')
        for i in range(len(self.list_item)):
            #ditampilkan tabel belanja hasil input
            self.table_belanja()
            if self.list_item[i][0] != '': #jika nama item tidak kosong
                print('Silakan Cek apakah Data Anda Sudah Benar?')
                print(' ')
                while True:
                    #diberikan opsi update item lagi
                    update_item_again = str(input('Apakah ingin Melakukan Update Item Belanja Lagi? (Yes/No) : '))
                    if update_item_again.lower() == 'yes': #jika iya
                        print(' ')
                        while True:
                            update_type = str(input('Bagian Mana yang ingin Anda Update? (Pilih Salah Satu : Item Name, Jumlah Item, Harga per Item) : '))
                            if update_type.title() == 'Item Name':
                                self.update_item_name()
                                break
                            elif update_type.title() == 'Jumlah Item':
                                self.update_item_qty()
                                break
                            elif update_type.title() == 'Harga Per Item':
                                self.update_item_price()
                                break
                            else:
                                print(' ')
                                print('⚠️Warning : ')
                                print('Mohon Maaf! Input yang Anda masukkan Tidak Terdaftar dalam Fitur Kami 🙏')
                                print('Silakan Coba Lagi! 🙏')
                                print(' ')
                        break                        
                    elif update_item_again.lower() == 'no': #jika tidak
                        while True:
                            #diberikan opsi hapus item
                            deletion_order_confirmation = str(input('Apakah anda Ingin Menghapus Salah Satu Item Belanja Anda? (Yes/No) : '))
                            if deletion_order_confirmation.lower() == 'yes':
                                self.delete_item()
                                break
                            elif deletion_order_confirmation.lower() == 'no':
                                while True:
                                    #diberikan opsi reset order
                                    reset_order_confirmation = str(input('Apakah anda Ingin Reset Input Item Belanja Anda? (Yes/No) : '))
                                    if reset_order_confirmation.lower() == 'yes':
                                        self.reset_transaction()
                                        break
                                    elif reset_order_confirmation.lower() == 'no':
                                        while True:
                                            #diberikan opsi input item lagi
                                            input_again_confirmation = str(input('Apakah anda Ingin Melakukan Input Kembali Item Belanja Anda? (Yes/No) : '))
                                            if input_again_confirmation.lower() == 'yes':
                                                self.add_item()
                                                break
                                            elif input_again_confirmation.lower() == 'no':
                                                print(' ')
                                                print('Yeay!👏🏼👏🏼👏🏼')
                                                print("🚀Selamat! Pesanan sudah Benar!🚀")
                                                print(' ')
                                                print(' ')
                                                self.total_price()
                                                print(' ')
                                                print('Note : Jika ada yang ingin diinput kembali silakan buat ID Transaksi Baru 🙏🥰')
                                                break
                                            else:
                                                print(' ')
                                                print('⚠️Warning : ')
                                                print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                                                print(' ')
                                        break
                                    else:
                                        print(' ')
                                        print('⚠️Warning : ')
                                        print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                                        print(' ')
                                break
                            else:
                                print(' ')
                                print('⚠️Warning : ')
                                print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                                print(' ')
                        break
                    else:
                        print(' ')
                        print('⚠️Warning : ')
                        print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                        print(' ')
                break
                                        
            elif self.list_item[i][0] == '': #jika nama item kosong
                print(' ')
                print('Yahh... Terdapat kesalahan input data nih! 🥲')
                print(' ')
                print('Silakan Bisa Menghapus Item Belanja, Reset Input Item Belanja atau Melakukan Input Kembali')
                print('Opsi Melakukan Input Kembali bisa Anda lakukan jika ingin melakukan input Belanja kembali sebelum menghapus input yang nama item nya kosong 🙏')
                print(' ')
                while True:
                    #diberikan opsi menghapus item
                    deletion_order_confirmation = str(input('Apakah anda Ingin Menghapus Salah Satu atau Seluruh Item Belanja Anda? (Yes/No) : '))
                    if deletion_order_confirmation.lower() == 'yes':
                        self.delete_item()
                        break
                    elif deletion_order_confirmation.lower() == 'no':
                        while True:
                            #diberikan opsi reset transaksi
                            reset_order_confirmation = str(input('Apakah anda Ingin Reset Input Item Belanja Anda? (Yes/No) : '))
                            if reset_order_confirmation.lower() == 'yes':
                                self.reset_transaction()
                                break
                            elif reset_order_confirmation.lower() == 'no':
                                while True:
                                    #diberikan opsi untuk input item belanja lagi sebelum menghapus nama item yang kosong
                                    input_again_confirmation = str(input('Apakah anda Ingin Melakukan Input Kembali Item Belanja Anda? (Yes/No) : '))
                                    if input_again_confirmation.lower() == 'yes':
                                        self.add_item()
                                        break
                                    elif input_again_confirmation.lower() == 'no':
                                        print(' ')
                                        print(' ')
                                        self.total_price()
                                        break
                                    else:
                                        print(' ')
                                        print('⚠️Warning : ')
                                        print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                                        print(' ')
                                break
                            else:
                                print(' ')
                                print('⚠️Warning : ')
                                print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                                print(' ')
                        break
                    else:
                        print(' ')
                        print('⚠️Warning : ')
                        print("Jawaban tidak valid. Silakan jawab 'Yes' atau 'No'.")
                        print(' ')                      
    
    #Fitur Melihat Total Harga Keseluruhan
    def total_price(self):
        total_transaksi = 0 #menyimpan niali total transaksi
        total_transaksi_sebelum_diskon = [] #menyimpan list transaksi sebelum diskon
        total_diskon = [] #menyimpan list total_diskon
        total_transaksi_final = [] #total transaksi final setelah dikurangi diskon
        for i in range(len(self.list_item)):
            total_transaksi += self.list_item[i][3]

        if total_transaksi > 500000: #jika transaksi di atas 500 ribu
            total_transaksi_sebelum_diskon = ['', 'Total Harga :','',total_transaksi]
            total_diskon = ['','Diskon:','10%',int((total_transaksi * 0.1) * (-1))]
            total_transaksi_final = ['', 'Total Harga Setelah Diskon:', '(Disc 10%)',int(total_transaksi - (total_transaksi * 0.1))]

        elif total_transaksi > 300000: #jika transaksi di atas 300 ribu
            total_transaksi_sebelum_diskon = ['', 'Total Harga :','',total_transaksi] 
            total_diskon = ['','Diskon:','8%',int((total_transaksi * 0.08) * (-1))]
            total_transaksi_final = ['', 'Total Harga Setelah Diskon : ','(Disc 8%)',int(total_transaksi - (total_transaksi * 0.08))]

        elif total_transaksi > 200000: #jika transaksi di atas 200 ribu
            total_transaksi_sebelum_diskon = ['', 'Total Harga :','',total_transaksi]
            total_diskon = ['','Diskon:','5%',int((total_transaksi * 0.05) * (-1))]
            total_transaksi_final = ['','Total Harga Setelah Diskon : ' , '(Disc 5%)',int(total_transaksi - (total_transaksi * 0.05))]

        elif total_transaksi <= 200000: #jika transaksi di bawah atau sama dengan 200 ribu
            total_transaksi_sebelum_diskon = ['', 'Total Harga :','',total_transaksi]
            total_diskon = ['','Diskon:','0%','']
            total_transaksi_final =['', 'Total Harga Setelah Diskon : ', '(No Disc)', int(total_transaksi)]
            
        self.list_item.append(total_transaksi_sebelum_diskon) #menambahkan listl transaksi sebelum diskon
        self.list_item.append(total_diskon) #menambah list  diskon
        self.list_item.append(total_transaksi_final) #menambah list total transaksi final
        self.table_belanja() #menampilkan nota transaksi dalam bentuk tabel
        
        
    #Fitur Menampilkan Tabel List Item Belanja----------------------------Code by : Oktavio Reza Putra-------------------------------------------------------------------------                
    def table_belanja(self):
        print(' ')
        print('‧₊˚ ☁️⋅♡🪐༘⋆---Supermarket Cak Andi---‧₊˚ ☁️⋅♡🪐༘⋆')
        print('Berikut adalah List Transaksi yang dibeli :')
        #membuat variabel header untuk menyimpan niali yang digunakan sebagai nama kolom
        header = ['Item', 'Jumlah Item', 'Harga per Item (Rp)','Total Harga Keseluruhan (Rp)']
        
        #membuat variabel tabel untuk menyimpan nilai di dalam atribut list_item
        table = tabulate(self.list_item, header, tablefmt='grid')
        
        #menampilkan tabel input belanja atau nota transaksi
        print(table)