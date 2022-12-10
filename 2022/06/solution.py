f = open(r"c:\Users\u-45886\AdventOfCode2022\2022\06\input", "r")
sequence = f.read()

proof = []
sol = 0
i = 1
for c in sequence:
    if c in proof:
        index = proof.index(c)
        proof = proof[index+1:]
        proof.append(c)
    else:
        proof.append(c)
    if len(proof) == 14:
        print(proof)
        sol = i
        break
    i += 1

print(sol)
    