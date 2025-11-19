from abc import ABC, abstractmethod
from random import randint, choice
from typing import Tuple

class Item(ABC):
    def __init__(self, name: str, health: int = 500):
        self.name = name
        self.health = health

    @abstractmethod
    def attack(self, another: "Item") -> str:
        pass

class Sword(Item):
    def __init__(self, name: str, attack_power: int):
        super().__init__(name=name)
        self.__attack_power = attack_power  # приватний
        self._sharp = 0

    def attack(self, another: Item) -> str:
        current_attack = self.__attack_power + self._sharp + randint(0, 10)
        another.health -= current_attack
        return f"{self.name} (Sword) strikes for {current_attack} dmg. {another.name} HP -> {max(0, another.health)}"

    @property
    def get_attack_power(self) -> str:
        return f"Sword {self.name} attack: {self.__attack_power + self._sharp}"

    def sharpening(self) -> None:
        self._sharp += 1

class Axe(Item):
    def __init__(self, name: str, attack_power: int):
        super().__init__(name=name)
        self.__attack_power = attack_power
        self._sharp = 0

    def attack(self, another: Item) -> str:
        current_attack = self.__attack_power + randint(0, 20)
        another.health -= current_attack
        return f"{self.name} (Axe) chops for {current_attack} dmg. {another.name} HP -> {max(0, another.health)}"

    @property
    def get_attack_power(self) -> str:
        return f"Axe {self.name} attack: {self.__attack_power + self._sharp}"

    def sharpening(self) -> None:
        self._sharp += 1

class Bow(Item):
    def __init__(self, name: str, attack_power: int, range_power: int):
        super().__init__(name=name)
        self.__attack_power = attack_power
        self.range_power = range_power  # публічний, змінюваний

    def attack(self, another: Item) -> str:
        current_attack = self.__attack_power + randint(5, 15) + self.range_power
        another.health -= current_attack
        return f"{self.name} (Bow) fires for {current_attack} dmg. {another.name} HP -> {max(0, another.health)}"

    def reload(self) -> None:
        self.range_power += 1

    @property
    def get_attack_power(self) -> str:
        return f"Bow {self.name} attack: {self.__attack_power + self.range_power}"

# Допоміжні функції
def create_random_weapon(name_prefix: str = "Player") -> Item:
    typ = choice(["sword", "axe", "bow"])
    seed = randint(70, 120)
    if typ == "sword":
        return Sword(f"{name_prefix}-Sword", attack_power=seed)
    if typ == "axe":
        return Axe(f"{name_prefix}-Axe", attack_power=seed - 5)
    return Bow(f"{name_prefix}-Bow", attack_power=seed - 10, range_power=randint(1, 5))

def simulate_auto_match(a: Item, b: Item, max_turns: int = 100) -> Tuple[str, Item]:
    turn = 0
    while a.health > 0 and b.health > 0 and turn < max_turns:
        turn += 1
        # a attacks
        _ = a.attack(b)
        # optional random buff
        if randint(0, 4) == 0:
            if hasattr(a, "sharpening"):
                a.sharpening()
            elif hasattr(a, "reload"):
                a.reload()
        if b.health <= 0:
            return ("A_wins", a)
        # b attacks
        _ = b.attack(a)
        if randint(0, 4) == 0:
            if hasattr(b, "sharpening"):
                b.sharpening()
            elif hasattr(b, "reload"):
                b.reload()
        if a.health <= 0:
            return ("B_wins", b)
    # if max_turns reached, compare HP
    winner = a if a.health >= b.health else b
    return ("Draw" if a.health == b.health else "Winner", winner)

def pick_weapon_interactive(player_name: str = "You") -> Item:
    print("Оберіть зброю або натисніть Enter для випадкової:")
    print("1) Sword  2) Axe  3) Bow  (Enter) Random")
    choice_input = input("Ваш вибір (1/2/3/Enter): ").strip()
    if choice_input == "1":
        return Sword(f"{player_name}-Sword", attack_power=100)
    if choice_input == "2":
        return Axe(f"{player_name}-Axe", attack_power=95)
    if choice_input == "3":
        return Bow(f"{player_name}-Bow", attack_power=90, range_power=3)
    return create_random_weapon(player_name)

def run_cli_game():
    print("=== Game: OOP Paradigms Demo ===")
    player = pick_weapon_interactive("Player")
    opponent = create_random_weapon("Enemy")
    print(f"You: {type(player).__name__} '{player.name}' vs Enemy: {type(opponent).__name__} '{opponent.name}'")
    turn = 0
    while player.health > 0 and opponent.health > 0:
        turn += 1
        print(f"\n--- Turn {turn} ---")
        # Player turn
        print(f"Your HP: {player.health} | Enemy HP: {opponent.health}")
        print("Actions: 1) Attack  2) Boost (sharpen/reload)  3) Status  4) Surrender")
        act = input("Choose action: ").strip()
        if act == "1":
            print(player.attack(opponent))
        elif act == "2":
            if hasattr(player, "sharpening"):
                player.sharpening()
                print("You sharpened your weapon.")
            elif hasattr(player, "reload"):
                player.reload()
                print("You reloaded/increased range.")
        elif act == "3":
            print("Status ->", getattr(player, "get_attack_power", "no power info"), "| Enemy power ->", getattr(opponent, "get_attack_power", "no info"))
            continue
        else:
            print("You surrendered.")
            break
        if opponent.health <= 0:
            print("Enemy defeated! You win.")
            break
        # Enemy turn (simple AI)
        if randint(0, 3) == 0:
            # enemy buffs
            if hasattr(opponent, "sharpening"):
                opponent.sharpening()
                print("Enemy sharpens weapon.")
            elif hasattr(opponent, "reload"):
                opponent.reload()
                print("Enemy reloads.")
        else:
            print(opponent.attack(player))
        if player.health <= 0:
            print("You were defeated!")
            break
    print("=== Game over ===")

if __name__ == "__main__":
    # Запуск CLI гри якщо скрипт запущено напряму
    run_cli_game()
