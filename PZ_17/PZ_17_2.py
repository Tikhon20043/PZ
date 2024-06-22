#Разработать программу с применением пакета tk, взяв в качестве условия одну
#любую задачу из ПЗ №№ 2 – 9.

import tkinter as tk
from random import randint

#Дни недели пронумерованы следующим образом: 0 — воскресенье, 1
#— понедельник, 2 — вторник, . . . , 6 — суббота. Дано целое число K, лежащее в диапазоне 1-365.
#Определить номер дня недели для K-го дня года, если известно, что в этом году 1 января было четвергом.
def calculate_day_of_week():
    K = randint(1, 365)  # Генерирует случайное число между 1 и 365 включительно.
    i = (K + 3) % 7  # Добавляет 3 к случайному числу, и затем находит остаток от деления на 7.
    result_label.config(text=f"Номер дня недели: {i}")

root = tk.Tk()
root.title("Номер дня недели")

button = tk.Button(root, text="Вычислить", command=calculate_day_of_week)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()