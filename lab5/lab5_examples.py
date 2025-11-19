import keyword
from random import randint
from typing import Optional

class MyName:
    """Опис класу / Документація"""
    total_names = 0  # Class Variable

    def __init__(self, name: Optional[str] = None) -> None:
        """Ініціалізація класу"""
        if name is None:
            name = self.anonymous_user().name
        # Переконаємось, що ім'я — рядок
        if not isinstance(name, str):
            raise ValueError("Ім'я має бути рядком!")
        # Очищаємо пробіли та робимо першу літеру великою
        name = name.strip().capitalize()
        # Перевірка: лише букви
        if not name.isalpha():
            raise ValueError("Ім'я може містити лише літери!")
        self.name = name  # Instance variable
        MyName.total_names += 1
        self.my_id = MyName.total_names

    @property
    def whoami(self) -> str:
        """Class property: повертаємо імя"""
        return f"My name is {self.name}"

    @property
    def my_email(self) -> str:
        """Class property: повертаємо емейл з дефолтним доменом"""
        return self.create_email()

    def create_email(self, domain: str = "itcollege.lviv.ua") -> str:
        """Instance method: можна вказати домен"""
        return f"{self.name}@{domain}"

    @classmethod
    def anonymous_user(cls):
        """Class method"""
        return cls("Anonymous")

    @staticmethod
    def say_hello(message: str = "Hello to everyone!") -> str:
        """Static method"""
        return f"You say: {message}"

    def name_length(self) -> int:
        """Повертає кількість букв у імені"""
        return len(self.name)

    @property
    def full_name(self) -> str:
        """Повертає формат: User #<id>: <name> (<email>)"""
        return f"User #{self.my_id}: {self.name} ({self.my_email})"

    def save_to_file(self, filename: str = "users.txt") -> None:
        """Додає повний рядок у файл (append)"""
        with open(filename, "a", encoding="utf-8") as f:
            f.write(self.full_name + "\n")


if __name__ == "__main__":
    print("Розпочинаємо створювати об'єкти!")

    # Додано власне ім'я "Ivan" як приклад
    names = ("Bohdan", "Marta", None, "Ivan", "Bohdan")  # дублікати показують різницю при використанні dict
    print("Кількість елементів у names (оригінал):", len(names))

    # Створюємо об'єкти у словнику — ключі як в початковому прикладі
    all_names = {name: MyName(name) for name in names}
    print("Кількість створених об'єктів (к-ть ключів у словнику):", len(all_names))
    print("Загальна кількість інстансів MyName (total_names):", MyName.total_names)
    print()

    for name_key, me in all_names.items():
        print(f"{'*>*'*10}")
        print("This is object:", me)
        print("This is object attribute:", me.name, "/", me.my_id)
        print("This is whoami:", me.whoami, "/ email:", me.my_email)
        print("create_email with custom domain:", me.create_email("example.com"))
        print("Static say_hello default:", MyName.say_hello())
        print("Static say_hello custom:", MyName.say_hello("Привіт з лабораторної!"))
        print("Class variable total_names (from class / from object):", MyName.total_names, "/", me.total_names)
        print("Name length:", me.name_length())
        print("Full name:", me.full_name)
        # Збережемо кожного користувача у файл
        me.save_to_file("users.txt")
        print(f"{'<*>*'*10}\n")

    print(f"We are done. We created total {MyName.total_names} names!")
    # Показати ключову відмінність: len(names) vs len(all_names)
    print("Пояснення: len(names) may differ from created objects because keys in dict are unique; None -> 'Anonymous'")
