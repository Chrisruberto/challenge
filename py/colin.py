def score(name, pos):
    score = 0

    for letra in name:
        if letra == "A": score += 1
        elif letra == "B": score += 2
        elif letra == "C": score += 3
        elif letra == "D": score += 4
        elif letra == "E": score += 5
        elif letra == "F": score += 6
        elif letra == "G": score += 7
        elif letra == "H": score += 8
        elif letra == "I": score += 9
        elif letra == "J": score += 10
        elif letra == "K": score += 11
        elif letra == "L": score += 12
        elif letra == "M": score += 13
        elif letra == "N": score += 14
        elif letra == "O": score += 15
        elif letra == "P": score += 16
        elif letra == "Q": score += 17
        elif letra == "R": score += 18
        elif letra == "S": score += 19
        elif letra == "T": score += 20
        elif letra == "U": score += 21
        elif letra == "V": score += 22
        elif letra == "W": score += 23
        elif letra == "X": score += 24
        elif letra == "Y": score += 25
        elif letra == "Z": score += 26
        else: score += 0
    # Termina el bucle

    return score * pos
#termina funcion es.

f = open('names.txt')
string = f.readlines()
f.close()

nombres = sorted(str(string).split(","))
tscore = 0
pos = 1

for name in nombres:
    tscore += score(name, pos)
    pos += 1
#end for loop.

print (tscore)