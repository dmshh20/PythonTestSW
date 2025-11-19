import sys

def demo_input_number():
    try:
        a = input("Введіть число: ")
    except Exception:
        # Якщо немає stdin (наприклад CI), використовуємо тестове значення
        a = "not_a_number"
    assert a.isdigit(), "Потрібно ввести число!"
    print(f"введене число: {a}")

def demo_figure_validation():
    try:
        # демонстрація assert при створенні об'єкта
        from app import Figure
        print("Creating Figure('трикутник', 3)")
        f = Figure("трикутник", 3)
        print("OK:", f.get_figure_type, f.get_figure_length)
        print("Creating invalid Figure('трапеція', 2)")
        Figure("трапеція", 2)
    except AssertionError as e:
        print("Caught AssertionError (expected):", e)

if __name__ == "__main__":
    demo_input_number()
    demo_figure_validation()
