from datetime import datetime
name = "Artem"
location = "Lviv"

print(f"{name} start programming at {datetime.now()}. {location} is the best city!")



def count_vowels(text: str) -> int:
    vowels = "aeiouy"
    text_lower = text.lower()
    return sum(1 for char in text_lower if char in vowels)

# Тестування
if __name__ == "__main__":
    user_input = input("Enter a field: ")
    result = count_vowels(user_input)
    print(f"How many vowels: {result}")
