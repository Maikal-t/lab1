list1 = ["золото", 2400, 1]
list2 = ["золото", 1960, 2]
list3 = ["позолоченное", 560, 1]
list4 = ["золото", 970, 4]
my_dict = {
    "Кольцо": list1,
    "Цепочка": list2,
    "Позолоченное кольцо": list3,
    "Серьги": list4,
}

print("Программа ювелирного магазина")
b = 0
l = 0

while b == 0:
    print(
        "1. Просмотр описания: название – описание\n2. Просмотр цены: название – цена.\n3. Просмотр количества: название – количество.\n4. Вся информация.\n5. Покупка.\n6. До свидания"
    )
    a = int(input("Введите необходимое действие:\n"))

    if a > 0 and a < 7:
        if a == 1:
            for key, value in my_dict.items():
                print(f"{key} - {value[0]}")
        if a == 2:
            for key, value in my_dict.items():
                print(f"{key} - {value[1]}")
        if a == 3:
            for key, value in my_dict.items():
                print(f"{key} - {value[2]}")
        if a == 4:
            for key, value in my_dict.items():
                print(f"{key} - {value}")
        if a == 5:
            c = input(
                "Введите необходимый товар или напишите 'неправильно', чтобы выйти из этой части программы (Не забывайте писать название товара с большой буквы):\n"
            )
            if c in my_dict:
                print("Такой товар есть в наличии:")
                print("Хотите приобрести?")
                while l == 0:
                    v = int(
                        input(
                            "Введите необходимое действие:\n1. - Приобрести\n2. - Вернутся назад :\n"
                        )
                    )
                    if v == 1:
                        n = input("Введите необходимое количество:\n")
                        if n.isdigit() == False:
                            print('Введёное вами значение не является целым, положительным числом.')
                        else:
                          n =  int (n)
                          if n > 0 and n <= my_dict[c][2]:
                            s = my_dict[c][1] * n
                            my_dict[c][2] -= n
                            print("Общая сумма:")
                            print(s)
                            print("Количество оставшихся товаров:")
                            print(my_dict[c][2])
                          else:
                            print(
                                "Данного количества товара нет в магазине или введено число 0."
                            )
                    elif v == 2:
                        print("Вы вышли из этой части программы")
                        break
                    else:
                        print("Вы ввели несуществующее действие. Повторите попытку!!!")
            else:
                print("Такой товар не существует или название введено с ошибкой!!!")
        if a == 6:
            print("До свидания!!!")
            break
    else:
        print("Вы ввели несуществующее действие. Повторите попытку!!!")
