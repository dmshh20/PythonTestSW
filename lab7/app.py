class Figure:
    FIGURES = ["квадрат", "прямокутник", "трикутник"]

    def __init__(self, type: str, length: int) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in self.FIGURES, "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length

    @property
    def get_figure_type(self):
        return self.type

    @property
    def get_figure_length(self):
        return self.length  # правильне значення (не помилка)

    @property
    def get_angles(self):
        if self.type in ["квадрат", "прямокутник"]:
            return 4
        if self.type == "трикутник":
            return 3
        return None


class Name:
    """Валідація імені та хоббі"""
    ALLOWED = ["Богдан", "Анонім", "Іван"]

    def __init__(self, name: str, hobby: str = "") -> None:
        if name not in self.ALLOWED:
            raise ValueError(f"Дозволені імена: {', '.join(self.ALLOWED)}")
        if not isinstance(hobby, str) or not hobby.strip():
            raise ValueError("Поле хоббі має бути заповнене!")
        self.name = name
        self.hobby = hobby


if __name__ == "__main__":
    # Кілька швидких демонстрацій (неінтерактивні)
    f = Figure("квадрат", 5)
    print("Figure:", f.get_figure_type, f.get_figure_length, "angles:", f.get_angles)
    try:
        bad = Figure("коло", 1)
    except AssertionError as e:
        print("AssertionError (expected):", e)
    try:
        n = Name("Богдан", "програмування")
        print("Name OK:", n.name, "hobby:", n.hobby)
    except ValueError as e:
        print("Name error:", e)
