#FIDA AMY
#L200170075

class stack():
    def __init__(self):#membuat stack kosong
        self.item = []
    def empty(self):#mengembalikan nilai boolean yg menunjukkan apakah stack itu kosong
        return len(self) == 0
    def __len__(self): #mengembalikan byknya item di stack
        return len(self.item)
    def peek(self): #mengembalikan nilai posisi atas tnpa menghapus data dan
                    #mengembalikan nilai dr item yg paling atas tnp mnghpus
        assert not self.empty()
        return self.item[-1]
    def pop(self): #mengembalikan nilai posisi atas lalu menghapus, stack kosong tdk dpt kosong
        assert not self.empty()
        return self.item.pop()
    def push(self, data): #mendorong item ke stact. menambah item ke puncak stack
        self.item.append(data)


nilai = stack()
for i in range(16):
    if i % 3 == 0:
        nilai.push(i)


print(nilai.item)
