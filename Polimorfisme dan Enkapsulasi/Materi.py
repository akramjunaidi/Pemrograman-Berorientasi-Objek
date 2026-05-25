#Materi

class MahasiswaTI:
    def __init__(self, nama, nim, nilai):
        super().__init__(nama, nim)
        self.__nilai = nilai

    def getNilai(self):
        return self.__nilai
    
    def setNilai(self, nilai):
        self.__nilai = nilai

mhs = MahasiswaTI("Rizky", "123456", 90)

print("Nama:", mhs.getNama())
print("NIM:", mhs.getNim())om 

class Mahasiswa:
    def __init__(self, nama, nim):
        self.__nama = nama
        self.__nim = nim

    def getNama(self):
        return self.__nama
    
    def getNim(self):
        return self.__nim
    
    def getNama(self, nama):
        self.__nama = nama

    def setNIM(self, nim):
        self.__nim = nim 


class MahasiswaTI(mahasiswa):
    def __init__(self, nama, nim, nilai):
        super().__init__(nama, nim)
        self.__nilai = nilai

    def getNilai(self):
        return self.__nilai
    
    def setNilai(self, nilai):
        self.__nilai = nilai

mhs = MahasiswaTI("Rizky", "123456", 90)

print("Nama:", mhs.getNama())
print("NIM:", mhs.getNim())