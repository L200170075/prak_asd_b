#NO 3

from time import time as timeD
from random import shuffle
import time

def swap (A, p,q):
    tmp = A[p]
    A[p] = A[p]
    A[q] = tmp
    
def cariPosisiTerkecil (A, dari, sampai):
    posisiTerkecil = dari
    for i in range(dari+1, sampai):
        if A[i] < A[posisiTerkecil]:
            posisiTerkecil = i
    return posisiTerkecil

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range (n-i-1):
            if A[j] > A[j+1]:
                swap (A,j,j+1)

def selectionSort(A):
    n = len (A)
    for i in range(n-1):
        indexKecil = cariPosisiTerkecil(A,i,n)
        if indexKecil != i :
            swap(A,i,indexKecil)

def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos-1]:
            A[pos] = A[pos-1]
            pos -=1
        A[pos] = nilai
def mergeSort(A):
    if len(A) > 1:
        mid = len(A)//2
        separuhKiri = A[:mid]
        separuhKanan = A[mid:]

        mergeSort(separuhKiri)
        mergeSort(separuhKanan)

        i = 0
        j = 0
        k = 0
        while i < len (separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i]<separuhKanan[j]:
                A[k] = separuhKiri[i]
                i = i + 1
            else :
                A[k] = separuhKanan[j]
                j = j+1
                k = k+1
        while i< len (separuhKiri):
            A[k] = separuhKiri[i]
            i = i+1
            k = k+1
        while j < len(separuhKanan):
            A[k] = separuhKanan[j]
            j = j+1
            k = k+1
        return A
def quickSort(A):
    quickSortBantu(A, 0, len(A) - 1)

def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)
        quickSortBantu(A, awal, titikBelah - 1)
        quickSortBantu(A, titikBelah + 1, akhir)

def partisi(A, awal, akhir):
    nilaiPivot = A[awal]

    penandaKiri = awal + 1
    penandaKanan = akhir

    selesai = False
    while not selesai:

        while penandaKiri <= penandaKanan and \
              A[penandaKiri] <= nilaiPivot:
            penandaKiri = penandaKiri + 1

        while A[penandaKanan] >= nilaiPivot and \
              penandaKanan >= penandaKiri:
            penandaKanan = penandaKanan - 1

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
    

k = range(6000)
shuffle(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]
u_mrg = k[:]
u_qck = k[:]

aw = detak();bubbleSort(u_bub);ak = detak();print('bubble : %g detik' %(ak-aw));
aw = detak();selectionSort(u_sel);ak = detak();print('selection : %g detik' %(ak-aw));
aw = detak();insertionSort(u_ins);ak = detak();print('insertion : %g detik' %(ak-aw));
aw = detak();mergeSort(u_mrg);ak = detak();print('merge : %g detik' %(ak-aw));
aw = detak();quickSort(u_qck);ak = detak();print('quick : %g detik' %(ak-aw));



            