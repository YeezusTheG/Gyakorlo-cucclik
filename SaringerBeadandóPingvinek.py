import random
#1.feladat
while True:
    hetekszama = int(input("Add meg a hetek számát [1...5]: "))
    if hetekszama <= 5 and hetekszama >= 1:
        break
    else:
        print("Hibás adatbevitel, próbáld újra...")
#2.feladat
támadások = []
i = 1
while i <= hetekszama:
    j =1
    while j <= 7:
        tamadas = random.randint(3,9)
        támadások.append(tamadas)
        j+=1
    i+=1
#3.feladat

#4.feladat
s = 0
for i in támadások:
    s = s + támadások[i]
print(f"Összes támadás száma : {s}db")
#5.feladat
l = 0
for i in range(len(támadások)):
    if támadások[i] <= 8 and támadások[i] >= 5:
        l += 1
print(f"Feltételnek megfelelő napok száma: {l}db")
#6.feladat
MaxÉrték = támadások[0]
MaxIndex = 0
for i in range(len(támadások)):
    if támadások[i] >= MaxÉrték:
        MaxÉrték = támadások[i]
        MaxIndex = i
print(f"Egy napon megtörtént legtöbb támadás száma:{MaxÉrték}")
print(f"Helye: {MaxIndex}, ")