# exersice 1
str_ = "строка с цифрой 1"
is_substr = "строка" in str_ # True
print("в строке есть слово строка?", is_substr)

# exersice 2
number = 12
condition_1 = number % 2 == 0 # число кратно 2
condition_2 = number % 3 == 0 # число кратно 3
if condition_1  and condition_2:
    print('число кратное 2 и 3')
else:
    print('число не(кратно 2 и 3)')

# exersice 3
mount = 12
# символ \ позволяет визуально разбить команду, для интерпретатора это одна строка
bad_condition = \
mount == 12 or \
mount == 1 or \
mount == 2 # очень плохая запись условия
print("зима!!!")

# exersice 4
hour = 7
bad_condition = (6 <= hour) and (hour < 12) # цепочки операторов всегда соединяются через AND
good_condition = 6 <= hour < 12
if good_condition:
    print("утро!!!")

# exersice 5
list_ = [5, 6, 7, 8, 9]
result = (4 in list_) and (8 in list_)
print(result)
