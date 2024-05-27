# задача 7_1
# month = 13
# if month in [1, 2, 12]:
#     print('winter')
# elif month in [3, 4, 5]:
#     print('spring')
# elif month in [6, 7, 8]:
#     print('summer')
# elif month in [9, 10, 11]:
#     print('autumn')
# else:
#     print('некоректный номер месяца')

# # задача 7.2
# is_logged_in = True
# has_items_in_cart = True
# has_shipping_address = True
# has_order = False
# if is_logged_in and has_items_in_cart and has_shipping_address:
#     print("все критерии для оформления заказа выполнены. заказ может быть оформлен")
#     has_order = True
# else:
#     print("не все критерии для оформления заказа выполнены. пожалуйста, проверьте информацию")
# is_first_order = False
# min_purchase = 1000
# total_purchase = 900
# if has_order and (is_first_order or total_purchase >= min_purchase):
#     print("вы получаете скидку!")
# else:
#     print("вы не получаете скидку")

# задача 7.3
number = 7
if number in [7, 13, 21]:
    print("счастливое число!")
elif number in range(1, 101):
    print("число в указанном диапазоне")
else:
    print("не повезло")
