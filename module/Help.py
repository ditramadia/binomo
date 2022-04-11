# HELP MODULE

def callHelp(currentState):
    print('============ HELP ===========')
    if (currentState[1][4] == "user"):
        print('''
1. login - Untuk melakukan login ke dalam sistem
2. list_game_toko - Untuk menampilkan daftar game dengan sorting
3. search_game_at_store - Untuk mencari game di toko
4. buy_game - Untuk membeli game
5. list_game - Untuk menampilkan daftar game yang dimiliki
6. search_my_game - Untuk mencari game yang dimiliki
7. riwayat - Untuk melihat riwayat pembelian
8. save - Untuk menyimpan data
9. help - Untuk menampilkan daftar perintah
10. exit - Untuk keluar dari aplikasi
''')
    elif (currentState[1][4] == "admin"):
        print('''
1. login - Untuk melakukan login ke dalam sistem
2. register - Untuk menambahkan akun ke dalam sistem
3. list_game_toko - Untuk menampilkan daftar game dengan sorting
4. search_game_at_store - Untuk mencari game di toko
5. tambah_game - Untuk menambahkan game ke dalam daftar game toko
6. ubah_game - Untuk mengubah informasi game dalam daftar game toko
7. ubah_stok - Untuk mengubah stok game dalam daftar game toko
8. topup - Untuk menambah saldo suatu akun
9. save - Untuk menyimpan data
10. help - Untuk menampilkan daftar perintah
11. exit - Untuk keluar dari aplikasi
''')
    else:
        print('''
1. login - Untuk melakukan login ke dalam sistem
2. save - Untuk menyimpan data
3. help - Untuk menampilkan daftar perintah
4. exit - Untuk keluar dari aplikasi
''')
