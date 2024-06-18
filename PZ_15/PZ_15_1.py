import sqlite3

# Создание таблицы "Торговая точка"
conn = sqlite3.connect('rental.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS TorgovajaТochka
             (etazh integer, ploshchad real, konditsioner integer, stoimost_arendy real)''')
conn.commit()

# Функция для ввода данных в БД
def vvod_dannykh():
    # Список данных для вставки
    data = [
        (1, 50.5, 1, 100.0),
        (2, 75.0, 0, 120.0),
        (1, 40.0, 1, 80.0),
        (3, 100.0, 1, 150.0),
        (2, 60.0, 0, 110.0),
        (1, 45.0, 0, 90.0),
        (4, 120.0, 1, 200.0),
        (3, 80.0, 0, 130.0),
        (2, 55.0, 1, 105.0),
        (5, 150.0, 1, 250.0)
    ]

    # Вставка данных в таблицу
    c.executemany("INSERT INTO TorgovajaТochka VALUES (?, ?, ?, ?)", data)
    conn.commit()
    print("Данные успешно добавлены в БД.")

    # Ввод новых данных
    while True:
        etazh = int(input("Введите этаж: "))
        ploshchad = float(input("Введите площадь: "))
        konditsioner = int(input("Наличие кондиционера (0 - нет, 1 - да): "))
        stoimost_arendy = float(input("Введите стоимость аренды в день: "))

        # Вставка новых данных в таблицу
        c.execute("INSERT INTO TorgovajaТochka VALUES (?, ?, ?, ?)", (etazh, ploshchad, konditsioner, stoimost_arendy))
        conn.commit()
        print("Данные успешно добавлены в БД.")

        cont = input("Добавить еще данные? (да/нет): ")
        if cont.lower() != 'да':
            break

# Функция для поиска данных в БД
def poisk_dannykh():
    # Ввод этажа для поиска
    etazh = int(input("Введите этаж для поиска: "))

    # Поиск данных в таблице по этажу
    c.execute("SELECT * FROM TorgovajaТochka WHERE etazh = ?", (etazh,))
    results = c.fetchall()
    if results:
        # Вывод найденных данных
        for row in results:
            print(f"Этаж: {row[0]}, Площадь: {row[1]}, Кондиционер: {row[2]}, Стоимость аренды: {row[3]}")
    else:
        print("Торговые точки на указанном этаже не найдены.")

    # Ввод площади для поиска
    ploshchad = float(input("Введите площадь для поиска: "))

    # Поиск данных в таблице по площади
    c.execute("SELECT * FROM TorgovajaТochka WHERE ploshchad = ?", (ploshchad,))
    results = c.fetchall()
    if results:
        for row in results:
            print(f"Этаж: {row[0]}, Площадь: {row[1]}, Кондиционер: {row[2]}, Стоимость аренды: {row[3]}")
    else:
        print("Торговые точки с указанной площадью не найдены.")

    # Ввод наличия кондиционера для поиска
    konditsioner = int(input("Введите наличие кондиционера для поиска (0 - нет, 1 - да): "))

    # Поиск данных в таблице по наличию кондиционера
    c.execute("SELECT * FROM TorgovajaТochka WHERE konditsioner = ?", (konditsioner,))
    results = c.fetchall()
    if results:
        for row in results:
            print(f"Этаж: {row[0]}, Площадь: {row[1]}, Кондиционер: {row[2]}, Стоимость аренды: {row[3]}")
    else:
        print("Торговые точки с указанным наличием кондиционера не найдены.")


# Функция для удаления данных из БД
def udalenie_dannykh():
    # Ввод этажа для удаления
    etazh = int(input("Введите этаж для удаления: "))

    # Удаление данных из таблицы по этажу
    c.execute("DELETE FROM TorgovajaТochka WHERE etazh = ?", (etazh,))
    conn.commit()
    print(f"{c.rowcount} строк удалено.")

    # Ввод площади для удаления
    ploshchad = float(input("Введите площадь для удаления: "))

    # Удаление данных из таблицы по площади
    c.execute("DELETE FROM TorgovajaТochka WHERE ploshchad = ?", (ploshchad,))
    conn.commit()
    print(f"{c.rowcount} строк удалено.")

    # Ввод наличия кондиционера для удаления
    konditsioner = int(input("Введите наличие кондиционера для удаления (0 - нет, 1 - да): "))

    # Удаление данных из таблицы по наличию кондиционера
    c.execute("DELETE FROM TorgovajaТochka WHERE konditsioner = ?", (konditsioner,))
    conn.commit()
    print(f"{c.rowcount} строк удалено.")


# Функция для редактирования данных в БД
def redaktirovanie_dannykh():
    # Ввод этажа для редактирования
    etazh = int(input("Введите этаж для редактирования: "))

    # Ввод новых данных
    ploshchad = float(input("Введите новую площадь: "))
    konditsioner = int(input("Наличие кондиционера (0 - нет, 1 - да): "))
    stoimost_arendy = float(input("Введите новую стоимость аренды в день: "))

    # Обновление данных в таблице по этажу
    c.execute("UPDATE TorgovajaТochka SET ploshchad = ?, konditsioner = ?, stoimost_arendy = ? WHERE etazh = ?",
              (ploshchad, konditsioner, stoimost_arendy, etazh))
    conn.commit()
    print(f"{c.rowcount} строк обновлено.")

    # Обновление данных в таблице по площади
    c.execute("UPDATE TorgovajaТochka SET etazh = ?, konditsioner = ?, stoimost_arendy = ? WHERE ploshchad = ?",
              (etazh, konditsioner, stoimost_arendy, ploshchad))
    conn.commit()
    print(f"{c.rowcount} строк обновлено.")

    # Обновление данных в таблице по наличию кондиционера
    c.execute("UPDATE TorgovajaТochka SET etazh = ?, ploshchad = ?, stoimost_arendy = ? WHERE konditsioner = ?",
              (etazh, ploshchad, stoimost_arendy, konditsioner))
    conn.commit()
    print(f"{c.rowcount} строк обновлено.")


# Главное меню программы
while True:
    print("\nГлавное меню:")
    print("1. Ввод данных")
    print("2. Поиск данных")
    print("3. Удаление данных")
    print("4. Редактирование данных")
    print("5. Выход")

    choice = input("Выберите действие (1-5): ")

    if choice == '1':
        vvod_dannykh()
    elif choice == '2':
        poisk_dannykh()
    elif choice == '3':
        udalenie_dannykh()
    elif choice == '4':
        redaktirovanie_dannykh()
    elif choice == '5':
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")

conn.close()