#В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в 2 раза.

# Создание и вывод исходной матрицы
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print("Исходная матрица:")
for row in matrix:
    print(row)

# Преобразование  матрицы
transformed_matrix = [[row[i] if i == index else row[i] * 2 for i in range(len(row))] for index, row in enumerate(matrix)]

print("\nПреобразованная мартица:")
for row in transformed_matrix:
    print(row)