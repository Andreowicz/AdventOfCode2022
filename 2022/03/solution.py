from string import ascii_lowercase, ascii_uppercase

f = open(r"c:\Users\u-45886\AdventOfCode2022\2022\03\input", "r")
liste = f.read().split("\n")
i = 1
d = {}
for c in ascii_lowercase:
    d[c] = i
    i = i + 1
for c in ascii_uppercase:
    d[c] = i
    i = i + 1
sol = 0
for element in liste:
    half = int(len(element)/2)
    low = element[0:half]
    high = element[-1*half:]
    for character in low:
        if character in high:
            sol = sol + d[character]
            break
print(sol)

sol = 0
i = 0
while i < 300:
    comp1 = liste[i]
    comp2 = liste[i+1]
    comp3 = liste[i+2]
    for character in comp1:
        if character in comp2:
            if character in comp3:
                sol = sol + d[character]
                print(comp1 + ' ' + comp2 + ' ' + comp3 + ' ' + str(d[character]) + ' ' + str(sol))
                i = i + 3
                break
print(sol)

