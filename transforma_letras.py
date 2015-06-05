#programa que transforma letras

print 'Entre com uma palavra:'
pal = str(raw_input('-> '))

a = 0
b = 1

pal2 = ''

while b != (len(pal) + 1):
    if pal[a:b] == 'a':
        pal2 = pal2 + 'A'
    elif pal[a:b] == 'A':
        pal2 = pal2 + 'a'
    elif pal[a:b] == 'b':
        pal2 = pal2 + 'B'
    elif pal[a:b] == 'B':
        pal2 = pal2 + 'b'
    elif pal[a:b] == 'c':
        pal2 = pal2 + 'C'
    elif pal[a:b] == 'C':
        pal2 = pal2 + 'c'
    elif pal[a:b] == 'd':
        pal2 = pal2 + 'D'
    elif pal[a:b] == 'D':
        pal2 = pal2 + 'd'
    elif pal[a:b] == 'e':
        pal2 = pal2 + 'E'
    elif pal[a:b] == 'E':
        pal2 = pal2 + 'e'
    elif pal[a:b] == 'f':
        pal2 = pal2 + 'F'
    elif pal[a:b] == 'F':
        pal2 = pal2 + 'f'
    elif pal[a:b] == 'g':
        pal2 = pal2 + 'G'
    elif pal[a:b] == 'G':
        pal2 = pal2 + 'g'
    elif pal[a:b] == 'h':
        pal2 = pal2 + 'H'
    elif pal[a:b] == 'H':
        pal2 = pal2 + 'h'
    elif pal[a:b] == 'i':
        pal2 = pal2 + 'I'
    elif pal[a:b] == 'I':
        pal2 = pal2 + 'i'
    elif pal[a:b] == 'k':
        pal2 = pal2 + 'K'
    elif pal[a:b] == 'K':
        pal2 = pal2 + 'k'
    elif pal[a:b] == 'l':
        pal2 = pal2 + 'L'
    elif pal[a:b] == 'L':
        pal2 = pal2 + 'l'
    elif pal[a:b] == 'm':
        pal2 = pal2 + 'M'
    elif pal[a:b] == 'M':
        pal2 = pal2 + 'm'
    elif pal[a:b] == 'n':
        pal2 = pal2 + 'N'
    elif pal[a:b] == 'N':
        pal2 = pal2 + 'n'
    elif pal[a:b] == 'm':
        pal2 = pal2 + 'M'
    elif pal[a:b] == 'M':
        pal2 = pal2 + 'm'
    elif pal[a:b] == 'n':
        pal2 = pal2 + 'N'
    elif pal[a:b] == 'N':
        pal2 = pal2 + 'n'
    elif pal[a:b] == 'o':
        pal2 = pal2 + 'O'
    elif pal[a:b] == 'O':
        pal2 = pal2 + 'o'
    elif pal[a:b] == 'p':
        pal2 = pal2 + 'P'
    elif pal[a:b] == 'P':
        pal2 = pal2 + 'p'
    elif pal[a:b] == 'q':
        pal2 = pal2 + 'Q'
    elif pal[a:b] == 'Q':
        pal2 = pal2 + 'q'
    elif pal[a:b] == 'r':
        pal2 = pal2 + 'R'
    elif pal[a:b] == 'R':
        pal2 = pal2 + 'r'
    elif pal[a:b] == 's':
        pal2 = pal2 + 'S'
    elif pal[a:b] == 'S':
        pal2 = pal2 + 's'
    elif pal[a:b] == 't':
        pal2 = pal2 + 'T'
    elif pal[a:b] == 'T':
        pal2 = pal2 + 't'
    elif pal[a:b] == 'u':
        pal2 = pal2 + 'U'
    elif pal[a:b] == 'U':
        pal2 = pal2 + 'u'
    elif pal[a:b] == 'v':
        pal2 = pal2 + 'V'
    elif pal[a:b] == 'V':
        pal2 = pal2 + 'v'
    elif pal[a:b] == 'w':
        pal2 = pal2 + 'W'
    elif pal[a:b] == 'W':
        pal2 = pal2 + 'w'
    elif pal[a:b] == 'x':
        pal2 = pal2 + 'X'
    elif pal[a:b] == 'X':
        pal2 = pal2 + 'x'
    elif pal[a:b] == 'y':
        pal2 = pal2 + 'Y'
    elif pal[a:b] == 'Y':
        pal2 = pal2 + 'y'
    elif pal[a:b] == 'z':
        pal2 = pal2 + 'Z'
    elif pal[a:b] == 'Z':
        pal2 = pal2 + 'z'

    a = a + 1
    b = b + 1

print 'A nova palavra e: ', pal2