"""import random

number = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
win = random.choice(number)


result = []

for i in range(1, win):
    if i > (win / 2):
        break
    else:
        for j in range(1, win):
            if (i + j) % win == 0:
                res = []
                res.append(i)
                res.append(j)
                result.append(res)

print(win, result)"""

import random

def get_random():
    num = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    numbers = list(range(3, 21))
    cipher = random.choice(numbers)
    return cipher

n = get_random()
print('Шифр:', n)

pairnum1 = list(range(1, n))
pairnum2 = list(range(1, n))
pairs = []
result = ''

for i in pairnum1:
    for j in pairnum2:
        pn1 = i
        pn2 = j
        if pn1 >= pn2:
            continue
        else:
            kratno = n % (pn1 + pn2)
            if kratno == 0:
                pairs.append([pn1, pn2])
                result = result + str(pn1) + str(pn2)
print('Пары чисел', *pairs)
print('Пароль', result)