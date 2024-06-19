import os

# 1. Перейти в каталог PZ_11 и вывести список файлов
os.chdir('PZ_11')
print("Список файлов в каталоге PZ_11:")
print(os.listdir())

# 2. Создать папку test и в ней папку test1
os.makedirs('test/test1')

# 3. Переместить файлы из ПЗ_6 в папку test
os.rename('PZ_6/file1.txt', 'test/file1.txt')
os.rename('PZ_6/file2.txt', 'test/file2.txt')

# 4. Переместить файл из ПЗ_7 в папку test1 и переименовать
os.rename('PZ_7/file.txt', 'test1/test.txt')
os.rename('test1/file.txt', 'test1/test.txt')

# 5. Вывести информацию о размере файлов в папке test
print("Информация о размере файлов в папке test:")
for file in os.listdir('test'):
    print(f"Файл {file}: {os.path.getsize(os.path.join('test', file))} байт")

# 6. Найти файл с самым коротким именем в папке PZ_11
shortest_file = min(os.listdir('PZ_11'), key=len)
print(f"Файл с самым коротким именем: {os.path.basename(shortest_file)}")

# 7. Найти файл с отчетом в формате .pdf и запустить его
for file in os.listdir():
    if file.endswith('.pdf'):
        os.startfile(file)

# 8. Удалить файл test.txt
os.remove('test1/test.txt')