# Factory Method Pattern
# Provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

from abc import ABC, abstractmethod

# Product interface
class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

# Concrete Products
class ConcreteProductA(Product):
    def operation(self):
        return "ConcreteProductA operation"

class ConcreteProductB(Product):
    def operation(self):
        return "ConcreteProductB operation"

# Creator interface
class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self):
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result

# Concrete Creators
class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()

# Usage
def client_code(creator: Creator):
    print(f"Client: I'm not aware of the creator's class, but it still works.\n{creator.some_operation()}")

print("App: Launched with the ConcreteCreatorA.")
client_code(ConcreteCreatorA())

print("\nApp: Launched with the ConcreteCreatorB.")
client_code(ConcreteCreatorB())


