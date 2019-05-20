#FIDA AMY
#L200170075

class stack():
    def __init__(self):
        self.list = []
    def empty(self):
        return len(self.list) == 0
    def __len__(self):
        return len(self.list)
    def push(self, data):
        self.list.append(data)
    def pop(self):
        assert not self.empty(), 'No file'
        return self.list.pop()

def cetak_hexa(angka):
    x = stack()
    if angka == 0:
        x.push(0)
    while angka != 0:
        sisa = angka % 16
        angka = angka // 16
        x.push(sisa)
    hexa = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    hasil = ''
    for i in range(len(x)):
        hasil += str(hexa[x.pop()])
    return hasil
    
