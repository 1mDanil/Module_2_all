import random

def pervyi_stolbik():
    num = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    numbers = range(3,20)
    vibor = random.choice(numbers)
    return vibor

def password(a):
    pass_ = {}
    pass_.update({3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645, 10: 141923283746, 11: 11029384756, 12: 12131511124210394857, 13: 112211310495867})
    pass_.update({14: 1611325212343114105968, 15: 1214114232133124115106978, 16:1317115262143531341251161079, 17:11621531441351261171089})
    pass_.update({18: 12151811724272163631545414513612711810, 19: 118217316415514613712811910, 20:13141911923282183731746416515614713812911})
    key = pass_.get(a)
    return key


n = pervyi_stolbik()

print(n)

pairnum1 = list(range(1,n))
pairnum2 = list(range(1,n))
pari = []
result = ''
end = ''

for i in pairnum1:
    for j in pairnum2:
        numero1 = i
        numero2 = j
        if numero1 >= numero2:
            continue
        else:
            konchilos_voobrajenie = n % (numero1 + numero2)
            if konchilos_voobrajenie == 0:
                pari.append([numero1, numero2])
                end = result + str(numero1), result + str(numero2)

print(pari)
print(result)
print(password(n), ' Exit ')