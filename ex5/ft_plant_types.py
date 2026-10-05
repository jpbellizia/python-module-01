#!/usr/bin/env python3

class Plant:
    def __init__(self,
                 name: str,
                 height: float = 0.0,
                 age: int = 0
                 ) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0

        if height < 0:
            print(f"{name}: Error, height can't be negative")
        else:
            self._height = height

        if age < 0:
            print(f"{name}: Error, age can't be negative")
        else:
            self._age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        else:
            self._age = age
            print(f"Age updated: {age} days")

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        else:
            self._height = height
            print(f"Height updated: {height}cm")

    def grow(self, amount: float = 0.8) -> None:
        self._height += amount

    def age(self, days: int = 1) -> None:
        self._age += days

    def show(self) -> None:
        print(f"{self._name}: "
              f"{round(self._height, 1)}cm, "
              f"{self._age} days old")


class Flower(Plant):
    def __init__(
                self,
                name: str,
                height: float = 0.0,
                age: int = 0,
                color: str = "green") -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._bloomed:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self,
                 name: str,
                 height: float = 0.0,
                 age: int = 0,
                 trunk_diameter: float = 0.0) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of "
              f"{round(self._height, 1)}cm long and "
              f"{round(self._trunk_diameter, 1)}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self._trunk_diameter, 1)}cm")


class Vegetable(Plant):
    def __init__(self,
                 name: str,
                 height: float = 0.0,
                 age: int = 0,
                 harvest_season: str = "Unknown"
                 ) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")

    def grow(self, amount: float = 0.8) -> None:
        super().grow(amount)
        self._nutritional_value += 1

    def age(self, days: int = 1) -> None:
        super().age(days)
        self._nutritional_value += 1


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()
