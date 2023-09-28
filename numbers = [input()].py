numbers = [1, 2, 3, 4]
summa = sum(numbers)
print(summa)

spisok = [1, 4, 8, 123, 31, 11]
naib =  max(spisok)
print(naib)

spisok2 = [4, 5, 234, 1346, 23, 5, 9, 4]
listik = list(set(spisok2))
print(listik)

spisok3 = [123, 1313]
spisok4 = ['Самара', 'пепперрони']
obyedinenie = spisok3 + spisok4
print(obyedinenie)

a1 = input()
spisok5 = []
for bb in a1.split(" "):
    spisok5.append(bb)
print(spisok5)
elem = input('Введите элемент для поиска')
if elem in spisok5:
    a = spisok5.index(elem)
    print(a)
else: 
    print('Нет такого элемента')

krt1 = (1, 2, 3)
krt2 = (76, 2, 5)
novkrt = krt1 + krt2
print(novkrt) 

a7 = input()
spisok6 = []
for bbb in a7.split(" "):
    spisok6.append(bbb)
print(spisok6)
elemen = input('Введите какой элемент удалить')
if elemen in spisok6:
    q = list(spisok6)
    q.remove(elemen)
    mmm = q
    print(mmm)
    x = tuple(mmm)
    print(x)
else: 
    print('Нет такого элемента')

kortage = input()
spisok7 = []
for rim in kortage.split(" "):
    spisok7.append(rim)
print(spisok7)
ind = input('Введите элемент ')
if ind in spisok7:
    rar = list(spisok7)
    tyt = rar.count(ind)
    print(tyt)
else:
    print('Нет такого элемента')