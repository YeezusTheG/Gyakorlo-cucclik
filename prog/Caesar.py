with open("text.txt") as f:
    lines = f.readlines()
abc = "AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ"
kódolnivaló = open("text.txt", "r")
kész_kód = ''
while True:
    eltolás_számérték = int(input("Adjá kulcsot:  "))
    if eltolás_számérték < len(abc):
        break
    else:
        print("Hibás érték, maximum 34")
if len(lines) > 1:
    print("A kódolni való üzenetnek több sora van, kérlek egysoros üzenetet adj meg.")
for i in kódolnivaló.read():
    if i.upper() not in abc:
        kész_kód += i
    else:
        eltolási_index_az_ABCben = abc.index(i.upper()) + eltolás_számérték
        if eltolási_index_az_ABCben > len(abc):
            eltolási_index_az_ABCben = len(abc)-(abc.index(i.upper()) + eltolás_számérték)
        else:
            eltolási_index_az_ABCben = abc.index(i.upper()) + eltolás_számérték
        kész_kód += abc[eltolási_index_az_ABCben]

kódolnivaló = open("text.txt", "a")
kódolnivaló.write("\n" + kész_kód)