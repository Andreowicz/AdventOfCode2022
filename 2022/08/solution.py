f = open(r"c:\Users\u-45886\AdventOfCode2022\2022\08\input", "r")
liste = f.read().split("\n")


def lookTree(m, n, toi):
    edges = 4
    for neighbor in range(0,n):
        if int(toi) <= int(liste[m][neighbor]):
            edges -= 1
            break
    for neighbor in range(n+1, 99):
        if int(toi) <= int(liste[m][neighbor]):
            edges -= 1
            break
    for neighbor in range(0,m):
        if int(toi) <= int(liste[neighbor][n]):
            edges -= 1
            break
    for neighbor in range(m+1, 99):
        if int(toi) <= int(liste[neighbor][n]):
            edges -= 1
            break
    return(int(edges))

def lookTreeHouse(m, n, toi):
    treest = 0
    treesl = 0
    treesr = 0
    treesd = 0
    for neighbor in range(n-1,-1,-1):
        if int(toi) > int(liste[m][neighbor]):
            treesl += 1
        elif int(toi) <= int(liste[m][neighbor]):
            treesl += 1
            break
    for neighbor in range(n+1, 99):
        if int(toi) > int(liste[m][neighbor]):
            treesr += 1
        elif int(toi) <= int(liste[m][neighbor]):
            treesr += 1
            break
    for neighbor in range(m-1,-1,-1):
        if int(toi) > int(liste[neighbor][n]):
            treest += 1
        elif int(toi) <= int(liste[neighbor][n]):
            treest += 1
            break
    for neighbor in range(m+1, 99):
        if int(toi) > int(liste[neighbor][n]):
            treesd += 1
        elif int(toi) <= int(liste[neighbor][n]):
            treesd += 1
            break
    return(int(treest*treesl*treesr*treesd))


m = 0
n = 0
visible = 0
spotheights = []
for element in liste:
    for tree in element:
        #part1
        if m == 0 or m == 98 or n == 0 or n == 98:
            visible += 1
        else:
            if lookTree(m, n, tree) > 0:
                visible += 1
        #part2
        spotheights.append(lookTreeHouse(m, n, tree))
        n += 1
    m += 1
    n = 0

print(visible)
print(spotheights)
print(len(spotheights))
print(max(spotheights))
