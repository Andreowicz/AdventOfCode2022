f = open(r"c:\Users\u-45886\AdventOfCode2022\2022\06\input", "r")
sequence = f.read()

proof = []
sol = 0
i = 1
for c in sequence:
    if c in proof:
        proof = [c]
    else:
        proof.append(c)
    if len(proof) == 4:
        print(proof)
        sol = i
        break
    i += 1

print(sol-1)
    