# Program Loyalty Point System
# Sistem poin loyalitas sederhana dengan fitur registrasi akun, akumulasi poin, dan penukaran hadiah.

# KAMUS
# data_nama, data_points, data_transaksi : array [100...199] of int
# data_nama, data_password : array [100...199] of string
# id_awal, command_awal, id_customer, menu, harga, uang, pake_voucher, diskon, tukar_voucher : int
# password, temp : string

# ALGORITMA
import os

if os.name == 'nt':
    co = lambda: os.system('cls')
else:
    co = lambda: os.system('clear')

# DATA UMUM - Deklarasi data yang diperlukan
data_nama = ['belum ada data' for i in range(100,200)]
data_voucher = [0 for i in range(100,200)]
data_points = [0 for i in range(100,200)]
data_transaksi = [0 for i in range(100,200)]
data_password = ['pwdefault' for i in range(100,200)]
id_awal = 100

# PROGRAM
while True:
    # Bagian Awal dengan 3 pilihan yang tersedia, jika input tidak valid maka akan diulang perintahnya
    while(True):
        # MAIN MENU
        if data_nama[0] == "belum ada data":
            print("Silahkan membuat membership baru terlebih dahulu jika belum memiliki akun. \n")
        print("\033[1m\x1B[4m" + 'MAIN MENU' + "\x1B[0m")
        command_awal = input('1. Menu Transaksi\n2. Buat membership baru\n3. Keluar Aplikasi\nMasukkan pilihan: ')
        if not command_awal.isdigit():
            co()
            print("Input tidak valid, silahkan masukkan angka.\n")
            continue
        command_awal = int(command_awal)
        break

    # CEK ID & PW
    if command_awal == 1:
        co()
        while True :
            print("\033[1m\x1B[4m" + 'LOGIN' + "\x1B[0m")
            id_customer = input('ID: ')
            if not id_customer.isdigit():
                co()
  
                print('Input ID tidak valid, silakan masukkan angka.\n')
                continue
            id_customer = int(id_customer)
            if not 100 <= id_customer <= 199:
                co()
                print('ID yang anda masukkan tidak valid, ID dalam rentang 100 hingga 199')
                continue
            break

        password = str(input('Password: '))
        while not password:
            co()
            print("\033[1m\x1B[4m" + 'TRANSAKSI' + "\x1B[0m")
            print('Password tidak boleh kosong.')
            password = str(input('Password: '))

        # MENU TRANSAKSI
        if password == data_password[id_customer - 100]:
            co()
            while True:
                if data_transaksi[id_customer - 100] < 1000000:
                    status = 'Bronze'
                elif 1000000 <= data_transaksi[id_customer - 100] <= 5000000:
                    status = 'Silver'
                else:
                    status = 'Gold'

                print("\033[1m\x1B[4m" + 'MENU TRANSAKSI' + "\x1B[0m")
                print('1. Payment\n2. Reedem Points\n3. Cek Points, Voucher, and Loyalty Status\n4. Kembali ke Main Menu\n')
                while(True):
                    menu = input('Masukkan pilihan anda: ')
                    if not menu.isdigit():
                        co()
                        print("\033[1m\x1B[4m" + 'MENU TRANSAKSI' + "\x1B[0m")
                        print('1. Payment\n2. Reedem Points\n3. Cek Points, Voucher, and Loyalty Status\n4. Kembali\n')
                        print('\033[3mInput tidak valid, silakan masukkan angka.\033[0m')
                        continue
                    menu = int(menu)
                    break

                # PAYMENT
                if menu == 1:
                    co()
                    print("\033[1m\x1B[4m" + 'PAYMENT' + "\x1B[0m")
                    while True:
                        harga = input('Nominal pembelian: Rp')
                        uang = input('Nominal pembayaran: Rp')
                        if not harga.isdigit() or not uang.isdigit():
                            co()
                            print('\033[3mInput nominal tidak valid, silakan masukkan angka.\033[0m')
                            continue
                        harga = int(harga)
                        uang = int(uang)
                        break
                    print(f'\nAnda memiliki voucher senilai \033[1mRp{data_voucher[id_customer - 100]:,}\033[0m')
                    print('Apakah anda akan menggunakan voucher untuk transaksi kali ini? *\033[3mhanya bisa memilih yang ada di pilihan\033[0m')
                    print('1. Diskon Rp. 50,000\n2. Diskon Rp. 100,000\n3. Diskon Rp. 200,000\n4. Transaksi tanpa voucher\n')
                    while True:
                        pake_voucher = input('Masukkan pilihan anda: ')
                        if not pake_voucher.isdigit():
                            co()
                            print(f'\nAnda memiliki voucher senilai \033[1mRp{data_voucher[id_customer - 100]:,}\033[0m')
                            print('Apakah anda akan menggunakan voucher untuk transaksi kali ini? *\033[3mhanya bisa memilih yang ada di pilihan\033[0m')
                            print('1. Diskon Rp. 50,000\n2. Diskon Rp. 100,000\n3. Diskon Rp. 200,000\n4. Transaksi tanpa voucher\n')
                            print('\033[3mInput pilihan voucher tidak valid, silakan masukkan angka.\033[0m')
                            continue
                        pake_voucher = int(pake_voucher)
                        break

                    diskon = 0
                    if pake_voucher == 1:
                        diskon = 50000
                    elif pake_voucher == 2:
                        diskon = 100000
                    elif pake_voucher == 3:
                        diskon = 200000
                    elif pake_voucher == 4:
                        diskon = 0
                    else:
                        co()
                        print('Input tidak valid, transaksi akan dilanjutkan tanpa voucher.')
                        diskon = 0

                    # CEK VOUCHER
                    if data_voucher[id_customer - 100] >= diskon:
                        if diskon <= harga:
                            if harga - diskon <= uang:
                                data_transaksi[id_customer - 100] += (harga - diskon)
                                data_points[id_customer- 100] += (harga - diskon)//1000
                                data_voucher[id_customer - 100] -= diskon
                                co()
                                print(f'Anda telah melakukan pembelian dengan nominal \033[1mRp{harga - diskon:,}\033[0m (setelah diskon)\nKembalian: Rp{uang - harga + diskon:,}\nPoints: +{(harga - diskon)//1000} points\nCurrent Points: {data_points[id_customer - 100]} points\n')
                                x=input('Tekan ENTER untuk kembali ke Menu Transaksi... ')
                                co()
                            else:
                                co()
                                print('Uang anda tidak mencukupi, anda akan dikembalikan ke Main Menu\n')
                        else:
                            co()
                            print('Nominal diskon lebih besar dari harga pembelian, kembali ke Main Menu\n')

                    # PEMBELIAN
                    elif 0 <= data_voucher[id_customer - 100] < diskon:
                        co()
                        print('Saldo voucher anda tidak mencukupi/voucher tidak valid\ntransaksi akan dilanjutkan tanpa voucher')
                        if harga <= uang:
                            data_transaksi[id_customer - 100] += harga
                            data_points[id_customer - 100] += harga//1000
                            print(f'Anda telah melakukan pembelian dengan nominal \033[1mRp{harga:,}\033[0m\nKembalian: Rp{uang - harga:,}\nPoints: +{harga//1000} points\nCurrent Points: {data_points[id_customer - 100]} points\n')
                            input('Tekan ENTER untuk kembali ke Menu Transaksi... ')
                            co()
                        else:
                            co()
                            print('Uang anda tidak mencukupi, anda akan dikembalikan ke Main Menu\n')
                    else:
                        if harga <= uang:
                            data_transaksi[id_customer - 100] += harga
                            data_points[id_customer - 100] += harga//1000
                            co()
                            print(f'Anda telah melakukan pembelian dengan nominal \033[1mRp{harga:,}\033[0m\nKembalian: Rp{uang - harga:,}\nPoints: +{harga//1000} points\nCurrent Points: {data_points[id_customer - 100]} points\n')
                            input('Tekan ENTER untuk kembali ke Menu Transaksi... ')
                            co()
                        else:
                            co()
                            print('Uang anda tidak mencukupi, anda akan dikembalikan ke Main Menu\n')

                # REDEEM POINTS
                elif menu == 2:
                    co()
                    print("\033[1m\x1B[4m" + 'REDEEM POINTS' + "\x1B[0m")
                    print(f'Anda memiliki \033[1m{data_points[id_customer - 100]}\033[0m points\n')
                    print('Pilih jenis voucher (Voucher bersifat akumulatif):\n1. Voucher diskon Rp. 50,000 (500 points)\n2. Voucher diskon Rp. 100,000 (950 points)\n3. Voucher diskon Rp. 200,000 (1800 points)')
                    while True:
                        tukar_voucher = input('Masukkan pilihan anda: ')
                        if not tukar_voucher.isdigit():
                            co()
                            print("\033[1m\x1B[4m" + 'REDEEM POINTS' + "\x1B[0m")
                            print(f'Anda memiliki \033[1m{data_points[id_customer - 100]}\033[0m points\n')
                            print('Pilih jenis voucher (Voucher bersifat akumulatif):\n1. Voucher diskon Rp. 50,000 (500 points)\n2. Voucher diskon Rp. 100,000 (950 points)\n3. Voucher diskon Rp. 200,000 (1800 points)')
                            print('\033[3mInput pilihan voucher tidak valid, silakan masukkan angka.\033[0m')
                            continue
                        tukar_voucher = int(tukar_voucher)
                        break

                    if tukar_voucher == 1:
                        if data_points[id_customer - 100] >= 500:
                            data_voucher[id_customer - 100] += 50000
                            data_points[id_customer - 100] -= 500
                            co()
                            print("\033[1m\x1B[4m" + 'REDEEM POINTS' + "\x1B[0m")
                            print(f'Reedem points berhasil, Total points anda: {data_points[id_customer - 100]} points')
                            input('\nTekan ENTER untuk kembali ke Menu Transaksi... ')
                            co()
                        else:
                            co()
                            print('Points anda tidak mencukupi.\n')
                            input('\nTekan ENTER untuk kembali ke Menu Transaksi... ')
                            co()
                    elif tukar_voucher == 2:
                        if data_points[id_customer - 100] >= 950:
                            data_voucher[id_customer - 100] += 100000
                            data_points[id_customer - 100] -= 950
                            co()
                            print("\033[1m\x1B[4m" + 'REDEEM POINTS' + "\x1B[0m")
                            print(f'Reedem points berhasil, Total points anda: {data_points[id_customer - 100]} points')
                            input('\nTekan ENTER untuk kembali ke Menu Transaksi... ')
                            co()
                        else:
                            co()
                            print("\033[1m\x1B[4m" + 'REDEEM POINTS' + "\x1B[0m")
                            print('Points anda tidak mencukupi.\n')
                            input('\nTekan ENTER untuk kembali ke Menu Transaksi... ')
                            co()
                    elif tukar_voucher == 3:
                        if data_points[id_customer - 100] >= 1800:
                            data_voucher[id_customer - 100] += 200000
                            data_points[id_customer - 100] -= 1800
                            co()
                            print("\033[1m\x1B[4m" + 'REDEEM POINTS' + "\x1B[0m")
                            print(f'Reedem points berhasil, Total points anda: {data_points[id_customer - 100]} points')
                            input('\nTekan ENTER untuk kembali ke Menu Transaksi... ')
                            co()
                        else:
                            co()
                            print("\033[1m\x1B[4m" + 'REDEEM POINTS' + "\x1B[0m")
                            print('Points anda tidak mencukupi.\n')
                            input('\nTekan ENTER untuk kembali ke Menu Transaksi... ')
                            co()
                    else:
                        co()
                        print("\033[1m\x1B[4m" + 'REDEEM POINTS' + "\x1B[0m")
                        print('Input tidak valid.\n')
                        input('\nTekan ENTER untuk kembali ke Menu Transaksi... ')
                        co()                        

                # CEK PROFIL
                elif menu == 3:
                    co()
                    print("\033[1m\x1B[4m" + 'PROFILE' + "\x1B[0m")
                    print(f'Halo \033[1m{data_nama[id_customer - 100]}\033[0m\nCurrent Points: {data_points[id_customer - 100]} points\nVoucher: Rp{data_voucher[id_customer - 100]:,} (voucher bersifat akumulatif)\nLoyalty Status: {status}\n')
                    input('Tekan ENTER untuk kembali ke Menu Transaksi... ')
                    co()
                elif menu == 4:
                    co()
                    break
                else:
                    co()
                    print('Pilih menu yang tersedia.\n')
            else:
                co()
                print('Password yang anda masukkan salah, anda akan dikembalikan ke Main Menu\n')

    # BUAT AKUN
    elif command_awal == 2:
        co()
        print("\033[1m\x1B[4m" + 'REGISTER MEMBERSHIP' + "\x1B[0m")
        if id_awal < 200:
            print(f'No ID anda adalah: {id_awal}')
            data_nama[id_awal - 100] = str(input('Bagaimana kami memanggil anda: '))
            while not data_nama[id_awal - 100]:
                co()
                print("\033[1m\x1B[4m" + 'REGISTER MEMBERSHIP' + "\x1B[0m")
                print(f'No ID anda adalah: {id_awal}')
                print('Nama tidak boleh kosong.')
                data_nama[id_awal - 100] = str(input('Bagaimana kami memanggil anda: '))

            data_password[id_awal - 100] = str(input('Buat Password: '))
            while not data_password[id_awal - 100]:
                co()
                print("\033[1m\x1B[4m" + 'REGISTER MEMBERSHIP' + "\x1B[0m")
                print(f'No ID anda adalah: {id_awal}')
                print(f'Bagaimana kami memanggil anda: {data_nama[id_awal-100]}')
                print('Password tidak boleh kosong.')
                data_password[id_awal - 100] = str(input('Buat Password: '))

            temp = str(input("Konfirmasi Password: "))

            # KONFIRMASI PASSWORD
            while temp != data_password[id_awal-100]:
                co()
                print("\033[1m\x1B[4m" + 'REGISTER MEMBERSHIP' + "\x1B[0m")
                print(f'No ID anda adalah: {id_awal}')
                print(f'Bagaimana kami memanggil anda: {data_nama[id_awal-100]}')
                print('\033[3mPassword tidak cocok, coba lagi\033[0m')
                data_password[id_awal - 100] = str(input('Buat Password: '))
                temp = str(input("Konfirmasi Password: "))
            co()
            print(f'Selamat \033[1m{data_nama[id_awal - 100]}\033[0m, pembuatan ID berhasil\nNo ID anda: {id_awal}, mohon \033[1mJANGAN SAMPAI LUPA PASSWORD\033[0m\n\nAnda akan dikembalikan ke Main Menu\n')
            id_awal += 1
        else:
            print('Kuota membership sudah habis\nAnda akan dikembalikan ke Main Menu.\n')

    # KELUAR
    elif command_awal == 3:
        co()
        print('Terima kasih telah bertransaksi di aplikasi kami!')
        break
    else:
        co()
        print('Silakan pilih menu yang tersedia\n.')