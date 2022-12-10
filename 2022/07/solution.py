f = open(r"c:\Users\u-45886\AdventOfCode2022\2022\07\input", "r")
liste = f.read().split("\n")


tree = {"/":0}
current = ""
totalused = 0 
i = 0
for element in liste:
    #print(element)
    if element == "$ cd /":
        current = "/"
        continue

    commands = element.split(' ')
    if commands[0] == '$':
        if commands[1] == "cd":
            if commands[2] == "..":
                current = current.rsplit('/', 2)[0] + '/'
            else:
                current += commands[2] + '/'
                tree.setdefault(current, 0)
    elif commands[0].isnumeric():
        totalused += int(commands[0])
        countfolder = len(current[1:-1].split('/'))
        tree["/"] += int(commands[0])
        if current != "/":
            for i in range(0,countfolder):
                currentadd = '/' + (current[1:-1].rsplit('/',i)[0]) + '/'
                tree[currentadd] += int(commands[0])

#part1
treelower = {k: v for k, v in tree.items() if v <= 100000}
print(sum(treelower.values()))

#part2
candidates = []
for key, value in tree.items():
    #print(key, value)
    if (30000000-(70000000-totalused) - value) <= 0:
        candidates.append(value)

print(min(candidates))



