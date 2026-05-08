class MataKuliah:
    def __init__(self, nama_mk, jumlah_sks, kelas_paralel, nama_dosen, nip_dosen, jam, ruangan):
        self.nama_mk = nama_mk
        self.jumlah_sks = jumlah_sks
        self.kelas_paralel = kelas_paralel
        self.nama_dosen = nama_dosen
        self.nip_dosen = nip_dosen
        self.jam = jam
        self.ruangan = ruangan

class Teori(MataKuliah):
    def tampilkanInformasi(self):
        print("--- [ JENIS: KELAS TEORI ] ---")
        print(f"Mata Kuliah  : {self.nama_mk} ({self.jumlah_sks} SKS)")
        print(f"Jadwal       : {self.jam} | Ruang: {self.ruangan}")
        print(f"Kelas        : {self.kelas_paralel}")
        print(f"Dosen        : {self.nama_dosen} (NIP: {self.nip_dosen})")

class Praktikum(MataKuliah):
    def tampilkanInformasi(self):
        print("--- [ JENIS: KELAS PRAKTIKUM (LAB) ] ---")
        print(f"Mata Kuliah  : {self.nama_mk} ({self.jumlah_sks} SKS)")
        print(f"Jam       : {self.jam} | Ruang: {self.ruangan}")
        print(f"Kelas        : {self.kelas_paralel}")
        print(f"Dosen        : {self.nama_dosen} (NIP: {self.nip_dosen})")
        print("Keterangan   : Wajib memakai jas laboratorium")

daftar_jadwal = [] 

temp_sks = ""
temp_kelas = ""
temp_nama_dosen = ""
temp_nip_dosen = ""
temp_jenis = ""

while True:
    print("Sistem Manajemen Jadwal Kuliah")
    print("1. Input SKS Mata Kuliah")
    print("2. Input Kelas (A/B)")
    print("3. Input Data Dosen (Nama & NIP)")
    print("4. Input Jenis (Teori/Praktikum)")
    print("5. Input Jadwal (Nama MK, Jam, Ruangan)")
    print("6. Tampilkan Seluruh Jadwal")
    print("7. Keluar Program")
    
    pilihan_menu = input("Pilih menu (1-7): ")

    if pilihan_menu == "1":
        temp_sks = input("Masukkan Jumlah SKS: ")
        print("Status: SKS tersimpan sementara.")

    elif pilihan_menu == "2":
        temp_kelas = input("Masukkan Kelas Paralel (A/B): ")
        print("Status: Kelas tersimpan sementara.")

    elif pilihan_menu == "3":
        temp_nama_dosen = input("Masukkan Nama Dosen : ")
        temp_nip_dosen  = input("Masukkan NIP Dosen  : ")
        print("Status: Data Dosen tersimpan sementara.")

    elif pilihan_menu == "4":
        temp_jenis = input("Masukkan Jenis (Teori/Praktikum): ")
        print("Status: Jenis tersimpan sementara.")

    elif pilihan_menu == "5":
        print("[ Input Detail Jadwal & Simpan ]")
        nama_mk_baru = input("- Masukkan Nama Mata Kuliah : ")
        jam_baru     = input("- Masukkan Jam (Contoh 08:00): ")
        ruang_baru   = input("- Masukkan Nama Ruangan      : ")
        
        if temp_sks == "" or temp_kelas == "" or temp_nama_dosen == "" or temp_jenis == "":
            print("GAGAL: Mohon lengkapi Menu 1 sampai 4 terlebih dahulu!")
        else:
            if temp_jenis == "Praktikum" or temp_jenis == "praktikum":
                objek_jadwal = Praktikum(nama_mk_baru, temp_sks, temp_kelas, temp_nama_dosen, temp_nip_dosen, jam_baru, ruang_baru)
            else:
                objek_jadwal = Teori(nama_mk_baru, temp_sks, temp_kelas, temp_nama_dosen, temp_nip_dosen, jam_baru, ruang_baru)
            
            daftar_jadwal.append(objek_jadwal)
            print("BERHASIL: Jadwal Baru telah dirakit dan disimpan!")
            
            temp_sks = ""; temp_kelas = ""; temp_nama_dosen = ""; temp_nip_dosen = ""; temp_jenis = ""

    elif pilihan_menu == "6":
        print("DAFTAR JADWAL TERSIMPAN")
        if daftar_jadwal == []:
            print("Belum ada jadwal yang tersimpan.")
        else:
            for jdl in daftar_jadwal:
                print()
                jdl.tampilkanInformasi()

    elif pilihan_menu == "7":
        print("Keluar program...")
        break