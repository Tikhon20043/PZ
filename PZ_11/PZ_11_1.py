#Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
#последовательности из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Элементы первого и второго файлов:
#Количество элементов первого и второго файлов:
#Индекс первого минимально элемента первого файла:
#Индекс последнего максимального элемента второго файла:
#Элементы кратные 4 первого и второго файлов:


# Генерация последовательности чисел
numbers1 = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]  # Пример последовательности для первого файла
numbers2 = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50]  # Пример последовательности для второго файла

# Запись последовательностей в файлы
with open('file1.txt', 'w') as file:
    for number in numbers1:
        file.write(str(number) + '\n')

with open('file2.txt', 'w') as file:
    for number in numbers2:
        file.write(str(number) + '\n')


# Чтение последовательностей из файлов
with open('file1.txt', 'r') as file:
    numbers1 = [int(line) for line in file.readlines()]

with open('file2.txt', 'r') as file:
    numbers2 = [int(line) for line in file.readlines()]

# Выполнение требуемой обработки
result = []
result.append(f'Элементы первого файла: {numbers1}')
result.append(f'Элементы второго файла: {numbers2}')
result.append(f'Количество элементов первого файла: {len(numbers1)}')
result.append(f'Количество элементов второго файла: {len(numbers2)}')
result.append(f'Индекс первого минимального элемента первого файла: {numbers1.index(min(numbers1))}')
result.append(f'Индекс последнего максимального элемента второго файла: {len(numbers2) - 1 - numbers2[::-1].index(max(numbers2))}')
result.append(f'Элементы кратные 4 первого файла: {[num for num in numbers1 if num % 4 == 0]}')
result.append(f'Элементы кратные 4 второго файла: {[num for num in numbers2 if num % 4 == 0]}')

# Запись результата в новый файл
with open('result.txt', 'w') as file:
    for line in result:
        file.write(line + '\n')