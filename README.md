# Python Final Project : Super Cashier - Pacmann AI
**Background Project :**

**Business Problem :** Andi ingin membuat sistem kasir self-service untuk supermarket miliknya. Sehingga, Andi membutuhkan programmer yang bisa membuat fitur-fitur yang dibutuhkan supaya sistem kasir self-service di supermarket nya berjalan dengan lancar. 

**Solution Problem :** Membuat sistem program kasir self-service dimana customer bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli dan harga item yang dibeli dan fitur yang lain. 

# Proses dan Fungsi yang dibutuhkan
1. Sistem untuk menambahkan item dengan quantity (qty) dan price per item dengan **method add_item()**
2. Sistem untuk Update nama Item dengan **method update_item_name()**
3. Sistem untuk Update Quantity (qty) dengan **method update_item_qty()**
4. Sistem untuk Update Price dengan **method update_item_price()**
5. Sistem untuk Menghapus Item dengan **method delete_item()**
6. Sistem untuk melakukan Reset pada Order dengan **method reset_transaction()**
7. Melakukan check pada Order dengan **method check_order()**

8. Sistem untuk menghitung total price dan diskon dengan **method total_price()**
9. Fitur Tambahan : Sistem untuk menapilkan Tabel Item Belanja seperti Nota Sederhana dengan **method table_belanja()**

# Super Cashier Project Flowchart
<img width="1075" alt="final project-super cashier-python-oktavio reza putra" src="https://github.com/oktaviorezap/Super_Cashier_Final_Project_Python_Pacmann/assets/98758499/a74b8ca0-33f4-4052-a785-b33e721133e6">

# Snippet Code
Berisi penjelasan atribut dan fungsi yang digunakan dalam sistem fungsi super cashier ini
1. Final Project ini menggunakan module yang dinamakan cashier.py
2. cashier.py berisi class yang bernama Transaction() 

