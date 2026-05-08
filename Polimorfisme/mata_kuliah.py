class MataKuliah:
    def __init__(self, Nama_mk, Jumlah_sks, Kelas_paralel, Nama_dosen, Nip_dosen, Jam, Ruangan):
        self.__nama_mk = Nama_mk
        self.__jumlah_sks = Jumlah_sks
        self.__kelas_paralel = Kelas_paralel
        self.__nama_dosen = Nama_dosen
        self.__nip_dosen = Nip_dosen
        self.__jam = Jam
        self.__ruangan = Ruangan

    def getNamaMk(self): return self.__nama_mk
    def setNamaMk(self, Nama_mk): self.__nama_mk = Nama_mk

    def getJumlahSks(self): return self.__jumlah_sks
    def setJumlahSks(self, Jumlah_sks): self.__jumlah_sks = Jumlah_sks

    def getKelasParalel(self): return self.__kelas_paralel
    def setKelasParalel(self, Kelas_paralel): self.__kelas_paralel = Kelas_paralel

    def getNamaDosen(self): return self.__nama_dosen
    def setNamaDosen(self, Nama_dosen): self.__nama_dosen = Nama_dosen

    def getNipDosen(self): return self.__nip_dosen
    def setNipDosen(self, Nip_dosen): self.__nip_dosen = Nip_dosen

    def getJam(self): return self.__jam
    def setJam(self, Jam): self.__jam = Jam

    def getRuangan(self): return self.__ruangan
    def setRuangan(self, Ruangan): self.__ruangan = Ruangan