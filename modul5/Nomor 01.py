class MhsTIF(object):
    def __init__(self, nama, umur, kota, NIM):
        self.nama = nama
        self.umur = umur
        self.kotaTinggal = kota
        self.nim = NIM

    def __str__(self):
        x = self.nim
        return x

    def getnim(self):
        return self.nim

c0 = MhsTIF('Tika', 19, 'magetan', 'L200170042')
c1 = MhsTIF('pipo', 19, 'skh', 'L200170080')
c2 = MhsTIF('Titis', 19, 'pwd', 'L200170052')
c3 = MhsTIF('Fida', 18, 'pati', 'L200170075')
c4 = MhsTIF('susi', 20, 'bojonegoro', 'L200170003')
c5 = MhsTIF('umi', 19, 'solo', 'L200170115')
c6 = MhsTIF('Elvy', 19, 'solo', 'L200170116')
c7 = MhsTIF('caca', 20, 'pwd', 'L200170067')
c8 = MhsTIF('celsi', 20, 'batang', 'L200170077')
c9 = MhsTIF('nesti', 25 ,'Sragen', 'L200170001')
c10 = MhsTIF('nustu', 29, 'Purwodadi', 'L200170002')

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai.nim < A[pos - 1].nim:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai

def cetakDaftar(d):
    for i in d:
        print (i)
        
insertionSort(Daftar)
cetakDaftar(Daftar)
