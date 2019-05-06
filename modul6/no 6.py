#6
class mhsTIF(object):
    def __init__(self, nama, no, kota, us):
        self.nama = nama
        self.no = no
        self.kota = kota
        self.uangSaku = us

c0 = mhsTIF('fida', 75, 'pati', 200000)
c1 = mhsTIF('pipo', 72, 'sukoharjo', 300000)
c2 = mhsTIF('titis', 54, 'purwodadi', 150000)
c3 = mhsTIF('tika', 43, 'magetan', 250000)
c4 = mhsTIF('caca', 53, 'purwodadi', 200000)

daftar = [c0.no, c1.no, c2.no, c3.no, c4.no]

def quickSort(L, ascending = True): 
    quicksorthelp(L, 0, len(L), ascending)
    
def quicksorthelp(L, low, high, ascending = True): 
    result = 0
    if low < high: 
        pivot_location, result = Partition(L, low, high, ascending)  
        result += quicksorthelp(L, low, pivot_location, ascending)  
        result += quicksorthelp(L, pivot_location + 1, high, ascending)
    return result


def Partition(L, low, high, ascending = True):
    result = 0 
    pivot, pidx = median_of_three(L, low, high)
    L[low], L[pidx] = L[pidx], L[low]
    i = low + 1
    for j in range(low + 1, high, 1):
        result += 1
        if (ascending and L[j] < pivot) or (not ascending and L[j] > pivot):
            L[i], L[j] = L[j], L[i]  
            i += 1
    L[low], L[i - 1] = L[i - 1], L[low] 
    return i - 1, result

def median_of_three(L, low, high):
    mid = (low + high - 1) // 2
    a = L[low]
    b = L[mid]
    c = L[high - 1]
    if a <= b <= c:
        return b, mid
    if c <= b <= a:
        return b, mid
    if a <= c <= b:
        return c, high - 1
    if b <= c <= a:
        return c, high - 1
    return a, low

print(daftar)
quickSort(daftar)
print(daftar)
