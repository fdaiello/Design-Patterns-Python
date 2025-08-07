# Builder Pattern
# Separates the construction of a complex object from its representation, allowing the same construction process to create different representations.

from abc import ABC, abstractmethod

class Burger:
    def __init__(self):
        self.buns = None
        self.patty = None
        self.cheese = None
        self.toppings = []

    def __str__(self):
        return f"Burger with {self.buns} buns, {self.patty} patty, {self.cheese if self.cheese else 'no'} cheese, and {', '.join(self.toppings) if self.toppings else 'no toppings'}."

class BurgerBuilder(ABC):
    @abstractmethod
    def build_buns(self):
        pass

    @abstractmethod
    def build_patty(self):
        pass

    @abstractmethod
    def build_cheese(self):
        pass

    @abstractmethod
    def build_toppings(self):
        pass

    @abstractmethod
    def get_burger(self) -> Burger:
        pass

class VeggieBurgerBuilder(BurgerBuilder):
    def __init__(self):
        self.burger = Burger()

    def build_buns(self):
        self.burger.buns = "Sesame Seed"

    def build_patty(self):
        self.burger.patty = "Veggie"

    def build_cheese(self):
        self.burger.cheese = "Cheddar"

    def build_toppings(self):
        self.burger.toppings.extend(["Lettuce", "Tomato", "Onion"])

    def get_burger(self) -> Burger:
        return self.burger

class ChickenBurgerBuilder(BurgerBuilder):
    def __init__(self):
        self.burger = Burger()

    def build_buns(self):
        self.burger.buns = "Brioche"

    def build_patty(self):
        self.burger.patty = "Chicken"

    def build_cheese(self):
        self.burger.cheese = "Swiss"

    def build_toppings(self):
        self.burger.toppings.extend(["Pickles", "Mayonnaise"])

    def get_burger(self) -> Burger:
        return self.burger

class Director:
    def __init__(self, builder: BurgerBuilder):
        self._builder = builder

    def construct_burger(self):
        self._builder.build_buns()
        self._builder.build_patty()
        self._builder.build_cheese()
        self._builder.build_toppings()

# Usage
veggie_builder = VeggieBurgerBuilder()
director = Director(veggie_builder)
director.construct_burger()
veggie_burger = veggie_builder.get_burger()
print(f"Veggie Burger: {veggie_burger}")

chicken_builder = ChickenBurgerBuilder()
director = Director(chicken_builder) # Director can work with different builders
director.construct_burger()
chicken_burger = chicken_builder.get_burger()
print(f"Chicken Burger: {chicken_burger}")


