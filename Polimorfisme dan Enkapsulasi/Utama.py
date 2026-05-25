#Class Utama

class MataKuliah:
    def __init__(self, nama_mk, jumlah_sks, kelas_paralel, nama_dosen, nip_dosen, jam, ruangan):
        self._nama_mk       = nama_mk      
        self._kelas_paralel = kelas_paralel  

        self.__jumlah_sks   = jumlah_sks  
        self.__jam          = jam        
        self.__ruangan      = ruangan       
        self.__nama_dosen   = nama_dosen  
        self.__nip_dosen    = nip_dosen   

    def _get_nama_mk(self): return self._nama_mk
    def _set_nama_mk(self, nama_mk):
        if nama_mk == "": 
            print("Gagal: Nama mata kuliah tidak boleh kosong.")
        else:
            self._nama_mk = nama_mk
            print(f"Nama MK berhasil diubah menjadi: {self._nama_mk}")
    def _get_kelas_paralel(self): return self._kelas_paralel
    def _set_kelas_paralel(self, kelas_paralel):
        if kelas_paralel == "": 
            print("Gagal: Kelas paralel tidak boleh kosong.")
        else:
            self._kelas_paralel = kelas_paralel
            print(f"Kelas berhasil diubah menjadi: {self._kelas_paralel}")

    def _get_ruangan(self): return self.__ruangan
    def _set_ruangan(self, ruangan):
        if ruangan == "": 
            print("Gagal: Ruangan tidak boleh kosong.")
        else:
            self.__ruangan = ruangan
            print(f"Ruangan berhasil diubah menjadi: {self.__ruangan}")
    def _get_jumlah_sks(self): return self.__jumlah_sks
    def _set_jumlah_sks(self, jumlah_sks):
        if jumlah_sks == "": 
            print("Gagal: Jumlah SKS tidak boleh kosong.")
        else:
            self.__jumlah_sks = jumlah_sks
            print(f"Jumlah SKS berhasil diubah menjadi: {self.__jumlah_sks}")
    def _get_jam(self): return self.__jam
    def _set_jam(self, jam):
        if jam == "": 
            print("Gagal: Jam kuliah tidak boleh kosong.")
        else:
            self.__jam = jam
            print(f"Jam kuliah berhasil diubah menjadi: {self.__jam}")
    def _get_nama_dosen(self): return self.__nama_dosen
    def _set_nama_dosen(self, nama_dosen):
        if nama_dosen == "": 
            print("Gagal: Nama dosen tidak boleh kosong.")
        else:
            self.__nama_dosen = nama_dosen
            print(f"Nama dosen berhasil diubah menjadi: {self.__nama_dosen}")
    def _get_nip_dosen(self): return self.__nip_dosen
    def _set_nip_dosen(self, nip_dosen):
        if nip_dosen == "": 
            print("Gagal: NIP dosen tidak boleh kosong.")
        else:
            self.__nip_dosen = nip_dosen
            print(f"NIP dosen berhasil diubah menjadi: {self.__nip_dosen}")

    def _get_info_dosen(self):
        return f"{self.__nama_dosen} (NIP: {self.__nip_dosen})"