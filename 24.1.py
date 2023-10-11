n = int(input("Введите натуральное число :\n"))
sum = 0
# Перебор цифр числа
while n > 0:
    digit = n % 10
    if digit % 2 != 0:
        sum += digit
    n //= 10
if sum > 0:
    print("Сумма нечётных цифр:", sum)
else:
    print("В числе нет нечётных цифр.")
