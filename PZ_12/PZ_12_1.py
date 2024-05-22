#Даны средние значения температур за каждый месяц в году. Найти минимальное
#и максимальное значения температур за год.


# Создание списка средних значений температур за каждый месяц
import random

temperature_values = []

for _ in range(12):
    random_number = random.randint(-20,45)
    temperature_values.append(random_number)

print(temperature_values)

# Нахождение минимальной и максимальной температуры за год с использованием списковых включений
min_temperature = min(temperature_values)
max_temperature = max(temperature_values)

print(f"Минимальная температура за год: {min_temperature}")
print(f"Максимальная температура за год: {max_temperature}")