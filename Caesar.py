abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
code = input("Adjal man meg textet: ")
encryptionkey = int(input("Adjá kulcsot:  "))
encryptedcode = ''
for i in code:
    if i.upper() in abc:
        index = abc.index(i.upper())
        encryptedcode = encryptedcode + abc[index + encryptionkey]

print(encryptedcode)



abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
code = input("Adjal man meg textet: ")
decritionkey = int(input("Adjá kulcsot:  "))
decryptedcode = ''
for i in code:
    if i.upper() in abc:
        index = abc.index(i.upper())
        decryptedcode = decryptedcode + abc[index - encryptionkey]

print(decryptedcode)