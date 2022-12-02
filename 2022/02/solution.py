f = open(r"c:\Users\u-45886\AdventOfCode2022\2022\02\input", "r")
liste = f.read().split("\n")
sumround = 0
sumtotal = 0
for element in liste:
    (you, me) = element.split(' ')
    if me == 'X':
        me = 'A'
        sumround += 1
    elif me == 'Y':
        me = 'B'
        sumround += 2
    elif me == 'Z':
        me = 'C'
        sumround += 3
    
    if you == me:
        sumtotal += sumround + 3
    elif you == 'A' and me == 'B':
        sumtotal += sumround + 6
    elif you == 'A' and me == 'C':
        sumtotal += sumround 
    elif you == 'B' and me == 'A':
        sumtotal += sumround
    elif you == 'B' and me == 'C':
        sumtotal += sumround + 6
    elif you == 'C' and me == 'A':
        sumtotal += sumround + 6
    elif you == 'C' and me == 'B':
        sumtotal += sumround
    sumround = 0

print(sumtotal)

sumround = 0
sumtotal = 0
for element in liste:
    (you, me) = element.split(' ')
    if me == 'X':
        if you == 'A':
            sumround += 3
        elif you == 'B':
            sumround += 1
        elif you == 'C':
            sumround += 2
    elif me == 'Y':
        sumround = 3
        if you == 'A':
            sumround += 1
        elif you == 'B':
            sumround += 2
        elif you == 'C':
            sumround += 3
    elif me == 'Z':
        sumround = 6
        if you == 'A':
            sumround += 2
        elif you == 'B':
            sumround += 3
        elif you == 'C':
            sumround += 1
    sumtotal += sumround
    sumround = 0

print(sumtotal)