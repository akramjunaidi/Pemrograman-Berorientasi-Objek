#Permasalahan Modul 1

class JadwalKuliah:
    def __init__(self, nama_mk, kelas, dosen, hari):
        self.nama_mk = nama_mk
        self.kelas = kelas
        self.dosen = dosen
        self.hari = hari

    def tampilkanInformasi(self):
        print(f"Hari Kuliah   : {self.hari}")
        print(f"Mata Kuliah   : {self.nama_mk}")
        print(f"Kelas         : {self.kelas}")
        print(f"Dosen         : {self.dosen}")

daftar_nama_mk = []
daftar_sks_mk = []
daftar_kelas = []
daftar_nama_dosen = []
daftar_nip_dosen = []
daftar_jadwal = []

while True:
    print("Sistem Manajemen Jadwal Kuliah")
    print("1. Input Data Mata Kuliah (Nama & SKS)")
    print("2. Input Kelas (A/B)")
    print("3. Input Data Dosen (Nama & NIP)")
    print("4. Input Jadwal Baru")
    print("5. Tampilkan Seluruh Jadwal")
    print("6. Keluar Program")
    
    pilihan_menu = input("Pilih menu (1-6): ")
    if pilihan_menu == "1":
        print("Tambah Data Mata Kuliah")
        nama_mk = input("a. Masukkan Nama Mata Kuliah : ")
        sks_mk = input("b. Masukkan Jumlah SKS       : ")
        daftar_nama_mk.append(nama_mk)
        daftar_sks_mk.append(sks_mk)
        print(f"BERHASIL: Mata Kuliah '{nama_mk}' ({sks_mk} SKS) disimpan ke sistem!")

    elif pilihan_menu == "2":
        print("Tambah Data Kelas")
        kelas = input("a. Masukkan Nama Kelas (A/B) : ")
        daftar_kelas.append(kelas)
        print(f"BERHASIL: Kelas '{kelas}' disimpan ke sistem!")

    elif pilihan_menu == "3":
        print("Tambah Data Dosen")
        nama_dosen = input("a. Masukkan Nama Dosen : ")
        nip_dosen = input("b. Masukkan NIP Dosen  : ")
        daftar_nama_dosen.append(nama_dosen)
        daftar_nip_dosen.append(nip_dosen)
        print(f"BERHASIL: Dosen '{nama_dosen}' disimpan ke sistem!")

    elif pilihan_menu == "4":
        print("Pembuatan Jadwal Kuliah")
        print("Ketikkan data untuk membuat jadwal:")
        input_mk    = input("a. Nama Mata Kuliah : ")
        input_kelas = input("b. Kelas            : ")
        input_dosen = input("c. Nama Dosen       : ")
        input_hari  = input("d. Hari Kuliah      : ")
        jadwal_baru = JadwalKuliah(input_mk, input_kelas, input_dosen, input_hari)
        daftar_jadwal.append(jadwal_baru)
        print("BERHASIL: Jadwal berhasil dirakit dan ditambahkan!")

    elif pilihan_menu == "5":
        print("DAFTAR JADWAL TERSIMPAN")
        if daftar_jadwal == []: 
            print("Belum ada jadwal yang diinputkan.")
        else:
            nomor_urut = 1
            for jadwal in daftar_jadwal:
                print(f"[ Jadwal ke-{nomor_urut} ]")
                jadwal.tampilkanInformasi()
                nomor_urut = nomor_urut + 1

    elif pilihan_menu == "6":
        print("Terima kasih telah menggunakan sistem ini. Sampai jumpa!")
        break  

    else:
        print("ERROR: Pilihan menu tidak valid. Silakan pilih angka 1 hingga 6.")
