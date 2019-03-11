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

#Soal 2
    # A . Metode mengambil kota tempat tinggal
class mahasiswa(object):
    "berisi biodata mahasiswa"
    def __init__(self, nama, KotaTinggal, UangSaku):
        self.nama = nama
        self.KotaTinggal = KotaTinggal
        self.UangSaku = UangSaku
    def ambilKotaTinggal(self):
        print(self.KotaTinggal)
    def perbaruiKotaTinggal(self, stringBaru):#B . Metode untuk memperbarui kota tinggal
        self.KotaTinggal = stringBaru
    def ambilUangSaku(self):
        print (self.UangSaku)
    def tambahUangSaku(self, intBaru): #C. metod menambah uang saku
        x = self.UangSaku + intBaru
        return x
        
m9= mahasiswa ('fida' , 'pati', 50000)
m9.ambilKotaTinggal

#Soal 3




