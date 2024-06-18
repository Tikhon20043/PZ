#

import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

def save_def(people, filename):
    with open(filename, 'wb') as file:
        pickle.dump(people, file)

def load_def(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

# Создаем экземпляры класса Person
person1 = Person("John", 25)
person2 = Person("Alice", 30)
person3 = Person("Bob", 35)

# Сохраняем экземпляры в файл
people = [person1, person2, person3]
save_def(people, "people.pkl")

# Загружаем экземпляры из файла
loaded_people = load_def("people.pkl")

# Выводим загруженные экземпляры
for person in loaded_people:
    print(person)