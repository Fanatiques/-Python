import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pylab

def read_sales_data(file_path):  # Создаем функцию для чтения файла с продажами
    opened_sales_data = open(file_path, 'r', encoding='utf-8')  #Открываем файл для чтения
    sales_data_str = list(map(str.strip, opened_sales_data.readlines())) # Преобразуем каждую строчку в список и удаляем пробелы
    sales_list = []  # Создаем пустой список для хранения данных о продажах
    for item in sales_data_str:
        splitted_item = list(map(str.strip, item.split(','))) #разделяем строчку по запятой и удаляем пробелы
        data_dict = {'product_name': splitted_item[0], 'quantity': int(splitted_item[1]), 'price': int(splitted_item[2]), 'date': splitted_item[3]} # Создаем словарь с данными о продаже
        sales_list.append(data_dict) # добавляем словарь из каждой итерации цикла в список sales_list
    return sales_list

# Путь к файлу с продажами
file_path = 'Sales_list.txt'
sales_data = read_sales_data(file_path)


def total_sales_per_product(sales_data):
    dict_products = {} # создаем пустой словарь для хранения общей суммы продаж по продуктам
    for product in sales_data:
        name = product['product_name']
        quantity = product['quantity']
        price = product['price']
        if name in dict_products: # если продукт уже есть в словаре - добавляем сумму к уже существующей сумме продаж
            dict_products[name] += quantity * price
        else: # если продукта нет в словаре - создаем ключ:значение суммы продаж для каждого продукта
            dict_products[name] = quantity * price
    return dict_products


def sales_over_time(sales_data):
    dict_products = {} # создаем пустой словарь для хранения суммы продаж для каждой даты
    for product in sales_data:
        date = product['date']
        quantity = product['quantity']
        price = product['price']
        if date in dict_products: # если дата уже есть в словаре - добавляем сумму к уже существующей сумме продаж
            dict_products[date] += quantity * price
        else: # если дата нет в словаре - создаем ключ:значение суммы продаж для каждой даты
            dict_products[date] = quantity * price
    return dict_products

result_total_sales_per_product = total_sales_per_product(sales_data) # создаем словарь с результатами функции total_sales_per_product
max_value_per_product = max(result_total_sales_per_product, key=result_total_sales_per_product.get) #находим продукт с максимальной суммой продаж
print(max_value_per_product) #выводим продукт с максимальной суммой продаж

result_sales_over_time = sales_over_time(sales_data) # создаем словарь с результатами функции sales_over_time
max_value_per_date = max(result_sales_over_time, key=result_sales_over_time.get) #находим дату с максимальной суммой продаж
print(max_value_per_date) #выводим дату с максимальной суммой продаж

x = np.array(list(result_total_sales_per_product.keys())) #создаем массивы для графиков
y = np.array(list(result_total_sales_per_product.values()))
x1 = np.array(list(result_sales_over_time.keys()))
y1 = np.array(list(result_sales_over_time.values()))
f, ax = plt.subplots(figsize=(16,7)) #создаем подложку под графики
plt.axis('off')
pylab.subplot (1, 2, 1)
plt.bar(x, y, width=0.5, color='blue') #рисуем график для суммы продаж по продуктам
pylab.title ("Сумма продаж по продуктам")
pylab.subplot (1, 2, 2) #рисуем график для суммы продаж по дням
plt.bar(x1, y1, width=0.5, color = 'orange')
pylab.title ("Сумма продаж по дням")
plt.show() #отображаем графики







































