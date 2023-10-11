a = input("Введите слово:\n")
count_w = 0
count_n = 0
count_s = 0
spis3 = ["A", "E", "I", "O", "U", "Y", "a", "e", "i", "o", "u", "y"]
symbols = list(a)
print(symbols)
prev = ""
for symbol in symbols:
    if symbol in spis3:
        count_s += 1
    if prev.isupper() and symbol.isupper():
        count_w += 1
    elif prev.islower() and symbol.islower():
        count_n += 1
    prev = symbol
print(f"Количество пар верхнего и нижнего регистра: {count_w, count_n}")
print(f"Количество гласных букв: {count_s}")
