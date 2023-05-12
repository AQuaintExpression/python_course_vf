# stringuri "asdkifhkj32490167234&*^@!%#$&^*@#$%" 'jlkadhsfjksd'
# stringuri pe mai multe randuri

string_multiline = """linia 1 a stringului
asta este o alta linie
linia 3
"""

# print (string_multiline)

s = "\"Mom\'s spaghetti\" is a line in Eminem\'s song."
print(s)

# string methods/functii
#s.lower() --> tranforma toate caracterele in litere mici
# s = s.lower()
print(s.lower())
# print(s)

#.upper() --> transforma toate caracterele in litere mari: 
print(s.upper())
# print(s)

#s.strip() --> elimina spatii/new line de la inceput/sfarsit de string
print('    \n    hello   ')
print('    \n    hello   '.strip())

#s.replace() --> inlocuieste un substring cu un altul 
print('Ana are mere')
print('Ana are mere'.replace('Ana', 'Ema')) #ce vreau sa inlocuiesc urmat de cu ce vreau sa inlocuiesc

#s.split() --> separa un sir de caractere dupa spatiu(default) sau dupa ce vrem noi
print(s.split()) #separa dupa spatii by default
print('1#4#10'.split('#'))

#s.join() --> ia o lista de stringuri si o uneste folosind un separator. 
print('#'.join(['"Mom\'s', 'spaghetti"', 'is', 'a', 'line', 'in', "Eminem's", 'song.']))

#s.find() --> returneaza pozitia unui substring in string 
print('Ana are 3 mere si are 2 porcale'.find('are'))

#s.startswith() --> returneaza True/False 
print(s.startswith('Ana'))
print(s.startswith('"Mom'))

#s.endswith() --> returneaza True/False daca stringul se termina cu subsirul
print('Ana are mere'.endswith('mere'))

# inlantuire 

print('   anA aRe mere  '.strip().lower().capitalize())

# string operators: 
# + * in not in [] [::] 
# operatorul + --> returneaza 'suma' a 2 stringuri (concatenarea lor)

print('Ana ' + 'are ' + str(3) + ' mere')

# operatorul * --> returneaza un string repetat de x ori
x = 5
s = 'Ana_are_mere'

print(s * x)

# in si not in -> returneaza True/False daca un substring este/nu intr-un altul:

print('mere' in s)
print('portocale' in s)

print('mere' not in s)
print('portocale' not in s)


# operatorul [] (indexing):
print(s[0])
print(s[11], s[-1])

# s[0] = 'a'
print(s)

# slicing [start:end:step] (daca nu ii punem)
print(s[0:4:-1]) # Ana
print(s[::]) # tot stringul
print(s[::-1]) # tot stringul inversat
print(s[::2])

substring_s = s[8::]
print(substring_s[::-1])
print(s[4:])


# string formating. %, s.format(), f-string 
# f"adsfasdgasdg"

nr_mere = 5
nr_banane = 2
nr_mango = 23
print(f"Ana are {nr_mere} mere")
print(f"Ana are {nr_mere} mere, {nr_banane} banane si {nr_mango} mango!")
print("Ana are {} mere, {} banane si {} mango!".format(nr_mere, nr_banane, nr_mango))
print(f'Suma lui 2 si 3 este {2 + 3}')