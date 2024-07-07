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
   ![Screenshot 2024-07-07 192214](https://github.com/oktaviorezap/Super_Cashier_Final_Project_Python_Pacmann/assets/98758499/98c410a2-fc20-4cf9-958f-fd8bde04a008)

2. Method add_item()
   <br> Method add_item digunakan untuk menginput satu atau lebih item Belanja yang meliputi nama item, jumlah item dan harga per satuan item
   <br>Setelah melakukan input item belanja, maka customer akan diarahkan untuk melakukan update item, menghapus item, melakukan reset transaksi, melakukan pengecekan transaksi dan opsi untuk kembali melakukan input item belanja 
   <br>![Screenshot 2024-07-07 193327](https://github.com/oktaviorezap/Super_Cashier_Final_Project_Python_Pacmann/assets/98758499/719c51cf-8ad2-4752-ab29-1d50806d0ebf)
   <br>
   <br>![Screenshot 2024-07-07 193441](https://github.com/oktaviorezap/Super_Cashier_Final_Project_Python_Pacmann/assets/98758499/baf6f810-0dd3-4f68-b597-24def9ac2faa)
