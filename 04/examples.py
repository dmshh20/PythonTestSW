# Демонстраційний файл прикладів для звіту

import keyword
import sys
from random import randint

# Типи даних та приклади змінних
a = "змінна з текстом"
b = 1  # числова Змінна
b1 = 1.1
c = ["a", 1, 1.25, "Слово", a]  # List
d = {"a": "Слово", "b": 1, a: b}  # Dict
e = ("a", a)  # Tuple
# множина: помітка — не можна додавати суміш str+int без перетворення
f = {"ss", str(b) + a}  # Set (перетворення на str щоб уникнути помилки)

print("=== Типи даних ===")
print("a:", a)
print("b:", b, "b1:", b1)
print("c(list):", c)
print("d(dict):", d)
print("e(tuple):", e)
print("f(set):", f)
print()

# Вбудовані константи і ключові слова
print("=== Константи і ключові слова ===")
print("Константи приклад:", True, None, False)
print("Ключові слова Python (частина):", keyword.kwlist[:10], "...")  # показати перші 10
print()

# Вбудовані функції (пара прикладів)
print("=== Вбудовані функції ===")
print("abs(-12.5):", abs(-12.5))
print("round(3.14159, 2):", round(3.14159, 2))
print("len(c):", len(c))
print()

# Цикли
print("=== Цикли ===")
letters = ["a", "b", "c"]
for i in range(len(letters)):
    print(f"На позиції {i} знаходиться буква {letters[i]}")
else:
    print("Цикл for завершився, блок else виконався")
print()

print("Приклад enumerate:")
for idx, val in enumerate(letters, start=1):
    print(idx, val)
print()

print("Приклад while:")
n = 3
while n > 0:
    print("n=", n)
    n -= 1
else:
    print("while завершився")
print()

# Розгалуження
print("=== Розгалуження ===")
A = randint(0, 2)
if A == 0:
    print("A is zero")
elif A == 1:
    print("A is one")
else:
    print(f"A is {A}")
# Теренарний приклад
print("Теренарний приклад:", f"Значить A={A}" if A else f"Але може бути що А={A}")
print()

# try -> except -> finally
print("=== try / except / finally ===")
A = 0
try:
    print("Спроба ділення 10/A:")
    print(10 / A)
except Exception as e:
    print("Виловлена помилка:", type(e).__name__, e)
finally:
    print("Блок finally виконався")
print()

# Контекст-менеджер with (безпечне читання файлу)
print("=== with (читання README.md 5 перших рядків як приклад) ===")
try:
    with open("readme.md", "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i >= 5:
                break
            print(f"{i+1}) {line.rstrip()}")
except FileNotFoundError:
    print("Файл readme.md не знайдено в поточній директорії.")
print()

# Lambda приклади
print("=== Lambda і функції ===")
def a_b_func(a_, b_):
    return a_, b_

this_is_lambda = lambda first, age: f'Цей код написав: {first}, Мені {age:d} років'
print("Функція a_b_func:", a_b_func("Ivan", 30))
print("Лямбда об'єкт:", this_is_lambda)
print("Виклик лямбда:", this_is_lambda('Богдан', 100000))
print("Розпакування через *:", this_is_lambda(*a_b_func("Anna", 25)))
print()

# Порада: як попросити AI (приклад prompt)
print("=== Підказка для AI ===")
print('''Prompt для ChatGPT:
I am learning Python using Jupyter Notebook. Please provide a concise explanation (4-6 short paragraphs) about Python basics (types, control flow, functions, modules) and include 3 small runnable code examples suitable for a notebook.
''')

# Кінець файлу
if __name__ == "__main__":
    print("=== Кінець прикладів ===")
