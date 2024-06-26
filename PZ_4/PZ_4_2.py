#Дано целое число N (>0). С помощью операций деления нацело и взятия остатка от
#деления определить, имеется ли в записи числа N цифра «2». Если имеется, то
#вывести TRUE, если нет — вывести FALSE.


N = int(input("Введите целое число N: "))  # Запросить у пользователя целое число N

while type(N) != int:  # Обработка исключений, если пользователь ввел не целое число
    try:
        N = int(N)
    except ValueError:
        print("Неправильно ввели!")
        N = input("Введите целое число N: ")
has_digit_2 = False  # Флаг для отслеживания наличия цифры 2

# Проверяем каждую цифру числа N, пока N не станет равным 0
while N != 0:
    digit = N % 10  # Получаем последнюю цифру числа N
    if digit == 2:
        has_digit_2 = True
        break  # Если найдена цифра 2, выходим из цикла
    N = N // 10  # Удаляем последнюю цифру числа N

# Выводим результат
if has_digit_2:
    print("TRUE")
else:
    print("FALSE")