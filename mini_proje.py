'''
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:
input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output: [1,'a','cat',2,3,'dog',4,5]
'''

boslist = []
    
def flat(l):
    for i in l:
        if type(i)==list:
            flat(i)
        else:
            boslist.append(i)

flat([[1,'a',['cat'],2],[[[3]],'dog'],4,5])
print(boslist)

'''
2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:
input: [[1, 2], [3, 4], [5, 6, 7]]
output: [[[7, 6, 5], [4, 3], [2, 1]]
'''

# reverse 

x = [[1, 2], [3, 4], [5, 6, 7]]
bos = []

def ters(l):
    for i in l:
        if type(i)==list:
            bos.append(list(reversed(i)))
            
            
        

ters([[1, 2], [3, 4], [5, 6, 7]])
print(list(reversed(bos)))