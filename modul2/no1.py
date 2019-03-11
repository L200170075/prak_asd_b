#Soal 1

class Pesan(object):        #A
    """Sebuah kelas bernama pesan .
        untuk memeriksa suatu str terkandung di dlmnya atau tidak"""
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print ("Kalimatku mempunyai " , len(self.teks), 'karakter.')
    def perbarui(self, stringBaru):
        self.teks = stringBaru
    def apakahTerkandung(self, a):
        if a in self.teks:
            return True
        else:
            return False
    def hitungKonsonan(self): #B
        a = 0
        x = 'aiueoAIUEO'
        for i in self.teks:
            if i  not in x :
                a += 1
        return a
    def hitungVokal(self): #C
        a = 0
        x = 'aiueoAIUEO'
        for i in self.teks:
            if i in x:
                a += 1
        return a
