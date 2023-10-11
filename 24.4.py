a = str(input("Введите  первую строку :\n"))
b = str(input("Введите  вторую строку :\n"))
print("Вы ввели :")
print(a)
print(b)
str_reverse = a[::-1]
print(str_reverse)
if b == str_reverse:
    print("Строки являются анаграммами")
else:
    print("Строки не являются анаграммами")
