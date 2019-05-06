#FIDA AMY NURDIANA AFIKOH
#L200170075
#B

class mhsTIF(object):
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.nim = nim
        self.kt = kota
        self.us = us
    def __str__(self):
        s = self.nama + ' NIM ' + str(self.nim)+ ' tinggal di ' + self.kt + \
            ' uang saku sebesar ' + str(self.us) + ' /bulan.'
        return s
    def getnim(self) :
        return self.nim

m1 = mhsTIF('fida', 75, 'pati', 200000)
m2 = mhsTIF('pipo', 72, 'sukoharjo', 300000)
m3 = mhsTIF('titis', 54, 'purwodadi', 150000)
m4 = mhsTIF('tika', 43, 'magetan', 250000)
m5 = mhsTIF('caca', 53, 'purwodadi', 200000)

Daftar = [m1,m2,m3,m4,m5]

def mergesort(A):
    if len(A)> 1 :
        mid = len(A)//2
        separuhKiri = A[:mid]
        separuhKanan = A[mid:]

        mergesort(separuhKiri)
        mergesort(separuhKanan)

        #Proses Penggabungan
        i = 0; j = 0; k = 0
        while i < len(separuhKiri) and j < len (separuhKanan):
            if separuhKiri[i].nim < separuhKanan[j].nim:
                A[k].nim = separuhKiri[i].nim
                i = i+1
            else :
                A[k].nim = separuhKanan[j].nim
                j = j+1
            k = k+1
        while i < len(separuhKiri):
            A[k].nim = separuhKiri[i].nim
            i = i+1
            k = k+1
        while k < len(separuhKanan):
            A[k].nim = separuhKanan[j].nim
            j = j+1
            k = k+1
        return A
mergesort(Daftar)
for i in Daftar :
    print(i)

def quickSort(A):
    quickSortBantu(A, 0, len(A)-1)
    return A
def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)
        quickSortBantu(A, awal, titikBelah - 1)
        quickSortBantu(A, titikBelah+1, akhir)

def partisi(A, awal, akhir):
    nilaiPivot = A[awal].getnim()

    penandaKiri = awal+1
    penandaKanan = akhir

    selesai = False
    while not selesai:

        while penandaKiri<= penandaKanan and \
              A[penandaKiri].getnim()<= nilaiPivot:
            penandaKiri +=1

        while A[penandaKanan].getnim()>= nilaiPivot and \
              penandaKanan >= penandaKiri:
            penandaKanan -=1

        if penandaKanan < penandaKiri:
            selesai = True
        else:
            temp = A[penandaKiri]
            A[penandaKiri] = A[penandaKanan]
            A[penandaKanan] = temp

    temp = A[awal]
    A[awal] = A[penandaKanan]
    A[penandaKanan] = temp

    return penandaKanan

quickSort(Daftar)
for i in Daftar :
    print (i)
print 





    
