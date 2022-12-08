f = open(r"c:\Users\u-45886\AdventOfCode2022\2022\04\input", "r")
liste = f.read().split("\n")

sol = 0
sol2 = 0 
for pair in liste:
    (first, second) = pair.split(',')
    (lowerf, upperf) = first.split('-')
    (lowers, uppers) = second.split('-')
    if (int(lowerf) >= int(lowers) and int(upperf) <= int(uppers)) or \
       (int(lowers) >= int(lowerf) and int(uppers) <= int(upperf)):
        sol += 1
    if (int(upperf) < int(lowers)) or (int(uppers) < int(lowerf)):
        sol2 += 1


print(sol)
print(1000-sol2)