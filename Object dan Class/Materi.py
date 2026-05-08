#Object dan Class

class mahasiswa:
    def __init__(self, nama, nim, tanggal_lahir, alamat):
        self.nama = nama
        self.nim = nim
        self.tanggal_lahir = tanggal_lahir
        self.alamat = alamat

    def tampilkanNama(self):
        print("Nama Mahasiswa: ", self.nama)
    def tampilkanNim(self):
        print("Nim Mahasiswa: ", self.nim)
    def tampilkanTanggallahir(self):
        print("Tanggal lahir: ", self.tanggal_lahir)
    def tampilkanAlamat(self):
        print("Alamat: ", self.alamat)

akaii = mahasiswa("Akram Junaidi", "250306033", "04-04-2005", "Maluk")
akaii.tampilkanNama()
akaii.tampilkanNim()
akaii.tampilkanTanggallahir()
akaii.tampilkanAlamat()
