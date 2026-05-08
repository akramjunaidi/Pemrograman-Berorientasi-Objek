class Penjumlahan:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def hitung(self):
        return self.a + self.b
    
class Pengurangan:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def hitung(self):
        return self.a - self.b
    
class Perkalian:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def hitung(self):
        return self.a * self.b
    
class Pembagian:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def hitung(self):
        return self.a / self.b
    
operasi = Perkalian(5, 3)
hasil = operasi.hitung()
print("Hasil perkalian: ", hasil)
