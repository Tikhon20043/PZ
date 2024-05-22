#Составить генератор (yield), который преобразует все буквенные символы в заглавные.

def to_upper(text):
    for char in text:
        if char.isalpha():
            yield char.upper()

text = "hello world"
upper_generator = to_upper(text)

for char in upper_generator:
    print(char, end='')