# # задача 8.1
# sum_ = 0
# input_number = int(input("введите число: "))
# while input_number != 0:
#     sum_ += input_number
#     input_number = int(input("введите число :"))
# print("ответ:", sum_)
#

# задача 8.2
# итерация по ключу
berries = {'strawberry': {'kind': 'red', 'price': 200},
           'raspberry': {'kind': 'yellow', 'price': 300},
           'blueberries': {'kind': 'blue', 'price': 150}
           }
for value in berries.keys():
    print(value)

# итерация по значению
berries = {'strawberry': {'kind': 'red', 'price': 200},
           'raspberry': {'kind': 'yellow', 'price': 300},
           'blueberries': {'kind': 'blue', 'price': 150}
           }
for value in berries.values():
    print(value)

# итерация по паре - ключ - значение
berries = {'strawberry': {'kind': 'red', 'price': 200},
           'raspberry': {'kind': 'yellow', 'price': 300},
           'blueberries': {'kind': 'blue', 'price': 150}
           }
for value in berries.items():
    print(value)

# множественное присваивание
berries = {'strawberry': {'kind': 'red', 'price': 200},
           'raspberry': {'kind': 'yellow', 'price': 300},
           'blueberries': {'kind': 'blue', 'price': 150}
           }
for index, value in berries.items():
    print(index, value)

# двухмерный список
for i in range(0, 10):
    for j in range(0, 11):
        print(j, end=" ")
    print(i)
