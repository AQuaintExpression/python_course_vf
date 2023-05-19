# listele sunt o colectie de obiecte incapsulate de [], sunt mutabile, ordonate si pot fi omogene/neomogene

# liste omogene
numbers = [1, 2, 3]
print(numbers)
numbers[0] = 10
print(numbers)
strings = ['ana', 'are', 'mere']

# liste neomogene
ad_hoc_data = [1, 2, 'Ana are mere', [1, 2, 3]]


print(len(ad_hoc_data))

# list methods:
# append, extend, insert, remove, pop, index, count, sort, reverse, copy

# append -> adauga un element la finalul listei.
l = [1, 2, 3]
print(l)
print(l.append('mere'))
print(l)

# extend -> adauga toate elementele unui iterabil (liste, tuplu, set) la finalul listei.

print(l.extend(ad_hoc_data))
print(l)

# insert -> adauga un element la o pozitie
l.insert(3, 'Bananamango')
print(l)

# remove -> scoate prima aparitie a unui element din lista. 
l.remove(1)
l.remove(1)
print(l)

# pop --> by default elimina din lista ultima valoare, si returneaza utilizatorului valoarea eliminata. Pop accepts an index.
print(l.pop())
print(l)

print(l.pop(2)) #eliminam cuvantul de la poz 2.
print(l)

# index --> returneaza pozitia la care se gaseste prima aparitie a unui element
print(l.index('mere'))

# count --> returneaza numarul de aparitii al unui element intr-o lista
l.extend([2, 2, 2, 2, 3, 1, 2, 3, 4, 12])
print(l.count(2))

# sort --> sorteaza o lista in place (il modifica pe l)
print(l)
l.remove('Ana are mere')
l.pop(2)
print(l)
print(l.sort())
print(l)

# reverse --> inverseaza o lista (in place)
l.reverse()
print(l)

# copy --> returneaza o copie a unei liste.
l2 = l
l_copy = l.copy()

print(l)
print(l2)
print(l_copy)

l_copy[0] = 120
print('#' * 23)
print(l)
print(l2)
print(l_copy)

l2[0] = "Ana are mere"
print('#' * 23)
print('l     ', l)
print('l2    ', l2)
print('l_copy', l_copy)


# list operators: 
# +, *, in/not in, [], [::]

# + --> returneaza o lista noua (rezultat al concatenarii celor 2)
print([1, 2, 3] + ['a', 'b', 'c'])

# * --> operatorul de repetare; returneaza o lista repetata de x ori
print([1, 2, 3] * 5)

# operatorii in/not in --> returneaza True/False daca sau nu un element este in lista: 
print(1 in [1, 2, 3]) # True
print(1 not in [1, 2, 3]) # False

# [] si [::]
l = [2, 2, 2, 2, 3, 1, 2, 3, 4, 12]
print(l[0])
print(l[-1])
print(l[:5])
print(l[:-5])
print(l[::-1])