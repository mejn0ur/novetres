#programa testa se existe vogal em palavra

print 'Entre com a palavra:'
pal = str(raw_input('-> '))

a = 0
b = 1
cont = 0

while b != (len(pal) + 1):
    if pal[a:b] == 'a' or 'A':
        cont = cont + 1
    elif pal[a:b] == 'e' or 'E':
        cont = cont + 1
    elif pal[a:b] == 'i' or 'I':
        cont = cont + 1
    elif pal[a:b] == 'o' or 'O':
        cont = cont + 1
    elif pal[a:b] == 'u' or 'U':
        cont = cont + 1
    a = a + 1
    b = b + 1