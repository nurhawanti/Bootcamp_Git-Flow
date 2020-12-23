"""
Afifah Kho'eriah

Bangun Ruang Kubus dan balok
Luas Kubus = 6*sisi**2
Luas Balok = 2*(panjang*lebar + panjang*tinggi + lebar*tinggi)

"""

class kubus:
    def __init__(self):
        self.sisi = float(input("Masukkan sisi Kubus: "))        
    
    def luas_kubus(self):
        self.luas_kubus = 6*(self.sisi**2)
        return self.luas_kubus

class balok:
    def __init__(self):
        self.panjang = float(input("Masukkan panjang balok: "))  
        self.lebar = float(input("Masukkan lebar balok: "))  
        self.tinggi = float(input("Masukkan tinggi balok: "))  

    def luas_balok(self):
        self.luas_balok = 2*(self.panjang*self.lebar + self.panjang*self.tinggi + self.lebar*self.tinggi)
        return self.luas_balok