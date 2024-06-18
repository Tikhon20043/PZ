#Текстовый файл состоит из символов I, U, V, W, X, U и Z.
#Определите в прилагаемом файле максимальное количество идущих подряд символов (длину непрерывной подпоследовательности),
#среди которых символ Х встречается не более 140 раз.

def find_max_continuous_subsequence(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    max_length = 0
    current_length = 0
    x_count = 0

    for char in text:
        if char in ['I', 'U', 'V', 'W', 'X', 'U', 'Z']:
            current_length += 1
            if char == 'X':
                x_count += 1
            if x_count > 140:
                current_length = 0
                x_count = 0
        else:
            current_length = 0
            x_count = 0
        max_length = max(max_length, current_length)

    return max_length

# Пример использования
file_path = '313_24.txt'
max_length = find_max_continuous_subsequence(file_path)
print(f"Максимальная длина непрерывной подпоследовательности: {max_length}")