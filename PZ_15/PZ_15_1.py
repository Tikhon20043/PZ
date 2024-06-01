#Приложение СДАЧА В АРЕНДУ ТОРГОВЫХ ПЛОЩАДЕЙ для некоторой
#организации. БД должна содержать таблицу Торговая точка со следующей структурой
#записи: этаж, площадь, наличие кондиционера и стоимость аренды в день.

import sqlite3

# Создание соединения с базой данных
db_connection = sqlite3.connect('rental.db')

# Создание курсора для выполнения запросов
cursor = db_connection.cursor()

# Создание таблицы Rental Point (Торговые точки), если она не существует
cursor.execute('''CREATE TABLE IF NOT EXISTS Rental_Point
                 (floor integer, area real, air_conditioner text, rental_cost real)''')

# Добавление торговых точек
cursor.execute("INSERT INTO Rental_Point VALUES (1, 50.2, 'Да', 2500.99)")
cursor.execute("INSERT INTO Rental_Point VALUES (2, 35.7, 'Нет', 1800.50)")
cursor.execute("INSERT INTO Rental_Point VALUES (3, 45.0, 'Да', 2200.00)")

# Получение и вывод списка всех торговых точек в столбик без цикла for
cursor.execute("SELECT * FROM Rental_Point")
while True:
    point = cursor.fetchone()
    if point is None:
        break
    print(f"Этаж: {point[0]}")
    print(f"Площадь: {point[1]} кв. м")
    print(f"Кондиционер: {point[2]}")
    print(f"Стоимость аренды: {point[3]} руб./день")
    print()

# Закрытие соединения с базой данных
db_connection.close()