# Class induk
class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def bersuara(self):
        pass
    def jumlah_kaki(self):
        print("Berkaki empat")
    def jenis_makanan(self):
        pass

# Class anak 1
class Anjing(Hewan):
    def bersuara(self):
        print ("Woof!")
    def jenis_makanan(self):
        print("Makan daging")

# Class anak 2
class Kucing(Hewan):
    def bersuara(self):
        print ("Meong!")
    def jenis_makanan(self):
        print("Makan daging")
    
# Class anak 3
class Sapi(Hewan):
    def bersuara(self):
        print ("Mooo!")
    def jenis_makanan(self):
        print("Makan rumput")

husky = Anjing("Max", "Husky")
oren = Kucing("Moko", "Oren")
putih = Sapi("Mili", "Putih")

husky.bersuara()
husky.jenis_makanan()
husky.jumlah_kaki()

oren.bersuara()
oren.jenis_makanan()
oren.jumlah_kaki()

putih.bersuara()
putih.jenis_makanan()
putih.jumlah_kaki()