#!/usr/bin/env python3

class Plant:
    def __init__(self, plant_name, plant_height, plant_age, plant_growth_rate):
        self.plant_name = plant_name
        self.plant_height = float(plant_height)
        self.plant_age = plant_age
        self.plant_growth_rate = float(plant_growth_rate)
        self.plant_growth_rate_week = 0

    def show(self):
        print(f"{self.plant_name}: "
              f"{self.plant_height:.1f}cm, "
              f"{self.plant_age} days old")

    def age(self):
        self.plant_age += 1

    def grow(self):
        self.plant_height = self.plant_height + self.plant_growth_rate
        self.plant_growth_rate_week += self.plant_growth_rate


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")

    rose = Plant("Rose", 25, 30, 0.8)
    rose.show()
    day = 1
    while (day <= 7):
        print(f"=== Day {day} ===")
        rose.age()
        rose.grow()
        rose.show()
        day += 1
    print(f"Growth this week: {rose.plant_growth_rate_week}cm")
