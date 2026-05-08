from mata_kuliah import MataKuliah

class Teori(MataKuliah):
    def __init__(self, Nama_mk, Jumlah_sks, Kelas_paralel, Nama_dosen, Nip_dosen, Jam, Ruangan):
        super().__init__(Nama_mk, Jumlah_sks, Kelas_paralel, Nama_dosen, Nip_dosen, Jam, Ruangan)

    def tampilkanInformasi(self):
        print("[JENIS: KELAS TEORI]")
        print(f"Mata Kuliah    : {self.getNamaMk()} ({self.getJumlahSks()} SKS)")
        print(f"Jadwal         : {self.getJam()} | Ruang: {self.getRuangan()}")
        print(f"Kelas          : {self.getKelasParalel()}")
        print(f"Dosen          : {self.getNamaDosen()} (NIP: {self.getNipDosen()})")

class Praktikum(MataKuliah):
    def __init__(self, Nama_mk, Jumlah_sks, Kelas_paralel, Nama_dosen, Nip_dosen, Jam, Ruangan):
        super().__init__(Nama_mk, Jumlah_sks, Kelas_paralel, Nama_dosen, Nip_dosen, Jam, Ruangan)

    def tampilkanInformasi(self):
        print("[JENIS: KELAS PRAKTIKUM (LAB)]")
        print(f"Mata Kuliah    : {self.getNamaMk()} ({self.getJumlahSks()} SKS)")
        print(f"Jam            : {self.getJam()} | Ruang: {self.getRuangan()}")
        print(f"Kelas          : {self.getKelasParalel()}")
        print(f"Dosen          : {self.getNamaDosen()} (NIP: {self.getNipDosen()})")
        print("Keterangan     : Wajib membawa modul praktikum")

def main():
    daftar_jadwal = []
    
    while True:
        print("PROGRAM MANAJEMEN JADWAL")
        print("1. Tambah Data Jadwal")
        print("2. Tampilkan Semua Jadwal")
        print("3. Keluar")
        
        pilihan_utama = input("Pilih Menu (1/2/3): ")

        if pilihan_utama == "1":
            print("Input Detail Mata Kuliah")
            nama_mk   = input("Nama Mata Kuliah  : ")
            sks       = input("Jumlah SKS        : ")
            kelas     = input("Kelas (A/B/C)     : ")
            dosen     = input("Nama Dosen        : ")
            nip       = input("NIP Dosen         : ")
            jam       = input("Jam (08:00)       : ")
            ruang     = input("Ruangan           : ")
            
            print("Pilih Jenis Perkuliahan")
            print("1. Kelas Teori")
            print("2. Kelas Praktikum")
            pilihan_jenis = input("Pilih Jenis (1/2): ")

            if pilihan_jenis == "1":
                objek = Teori(nama_mk, sks, kelas, dosen, nip, jam, ruang)
                daftar_jadwal.append(objek)
                print("Status: Data Teori berhasil disimpan!")
            elif pilihan_jenis == "2":
                objek = Praktikum(nama_mk, sks, kelas, dosen, nip, jam, ruang)
                daftar_jadwal.append(objek)
                print("Status: Data Praktikum berhasil disimpan!")
            else:
                print("Gagal: Pilihan jenis tidak tersedia.")

        elif pilihan_utama == "2":
            if daftar_jadwal == []:
                print("Belum ada data yang tersimpan.")
            else:
                print("      DAFTAR JADWAL KULIAH")
                for jadwal in daftar_jadwal:
                    jadwal.tampilkanInformasi()

        elif pilihan_utama == "3":
            print("Terima kasih, program selesai.")
            break
        
        else:
            print("Pilihan menu tidak valid!")

if __name__ == "__main__":
    main()