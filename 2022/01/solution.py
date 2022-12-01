f = open("input", "r")
liste = f.read().split("\n")
a = 0
i = 1
d = {}
for element in liste:
    if element == '':
        d[i] = a
        i = i + 1
        a = 0
        continue
    a = a + int(element)
sol1 = (sorted(d, key=d.get)[-1])
zsol = (sorted(d, key=d.get)[-3:])
sol2 = 0
for e in zsol:
    sol2 = sol2 + d[e]