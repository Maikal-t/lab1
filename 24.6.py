my_set1 = set("3145m")
my_set2 = set("345m")
print(my_set1)
print(my_set2)
new_set = set()
for el in my_set1 and my_set2:
    new_set.add(el)
print("Элементы в обоих множествах :\r")
print(new_set)
