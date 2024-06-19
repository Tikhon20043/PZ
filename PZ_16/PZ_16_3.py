#Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
#сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
#Использовать модуль pickle для сериализации и десериализации объектов Python в
#бинарном формате.

import pickle

class Bank:
    def __init__(self, money, rate):
        self.money = money
        self.rate = rate

    def calculate_interest(self):
        return self.money * self.rate / 100

    def withdraw(self, amount):
        if amount > self.money:
            raise ValueError("Insufficient funds")
        self.money -= amount

    def deposit(self, amount):
        self.money += amount

def save_def(bank_instances, filename):
    with open(filename, 'wb') as file:
        pickle.dump(bank_instances, file)

def load_def(filename):
    with open(filename, 'rb') as file:
        bank_instances = pickle.load(file)
    return bank_instances

# Example usage
bank1 = Bank(10000, 5)
bank2 = Bank(20000, 3.5)
bank3 = Bank(15000, 4.2)

bank_instances = [bank1, bank2, bank3]

save_def(bank_instances, 'bank_data.pkl')

loaded_instances = load_def('bank_data.pkl')
for instance in loaded_instances:
    print(f"Money: {instance.money}, Rate: {instance.rate}")