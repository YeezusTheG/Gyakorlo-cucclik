abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
kódolnivaló = open("open.txt", "r")
eltolás = int(input("Adjá kulcsot:  "))
kódoltcuccli = ''
for i in kódolnivaló.read():
    if i.upper() not in abc:
        kódoltcuccli += i
    else:
        eltolósdi = abc.index(i.upper()) + eltolás
        if eltolósdi > len(abc):
            eltolósdi = len(abc)-(abc.index(i.upper()) + eltolás)
        else:
            eltolósdi = abc.index(i.upper()) + eltolás
        kódoltcuccli += abc[eltolósdi]

kódolnivaló = open("open.txt", "a")
kódolnivaló.write("\n" + kódoltcuccli)