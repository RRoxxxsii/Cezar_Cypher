def english_cypher(s: str, n:int) -> int:
    eng_alpha = [chr(i) for i in range(ord('a'), ord('z')+1)]
    eng_alpha_upper = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    cyphered = []
    for i in s:
        if i in eng_alpha:
            cyphered.append((eng_alpha.index(i) + n) % 26)
        else:
            cyphered.append(i)

    cyphered1 = []
    for i in cyphered:
        if str(i).isdigit():
            cyphered1.append(eng_alpha[i])
        else:
            cyphered1.append(i)
    for i in cyphered1:
        if i.isupper():
            cyphered1[cyphered1.index(i)] = (eng_alpha_upper.index(i) + n) % 26

    for i in cyphered1:
        if str(i).isdigit():
            cyphered1[cyphered1.index(i)] = eng_alpha_upper[i]

    return ''.join(cyphered1)

s = input()

a = [(len(i.strip(',!.?"'))) for i in s.split()]
lst = []
for i in a:
    lst.append((english_cypher(s, i)))
for i in range(len(lst)):
    print(lst[i].split()[i], end=' ')
