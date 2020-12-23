"""
Afifah Kho'eriah

Bangun Ruang Kubus dan balok
Volume Kubus = s**3
Volume Balok = panjang*lebar*tinggi

"""

class kubus:
    def __init__(self):
        self.sisi = float(input("Masukkan sisi Kubus: "))        
    
    def volume_kubus(self):
        self.luas_kubus = self.sisi**3
        return self.luas_kubus

class balok:
    def __init__(self):
        self.panjang = float(input("Masukkan panjang balok: "))  
        self.lebar = float(input("Masukkan lebar balok: "))  
        self.tinggi = float(input("Masukkan tinggi balok: "))  

    def Volume_balok(self):
        self.luas_balok = self.panjang*self.lebar*self.tinggi
        return self.luas_balok