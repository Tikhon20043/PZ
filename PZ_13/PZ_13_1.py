#1. Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0.

# Генерация исходной матрицы
original_matrix = [[i*j for j in range(1, 5)] for i in range(1, 5)]

# Вывод исходной матрицы
print("Исходная матрица:")
for row in original_matrix:
    print(row)

# Изменение матрицы: замена элементов > 10 на 0
modified_matrix = [[0 if element > 10 else element for element in row] for row in original_matrix]

# Вывод изменённой матрицы
print("\nИзменённая матрица:")
for row in modified_matrix:
    print(row)