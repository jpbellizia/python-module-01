#!/usr/bin/env python3

class Plant:
    def __init__(self,
                 plant_name: str,
                 plant_height: float,
                 plant_age: int,
                 plant_growth_rate: float) -> None:

        self.plant_name = plant_name
        self.plant_height = float(plant_height)
        self.plant_age = plant_age
        self.plant_growth_rate = float(plant_growth_rate)

    def show(self) -> None:
        print("Created: "
              f"{self.plant_name}: "
              f"{self.plant_height:.1f}cm, "
              f"{self.plant_age} days old")

    def age(self) -> None:
        self.plant_age += 1

    def grow(self) -> None:
        self.plant_height = self.plant_height + self.plant_growth_rate


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25.0, 30, 0.8),
        Plant("Oak", 200.0, 365, 1.5),
        Plant("Cactus", 5.0, 90, 0.2),
        Plant("Sunflower", 80.0, 45, 0.6),
        Plant("Fern", 15.0, 120, 3.0)
    ]
    print("=== Plant Factory Output ===")
    for plant in plants:
        plant.show()
