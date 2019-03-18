

#NOTE : sy upload smalem tp salah akun mas. di akun tmen yg nimnya
#L200170072 soalnya temen juga pernah login di lptop saya. dan baru sadar pagi ini. :)

#fida Amy N A
#L200170075
#B

m1 = [
    [5, 0],
    [2, 6],
]

m2 = [
    [1, 0],
    [4, 2],
]
##NO 1
    #A
def cekMat(matrix):
    """memastikan type data Integer"""
    jum = len(matrix)
    hasil = ""
    for x in matrix:
        for i in x:
            assert isinstance(i, int),"Harus Integer"
        return True
#B
def Ukuran(matrix):
    """Mengambil ukuran matriks"""
    return("Ukuran Matrix = "+str(len(matrix))+" x "+str(len(matrix[0])))

#c menjumlahkan matriks

def Jumlah(matrix1,matrix2):
    """Penjumlahan 2 Matrix"""
    if Ukuran(matrix1) == Ukuran(matrix2):
        for x in range(0, len(matrix1)):
            for y in range(0, len(matrix1[0])):
                print(matrix1[x][y] + matrix2[x][y], end=' '),
            print()
    else:
        print("Matriks Tidak Sesuai")
        
#D mengalikan matriks
def Kali(matrix1,matrix2):
    """Perkalian 2 Matrix"""
    mat3 = []
    if Ukuran(matrix1) == Ukuran(matrix2):
        for x in range(0, len(matrix1)):
            row = []
            for y in range(0, len(matrix1[0])):
                total = 0
                for z in range(0, len(matrix1)):
                    total = total + (matrix1[x][z] * matrix2[z][y])
                row.append(total)
            mat3.append(row)

        for x in range(0, len(mat3)):
            for y in range(0, len(mat3[0])):
                print(mat3[x][y], end=' ')
            print()
    else:
        print("Matriks Tidak Sesuai")
def determinan(matrix):
    """Menghitung Determinan Matrix"""
    if len(matrix) == len(matrix[0]):
        bil = [x for x in range(len(matrix))]
        jum = 0
        for i in range(len(matrix)):
            total = 1
            for x in range(len(matrix)):
                total *= matrix[x][bil[x]]
            bil += [bil.pop(0)]
            jum += total
        bil2 = [x for x in range(len(matrix))]
        bil.reverse()
        jum2 = 0
        for i in range(len(matrix)):
            total2 = 1
            for x in range(len(matrix)):
                total2 *= matrix[x][bil2[x]]
            bil2 += [bil2.pop()]
            jum2 += total2
        print(total-total2)
        return ""
    else:
        print("Matriks Harus Bujursangkar")

#CEK NOMER 1
print(cekMat(m1))
print(Ukuran(m1))
Jumlah(m1,m2)
Kali(m1,m2)
print(determinan(m1))

# 2 (A)
def buatNol(m, n):
    """Menggunakan dua input"""
    matrix = [[0 for x in range(m)] for i in range(n)]
    print(matrix)

def buatNol2(m):
    """Menggunakan satu input"""
    n = m
    matrix = [[0 for x in range(m)] for i in range(n)]
    print(matrix)

#2(B)
def buatIdentitas(m):
    n = m
    matrix = [[1 if j == i else 0 for j in range(m)]for i in range(n)]
    print(matrix)

#CEK NOMER 2
buatNol(4,2)
buatNol2(1)
buatIdentitas(2)

#3
class Node(object):
    def __init__(self, data, nextNode=None):
        self.data = data
        self.next = next
        
    def MakeNode(list):
        a = Node(list[0])
        if len(list) > l:
            b = a
            for i in range (l, len(list)):
                b.next = Node (list[i])
                b = b.next
        return a 

    def kunjungi (head):
        curNode = head
        while curNode != None :
            print (curNnode.data)
            curNode = curNode.next
            
    def cari(head, yang_dicari):
        temp = head
        while temp != None :
            if temp.data == yang_dicari:
                return temp
            temp = temp.next
        return Node(None)
    
    def tambahDepan(head):
        temp = Node['tambah depan', head]
        return temp
    
    def tambahAkhir(head):
        temp = head
        while temp.next != None :
            temp = temp.next
        temp.next = Node ("tambah akhir")
        return head
    
    def tambah(head, posisi):
        "menambahkan simpul sebelum posisi"
        temp = head
        while temp !=  None :
            if temp.next.data == posisi:
                temp.belakang = temp.next
                temp.next = Node ("tambah tengah", temp_belakang)
                return head
            temp = temp.next
        return None
        
    def hapus(head, posisi):
        temp = head
        while temp != None :
            if temp.next.data == posisi:
                temp_belakang = temp.next.next
                temp.next = temp_belakang
                return head
            temp = temp.next
        return None

#4
class doubly_linked():
    def __init__(self, Data, Next=None, Prev=None):
        self.Data = Data
        self.Next = Next
        self.Prev = Prev

    def mencetak():
        curr = head
        while curr != None:
            print(curr.Data)
            if curr.Next == None:
                curr = curr
                break
            else:
                curr = curr.Next
        print("\n")
        while curr != None:
            print(curr.Data)
            curr = curr.Prev
    def simpulAwal(head):
        newNode = doubly_linked(25)
        newNode.Next = head
        head.Prev = newNode
        head =newNode
        return head

    def simpulAkhir(head):
        curr = head
        while curr != None:
            if curr.Next == None:
                newNode = doubly_linked(365)
                curr.Next = newNode
                newNode.Prev = curr
                return curr
            else:
                pass
            curr = curr.Next
        return curr