Penjelasan fungsi dan atribut adalah sebagai berikut:
1. **Class Transaction()**
   <br>Berisi Method dan atribut yang digunakan untuk menjalankan Program Super Cashier
   <br>Class Transaction() memiliki atribut yang bernama list_item yang digunakan untuk menyimpan input item belanja yang dimasukkan oleh customer
   <br>![Screenshot 2024-07-07 192214](https://github.com/oktaviorezap/Super_Cashier_Final_Project_Python_Pacmann/assets/98758499/98c410a2-fc20-4cf9-958f-fd8bde04a008)

3. Method add_item()
   <br> Method add_item digunakan untuk menginput satu atau lebih item Belanja yang meliputi nama item, jumlah item dan harga per satuan item
   <br>Setelah melakukan input item belanja, maka customer akan diarahkan untuk melakukan update item, menghapus item, melakukan reset transaksi, melakukan pengecekan transaksi dan opsi untuk kembali melakukan input item belanja 
   <br>
   <br>
   ```python
    #Fitur Add Item Belanja------------------------------------------------------------------------------------------------------------------------------
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
                        
                        #ingin melakukan update?
                        update_confirmation = str(input('Apakah Anda ingin mengganti Nama Item, Jumlah Item, atau Harga per Item yang sudah dimasukkan? (Yes / No) : '))
                        if update_confirmation.lower() == 'yes':
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
                        elif update_confirmation.lower() == 'no':
                            #ingin melakukan penghapusan item belanja yang sudah diinput?
                            deletion_order_confirmation = str(input('Apakah anda Ingin Menghapus Salah Satu Item Belanja Anda? (Yes/No) : '))
                            if deletion_order_confirmation.lower() == 'yes':
                                self.delete_item()
                                break
                            elif deletion_order_confirmation.lower() == 'no':
                                #ingin melakukan cek order
                                check_order_confirmation = str(input('Apakah anda Ingin Melakukan Pengecekan Item Belanja Anda? (Yes/No) : '))
                                if check_order_confirmation.lower() == 'yes':
                                    self.check_order()
                                    break
                                elif check_order_confirmation.lower() == 'no':
                                    #ingin melakukan reset order?
                                    reset_order_confirmation = str(input('Apakah anda Ingin Reset Input Item Belanja Anda? (Yes/No) : '))
                                    if reset_order_confirmation.lower() == 'yes':
                                        self.reset_transaction()
                                        break
                                    elif reset_order_confirmation.lower() == 'no':
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
                                            print(' ')
                                            print('Note : Jika ada yang ingin diinput kembali silakan buat ID Transaksi Baru 🙏🥰')
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
                    print('Input Jumlah Item, Harga per Satuan Item tidak boleh kosong')
                    print('atau diinput dengan nilai selain angka!')
                    print('Silakan Ulangi Kembali Input Item Belanja Anda! 🙏')
                    self.add_item()
                    
        elif input_item.lower()=='no': #jika tidak ingin menginput item belanja untuk pertama kalinya
            if self.list_item != []: #jika list sebelumnya sudah terisi?
                #ingin menghapus item belanja?
                deletion_order_confirmation = str(input('Apakah anda Ingin Menghapus Salah Satu Item Belanja Anda? (Yes/No) : '))
                if deletion_order_confirmation.lower() == 'yes':
                    self.delete_item()
                    pass
                elif deletion_order_confirmation.lower() == 'no':
                    #ingin cek order?
                    check_order_confirmation = str(input('Apakah anda Ingin Melakukan Pengecekan Item Belanja Anda? (Yes/No) : '))
                    if check_order_confirmation.lower() == 'yes':
                        self.check_order()
                        pass
                    elif check_order_confirmation.lower() == 'no':
                        #ingin reset order?
                        reset_order_confirmation = str(input('Apakah anda Ingin Reset Input Item Belanja Anda? (Yes/No) : '))
                        if reset_order_confirmation.lower() == 'yes':
                            self.reset_transaction()
                            pass
                        elif reset_order_confirmation.lower() == 'no':
                            print(' ')
                            print(' ')
                            self.total_price()
                            pass
                        
            elif self.list_item == []: #jika list sebelumnya kosong? atau tidak jadi mengisi untuk pertama kalinya
                self.table_belanja()
                pass
        
        else: #ketika input ingin input belanja tidak terisi yes atau no
            print('Input Salah! Silakan Ulangi Kembali! 🙏')
            self.add_item()            
    
    
    #Fitur Update Item Name-----------------------------------------------------------------------------------------------------
    def update_item_name(self):
        print(' ')
        print(' ')
        print('🛍️ Fitur Update Item Name 🛍️')
        print('---------------------------------------------')
        self.table_belanja() 
        print(' ')
        old_item = str(input('Nama Item Lama yang mau diganti : '))
        found = False
        for i in range(len(self.list_item)):
            if old_item.upper() == self.list_item[i][0]:
                found = True
                new_item = str(input('Input Item Baru : '))
                self.list_item[i][0] = new_item.upper()
                print(' ')
                    
                update_item_again = str(input('Apakah ingin Melakukan Update Item Belanja Lagi? (Yes/No) : '))
                if update_item_again.lower() == 'yes':
                    print(' ')
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
                        
                elif update_item_again.lower() == 'no':
                    deletion_order_confirmation = str(input('Apakah anda Ingin Menghapus Salah Satu Item Belanja Anda? (Yes/No) : '))
                    if deletion_order_confirmation.lower() == 'yes':
                        self.delete_item()
                        break
                    elif deletion_order_confirmation.lower() == 'no':
                        check_order_confirmation = str(input('Apakah anda Ingin Melakukan Pengecekan Item Belanja Anda? (Yes/No) : '))
                        if check_order_confirmation.lower() == 'yes':
                            self.check_order()
                            break
                        elif check_order_confirmation.lower() == 'no':
                            reset_order_confirmation = str(input('Apakah anda Ingin Reset Input Item Belanja Anda? (Yes/No) : '))
                            if reset_order_confirmation.lower() == 'yes':
                                self.reset_transaction()
                                break
                            elif reset_order_confirmation.lower() == 'no':
                                input_again_confirmation = str(input('Apakah anda Ingin Melakukan Input Kembali Item Belanja Anda? (Yes/No) : '))
                                if input_again_confirmation.lower() == 'yes':
                                    self.add_item()
                                    break
                                elif input_again_confirmation.lower() == 'no':
                                    print(' ')
                                    print(' ')
                                    self.total_price()
                                    print(' ')
                                    print('Note : Jika ada yang ingin diinput kembali silakan buat ID Transaksi Baru 🙏🥰')
                                    break                

        if found == False:
            print('⚠️Warning : ')
            print('Input Nama Item Salah! 🙅')
            print('Penyebab : Nama Item sudah Diganti atau Tidak ada Dalam Input Item Belanja Anda 🥲')
            print('Silakan Ulangi! 🙏')
            self.update_item_name()
   ```
3. Method update_item_name()
   <br>Method update_item_name() digunakan untuk melakukan input pada nama item
   <br>Cara kerjanya adalah sebagai berikut:
   <br> a. Menginput nama item sebelumnya diinput dalam method add_item() dan disimpan pada atribut list_item
 
      
