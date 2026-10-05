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


if __name__ == "__main__":
    rose = Plant("Rose", 15.0, 10)
    rose.show()
    print("Plant created: ", end="")
    rose.show()
    print()

    rose.set_height(25)
    rose.set_age(30)
    print()

    rose.set_height(-5)
    rose.set_age(-10)
    print()

    print("Current state: ", end="")
    rose.show()
