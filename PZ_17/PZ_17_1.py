import tkinter as tk
from tkinter import ttk

def register():
    # Получение данных из полей ввода
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    age_var = age_var.get()
    languages = []
    if russian_var.get():
        languages.append("Русский")
    if english_var.get():
        languages.append("Английский")
    if french_var.get():
        languages.append("Французский")
    if german_var.get():
        languages.append("Немецкий")
    data_format = data_format_var.get()
    favorite_authors = favorite_authors_entry.get()

    # Выводим введенные данные в консоль
    print("Регистрационное имя:", username)
    print("Пароль:", password)
    print("Подтверждение пароля:", confirm_password)
    print("Возраст:", age_var)
    print("Языки:", ", ".join(languages))
    print("Формат данных:", data_format)
    print("Любимые авторы:", favorite_authors)

    # Сбрасываем значения полей ввода
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    confirm_password_entry.delete(0, tk.END)
    favorite_authors_entry.delete(0, tk.END)

    # Закрываем окно
    root.destroy()

root = tk.Tk()
root.title("Регистрация в электронной библиотеке")

# Создание виджетов
username_label = tk.Label(root, text="Введите регистрационное имя:")
username_entry = tk.Entry(root)

password_label = tk.Label(root, text="Введите пароль:")
password_entry = tk.Entry(root, show="*")

confirm_password_label = tk.Label(root, text="Подтвердите пароль:")
confirm_password_entry = tk.Entry(root, show="*")

age_label = tk.Label(root, text="Ваш возраст:")
age_var = tk.StringVar()
age_under_20 = tk.Radiobutton(root, text="До 20", variable=age_var, value="До 20")
age_20_30 = tk.Radiobutton(root, text="20-30", variable=age_var, value="20-30")
age_30_50 = tk.Radiobutton(root, text="30-50", variable=age_var, value="30-50")
age_over_50 = tk.Radiobutton(root, text="От 50", variable=age_var, value="От 50")

languages_label = tk.Label(root, text="На каких языках читаете:")
russian_var = tk.BooleanVar()
russian_checkbox = tk.Checkbutton(root, text="Русский", variable=russian_var)
english_var = tk.BooleanVar()
english_checkbox = tk.Checkbutton(root, text="Английский", variable=english_var)
french_var = tk.BooleanVar()
french_checkbox = tk.Checkbutton(root, text="Французский", variable=french_var)
german_var = tk.BooleanVar()
german_checkbox = tk.Checkbutton(root, text="Немецкий", variable=german_var)

data_format_label = tk.Label(root, text="Какой формат данных является для вас предпочтительным?")
data_format_var = tk.StringVar()
data_format_html = tk.Radiobutton(root, text="HTML", variable=data_format_var, value="HTML")
data_format_text = tk.Radiobutton(root, text="Обычный текст", variable=data_format_var, value="Обычный текст")

favorite_authors_label = tk.Label(root, text="Ваши любимые авторы:")
favorite_authors_entry = tk.Entry(root)

register_button = tk.Button(root, text="OK", command=register)
cancel_button = tk.Button(root, text="Отменить", command=root.destroy)

# Размещение виджетов в окне
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry.grid(row=0, column=1, padx=10, pady=10)

password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry.grid(row=1, column=1, padx=10, pady=10)

confirm_password_label.grid(row=2, column=0, padx=10, pady=10)
confirm_password_entry.grid(row=2, column=1, padx=10, pady=10)

age_label.grid(row=3, column=0, padx=10, pady=10)
age_under_20.grid(row=3, column=1, padx=10, pady=5, sticky="w")
age_20_30.grid(row=4, column=1, padx=10, pady=5, sticky="w")
age_30_50.grid(row=5, column=1, padx=10, pady=5, sticky="w")
age_over_50.grid(row=6, column=1, padx=10, pady=5, sticky="w")

languages_label.grid(row=7, column=0, padx=10, pady=10)
russian_checkbox.grid(row=7, column=1, padx=10, pady=5, sticky="w")
english_checkbox.grid(row=8, column=1, padx=10, pady=5, sticky="w")
french_checkbox.grid(row=9, column=1, padx=10, pady=5, sticky="w")
german_checkbox.grid(row=10, column=1, padx=10, pady=5, sticky="w")

data_format_label.grid(row=11, column=0, padx=10, pady=10)
data_format_html.grid(row=11, column=1, padx=10, pady=5, sticky="w")
data_format_text.grid(row=12, column=1, padx=10, pady=5, sticky="w")

favorite_authors_label.grid(row=13, column=0, padx=10, pady=10)
favorite_authors_entry.grid(row=13, column=1, padx=10, pady=10)

register_button.grid(row=14, column=0, padx=10, pady=10)
cancel_button.grid(row=14, column=1, padx=10, pady=10)

root.mainloop()