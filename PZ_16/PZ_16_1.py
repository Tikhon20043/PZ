#Создайте класс «Банк», который имеет атрибуты суммы денег и процентной ставки.
#Добавьте методы для вычисления процентных начислений и снятия денег.

class Bank:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate

    def calculate_interest(self, time_period):
        """
        Вычисляет начисленные проценты за указанный период времени.

        Args:
            time_period (int): Период времени в годах.

        Returns:
            float: Начисленные проценты.
        """
        interest = self.balance * (self.interest_rate / 100) * time_period
        return interest

    def withdraw(self, amount):
        """
        Снимает указанную сумму денег с баланса.

        Args:
            amount (float): Сумма для снятия.

        Raises:
            ValueError: Если сумма для снятия превышает текущий баланс.
        """
        if amount > self.balance:
            raise ValueError("Недостаточно средств на балансе.")
        self.balance -= amount


# Пример использования
my_bank = Bank(10000, 5.0)
print(f"Текущий баланс: {my_bank.balance:.2f} руб.")

interest_earned = my_bank.calculate_interest(3)
print(f"Начисленные проценты за 3 года: {interest_earned:.2f} руб.")

try:
    my_bank.withdraw(3000)
    print(f"Новый баланс: {my_bank.balance:.2f} руб.")
except ValueError as e:
    print(e)