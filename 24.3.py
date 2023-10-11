spisok = [
    1,
    3,
    4,
    6,
    7,
    8,
]
a = 1
new_spisok = []
for el in spisok:
    if spisok.index(el) % 2 == 0:
        new_spisok.append(el)
        a *= el
print(new_spisok)
print("Произведение четных :")
print(a)
