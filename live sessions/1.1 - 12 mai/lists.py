# inlantuire de obiecte omogene/neomogene cuprinse intre paranteze drepte [1, 2, 'asd']
# sunt mutabile (modificabile)

#liste omogene: 
nr_list = [1, 2, 3, 4]
str_list = ['a', 'ana are mere', "bananamango"]

#liste neomogene:
ne_list = ['Portocala', 1, [1, 2, 3]]

l = [1, 2, 3]

# list methods:
# l.append() --> adauga la finalul listei un element: 

print(l)

print(l.append('Ana are mere'))
print(l)

# l.extend() --> adauga la finalul listei mai multe elemente:
l2 = [10, 11, 12]
print(l.extend(l2))
print(l)

# l.insert() --> adauga un element la o anumita pozitie
l.insert(1, 'sunt nou aici')
print(l)

# l.remove() --> elimina prima aparitie a unui element (o sigura elminare)
l.append(1)
print(l)
l.remove(1)
print(l)
print(l.remove(1))
print(l)

# l.pop() --> elimina un element din list (ultimul by default sau de la pozitia pe care o dam); si returneaza valoarea care a fost scoasa din lista
print(l.pop())
print(l)
l.pop(0)
print(l)

# l.index() --> returneaza indexul unde se afla un element(primul index)
print(l.index(10))

# l.count() --> returneaza numarul de aparitii al unui element: 
l.append(2)
l.append(2)
l.append(3)
l.extend([2, 2, 3])
print(l)
print(l.count(2))

# l.sort() --> sorteaza lista (nu returneaza nimic)
l.remove('Ana are mere')
print(l.sort())
print(l)

# l.copy() --> returneaza o copie a listei
l2 = l
l3 = l.copy()

print(l)
l.pop()
l.pop()
l.pop()
print('print l: ', l)
print('print l2:', l2)
print('print l3:', l3)

# l.reverse() --> inverseaza lista
l.reverse()
print(l)

# List operators: 
# + * in not in [] [::]

# operatorul +  --> returneaza concatenearea a 2 liste 
print(l + [10, 11, 12])
print(l)

# operatorul * --> returneaza o lista repetata de x ori:
print(l * 3)

# operatorii in/not in: --> returneaza True/False daca elem este sau nu in lista:
print(2 in l)
print(10 not in l)

# operatorul index [] --> exact ca la stringuri:
l.insert(3, 'BananaMango')
print(l)
print(l[3])

# slicing [start:end:step]
print(l[1::2])
print(l[::-1])
print(l[::-1])
print(l[::-1])

