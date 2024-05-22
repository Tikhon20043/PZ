#Дана строка, состоящая из русских слов и разделенных пробелами
#(одним или несколькими). Найти количество слов, которые начинаются
#и заканчиваются одной и той же буквой.


def count_words(string): # Разбиваем строку на слова

    words = string.split()  # Инициализируем счетчик
    count = 0   # Перебираем каждое слово

    for word in words: # Проверяем, начинается ли слово и заканчивается ли оно одной и той же буквой
        if word[0] == word[-1]:
            count += 1  # Возвращаем количество слов, удовлетворяющих условию
    return count

string = "кот доход шала лёд лампа казак телефон"
count = count_words(string)
print(f"Количество слов, которые начинаются и заканчиваются одной и той же буквой: {count}")