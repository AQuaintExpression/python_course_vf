# o insiruire de caractere cuprinsa intre '' sau ""

s = ' A string is a sequence of characters enclosed in single or double quotes!'
s2 = " Ana are mere!"
multiline_string = """asta este o linie
Asta este o alta linie"""

print(s)
print(s2)
print(multiline_string)

my_string = "Ana are mere.\nGeorge vrea si el un mar"
print(my_string)

# \n \r\n \t
print('\tAbracadabra')

# functia len()
print(len(my_string))


s = ' A string is a sequence of characters enclosed in single or double quotes!'
s2 = '\n \tA string is a sequence of characters enclosed in single or double QuoTeS!'
# string methods
# lower, upper, strip, replace, split, join, find, startswith, endswith

#lower --> returneaza un string cu toate literele mici.
print(s.lower())
print(s)

#upper --> returneaza un string cu toate literele mari. 
print(s.upper())

#strip --> returneaza un string fara orice fel de spatii la inceput si final 
print(s2)
print(s2.strip())

#replace --> returneaza un string in care un subsir este inlocuit de un altul pe care il vrem noi. 
print(s.replace('quotes', 'QUOTES'))
print(s)

#split() --> returneaza o lista de substringuri pornind de la stringul original: 
print(s.split())
s_csv = '1,,2,,3,,4'
print(s_csv.split(',,'))

#join --> returneaza un sir concatenand o lista de subsiruri, folosind un separator. 
# 'separator'.join(list_of_substrings)
print('ASD'.join(['A', 'string', 'is', 'a', 'sequence', 'of', 'characters', 'enclosed', 'in', 'single', 'or', 'double', 'quotes!']))

#find --> find returneaza pozitia la care se gaseste un substring intr-un string. 
#    0123456789
s = 'Ana are mere'

print(s.find('are'))

# startswith/endswith --> returneaza True/False daca/nu un sir sir incepe/se termina cu un subsir:
print(s.startswith('ana'))
print(s.startswith('Ana'))
print(s.endswith('mere.'))


print(s2)
# s2 = s2.strip()
# s2 = s2.lower()
# s2 = s2.capitalize() # returneaza un string cu prima litera capitalizata
# print(s2)

s2 = s2.strip().lower().capitalize()
print(s2)

s = "Hello there, I'm Daniel."
print(s)
s = '\"Mom\'s spaghetti\" is one of Eminem\'s songs'
print(s)

# String operators.
# +, *, in, not in, [], [::]

# operatorul + --> returneaza concatenarea a 2 stringuri 
print('Ana' + 'are' + 'mere')
print('Ana', 'are', 'mere', end='', sep=',')
print('!!!')

# operatorul * --> operatorul de repetare a unui string -> returneaza un nou string repetat de x ori
print('#!' * 23)

# operatorii in/not in -> returneaza True/False daca un substring este/nu intr-un alt string: 
print('Ana' in 'Ana are mere') # True
print('George' not in 'Ana are mere') # True

# index operator []: --> returneaza caracterul de la pozitia pe care o vrem. 

s = 'Ana are mere'
print(s[5])
# s[5] = 'R'
print(s[-4])

# operatorul de slicing [::] --> [start:end (not included):step] --> returneaza un subsir/o copie a sirului
print(s[0:12:1])
print(s[0:12:])
print(s[0::])
print(s[::-1]) # --> retuneaza sirul inversat.
print(s[6:3:-1])
print(s[-5:])
print(s[::2])
print(s[1::2])

# string formatting.

nr_mere = 10
nr_portocale = 3
nr_mango = 6
print('Ana are ' + str(nr_mere) + ' mere')
# functia format
print('Ana are {} mere'.format(nr_mere)) # valid in python 2
print('Ana are {} mere, {} portocale si {} mango'.format(nr_mere, nr_portocale, nr_mango)) # valid in python 2
print(f'Ana are {nr_mere} mere, {nr_portocale} portocale si {nr_mango} mango. Deci are in total {nr_mango + nr_mere + nr_portocale} fructe') # f-string literals valid in python 3