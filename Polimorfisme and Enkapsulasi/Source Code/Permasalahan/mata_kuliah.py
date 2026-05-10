#mata_kuliah

class MataKuliah:
    def __init__(self, nama_mk, jumlah_sks, kelas_paralel, nama_dosen, nip_dosen, jam, ruangan):
        self.__nama_mk = nama_mk
        self.__jumlah_sks = jumlah_sks
        self.__kelas_paralel = kelas_paralel
        self.__nama_dosen = nama_dosen
        self.__nip_dosen = nip_dosen
        self.__jam = jam
        self.__ruangan = ruangan

    def getNamaMk(self): return self.__nama_mk
    def setNamaMk(self, nama_mk): self.__nama_mk = nama_mk

    def getJumlahSKS(self): return self.__jumlah_sks
    def setJumlahSKS(self, jumlah_sks): self.__jumlah_sks = jumlah_sks

    def getKelasParalel(self): return self.__kelas_paralel
    def setKelasParalel(self, kelas_paralel): self.__kelas_paralel = kelas_paralel

    def getNamaDosen(self): return self.__nama_dosen
    def setNamaDosen(self, nama_dosen): self.__nama_dosen = nama_dosen

    def getNIPDosen(self): return self.__nip_dosen
    def setNIPDosen(self, nip_dosen): self.__nip_dosen = nip_dosen

    def getJam(self): return self.__jam
    def setJam(self, jam): self.__jam = jam

    def getRuangan(self): return self.__ruangan
    def setRuangan(self, ruangan): self.__ruangan = ruangan