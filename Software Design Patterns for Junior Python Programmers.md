# Software Design Patterns for Junior Python Programmers

This repository contains a collection of common software design patterns implemented in Python, specifically tailored for junior programmers. Each pattern is presented with a simple, workable code example and a deeper explanation of its purpose, structure, and application.

## What are Design Patterns?

Design patterns are generalized, reusable solutions to common problems that arise during software design. They are not finished designs that can be directly converted into code. Instead, they are templates or blueprints that describe how to solve a particular problem in various contexts. Using design patterns helps in creating more robust, flexible, and maintainable software.

## Why Learn Design Patterns?

*   **Improved Code Structure:** Patterns provide a proven way to structure your code, making it more organized and easier to understand.
*   **Reusability:** They promote code reuse, reducing development time and potential errors.
*   **Maintainability:** Well-designed patterns make it easier to modify and extend your codebase in the future.
*   **Common Vocabulary:** Patterns provide a shared language for developers, facilitating communication and collaboration within a team.
*   **Problem Solving:** They offer elegant solutions to recurring design problems, saving you from reinventing the wheel.

## Design Patterns Included

This tutorial covers a selection of Creational, Structural, and Behavioral design patterns.




### Singleton Pattern

**Purpose:** The Singleton pattern ensures that a class has only one instance and provides a global point of access to that instance. This is useful when exactly one object is needed to coordinate actions across the system.

**Structure:**

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            # Put any initialization here that should only happen once
            cls._instance.value = 0
        return cls._instance

    def increment(self):
        self.value += 1

# Usage
s1 = Singleton()
s1.increment()
print(f"Singleton instance 1 value: {s1.value}")

s2 = Singleton()
s2.increment()
print(f"Singleton instance 2 value: {s2.value}")

print(f"Are s1 and s2 the same instance? {s1 is s2}")
```

**Explanation:**

In Python, the `__new__` method is called before `__init__` when creating an instance of a class. By overriding `__new__`, we can control the instance creation process. In the Singleton pattern, we check if an instance (`_instance`) already exists. If not, we create one and store it. Subsequent calls to create an instance of `Singleton` will return the already existing instance. This guarantees that `s1` and `s2` in the example refer to the exact same object, as confirmed by `s1 is s2` being `True`.

**When to Use:**

*   When there must be exactly one instance of a class, and it must be accessible to clients from a well-known access point.
*   Examples include a logging class, configuration manager, or a database connection pool.

**Considerations:**

*   Can make testing more difficult due to global state.
*   Can hide dependencies, making code less explicit.
*   In Python, modules are naturally singletons (they are loaded only once), so for simple cases, a module-level instance might suffice.




### Factory Method Pattern

**Purpose:** The Factory Method pattern provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created. It promotes loose coupling by decoupling the client code from the concrete classes it instantiates.

**Structure:**

```python
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
        result = f"Creator: The same creator\\'s code has just worked with {product.operation()}"
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
    print(f"Client: I\\'m not aware of the creator\\'s class, but it still works.\\n{creator.some_operation()}")

print("App: Launched with the ConcreteCreatorA.")
client_code(ConcreteCreatorA())

print("\\nApp: Launched with the ConcreteCreatorB.")
client_code(ConcreteCreatorB())
```

**Explanation:**

The Factory Method pattern defines a `factory_method` in a `Creator` class (which can be an abstract class or an interface). Subclasses of `Creator` then implement this `factory_method` to return instances of different `Product` types. The client code interacts with the `Creator` interface, remaining unaware of the specific `ConcreteProduct` being created. This allows for easy extension: to add a new product type, you only need to create a new `ConcreteProduct` and a new `ConcreteCreator` without modifying existing client code.

**When to Use:**

*   When a class can't anticipate the class of objects it must create.
*   When a class wants its subclasses to specify the objects it creates.
*   When classes delegate responsibility to one of several helper subclasses, and you want to localize the knowledge of which helper subclass is the delegate.

**Considerations:**

*   Can lead to a proliferation of subclasses if not managed carefully.
*   The `factory_method` can be parameterized to create different types of products based on input.




### Builder Pattern

**Purpose:** The Builder pattern separates the construction of a complex object from its representation, allowing the same construction process to create different representations. It's particularly useful when an object has many optional parameters or when its construction involves multiple steps.

**Structure:**

```python
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
```

**Explanation:**

The Builder pattern involves a `Director` and a `Builder` interface. The `Director` knows the sequence of steps to construct a complex object, but it doesn't know the specifics of how each step is performed. The `Builder` interface defines the steps for building the object, and concrete builders (e.g., `VeggieBurgerBuilder`, `ChickenBurgerBuilder`) implement these steps to create different representations of the object. This allows you to reuse the construction logic (in the `Director`) with different builders to produce varied results.

**When to Use:**

*   When the creation of a complex object should be independent of its parts and how they are assembled.
*   When the construction process allows for different representations of the object being constructed.
*   When an object has many optional parameters, and using a constructor with many arguments would be cumbersome.

**Considerations:**

*   Can increase the number of classes in your project.
*   Provides fine-grained control over the construction process.




### Adapter Pattern

**Purpose:** The Adapter pattern allows objects with incompatible interfaces to collaborate. It acts as a bridge between two incompatible interfaces, converting the interface of one class into another interface clients expect.

**Structure:**

```python
class EuropeanSocket:
    def plug_in(self):
        return "220V European power."

class AmericanDevice:
    def __init__(self):
        self.voltage = "110V American power."

    def operate(self):
        return f"Operating with {self.voltage}"

class EuropeanToAmericanAdapter:
    def __init__(self, european_socket: EuropeanSocket):
        self._european_socket = european_socket

    def operate(self):
        # Adapt the European socket to work with an American device
        power = self._european_socket.plug_in()
        return f"Adapter converting {power} to 110V American power for device operation."

# Usage
european_socket = EuropeanSocket()
american_device = AmericanDevice()

# Direct operation of American device
print(american_device.operate())

# Using the adapter to power an American device with a European socket
adapter = EuropeanToAmericanAdapter(european_socket)
print(adapter.operate())
```

**Explanation:**

In this example, we have a `EuropeanSocket` that provides 220V power and an `AmericanDevice` that expects 110V power. These two interfaces are incompatible. The `EuropeanToAmericanAdapter` acts as an adapter, taking a `EuropeanSocket` object and providing an `operate` method that makes it compatible with the `AmericanDevice`'s expectation. It essentially translates the `plug_in` method of the `EuropeanSocket` into something the `AmericanDevice` can use, demonstrating how the adapter bridges the gap between incompatible interfaces.

**When to Use:**

*   When you want to use an existing class, but its interface doesn't match the one you need.
*   When you want to create a reusable class that cooperates with unrelated or unforeseen classes, which don't necessarily have compatible interfaces.
*   When you need to integrate a new component into an existing system without changing the existing system's code.

**Considerations:**

*   Can add an extra layer of complexity.
*   Useful for integrating legacy code with new systems.




### Decorator Pattern

**Purpose:** The Decorator pattern attaches new behaviors or responsibilities to an object dynamically. It provides a flexible alternative to subclassing for extending functionality. It wraps an object in a decorator object, which adds new behavior while maintaining the original object's interface.

**Structure:**

```python
def greet(func):
    def wrapper(*args, **kwargs):
        print("Hello!")
        return func(*args, **kwargs)
    return wrapper

def farewell(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Goodbye!")
        return result
    return wrapper

@greet
@farewell
def say_name(name):
    print(f"My name is {name}.")

# Usage
say_name("Alice")

# Another example with a return value
@greet
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(f"Result of addition: {result}")
```

**Explanation:**

In Python, decorators are a powerful and concise way to implement the Decorator pattern. A decorator is a function that takes another function as an argument and extends or changes the behavior of the latter function without explicitly modifying it. The `@greet` and `@farewell` syntax is syntactic sugar for `say_name = greet(farewell(say_name))`. When `say_name("Alice")` is called, the `greet` decorator's `wrapper` is executed first, printing "Hello!". Then, the `farewell` decorator's `wrapper` is executed, which in turn calls the original `say_name` function. After `say_name` finishes, `farewell` prints "Goodbye!". This demonstrates how decorators can add functionality before and after the original function's execution.

**When to Use:**

*   When you need to add responsibilities to individual objects dynamically and transparently, without affecting other objects.
*   When you want to add functionality to an object without subclassing, which can lead to a large number of subclasses for different combinations of behaviors.
*   When an object's responsibilities can be withdrawn.

**Considerations:**

*   Can make debugging more challenging as the call stack becomes deeper.
*   Order of decorators matters.




### Facade Pattern

**Purpose:** The Facade pattern provides a simplified interface to a complex subsystem. It hides the complexities of the system and provides a single, unified interface to the client. This makes the subsystem easier to use and reduces dependencies between the client and the subsystem.

**Structure:**

```python
class Engine:
    def start(self):
        return "Engine started."

    def stop(self):
        return "Engine stopped."

class Lights:
    def turn_on(self):
        return "Lights on."

    def turn_off(self):
        return "Lights off."

class AirConditioner:
    def turn_on(self):
        return "AC on."

    def turn_off(self):
        return "AC off."

class CarFacade:
    def __init__(self):
        self.engine = Engine()
        self.lights = Lights()
        self.ac = AirConditioner()

    def start_car(self):
        print("Starting car...")
        print(self.engine.start())
        print(self.lights.turn_on())
        print(self.ac.turn_on())
        print("Car started!")

    def stop_car(self):
        print("Stopping car...")
        print(self.ac.turn_off())
        print(self.lights.turn_off())
        print(self.engine.stop())
        print("Car stopped!")
```

**Explanation:**

In this example, starting or stopping a car involves interacting with multiple subsystems: the engine, lights, and air conditioner. Without the Facade, a client would need to know about each of these components and their respective methods. The `CarFacade` class provides a simplified interface (`start_car` and `stop_car`) that encapsulates these complex interactions. The client only needs to interact with the `CarFacade`, making the system easier to use and reducing the client's dependency on the internal workings of the car's subsystems.

**When to Use:**

*   When you want to provide a simple interface to a complex subsystem.
*   When you want to decouple a client from a subsystem.
*   When you want to layer your subsystems.

**Considerations:**

*   Can become a 


god object" if it becomes too large and tries to encapsulate too many unrelated subsystems.




### Observer Pattern

**Purpose:** The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents (observers) are notified and updated automatically. This pattern is often used to implement distributed event handling systems.

**Structure:**

```python
class Subject:
    def __init__(self):
        self._observers = []
        self._state = None

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def _notify(self):
        for observer in self._observers:
            observer.update(self._state)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state):
        self._state = new_state
        self._notify()

class Observer:
    def __init__(self, name):
        self.name = name

    def update(self, state):
        print(f"Observer {self.name}: Subject\\\'s state is now {state}")

# Usage
subject = Subject()

observer1 = Observer("Observer 1")
observer2 = Observer("Observer 2")
observer3 = Observer("Observer 3")

subject.attach(observer1)
subject.attach(observer2)
subject.attach(observer3)

print("Setting subject state to 10")
subject.state = 10

print("\\nDetaching Observer 2")
subject.detach(observer2)

print("\\nSetting subject state to 20")
subject.state = 20
```

**Explanation:**

The Observer pattern consists of a `Subject` (also known as Publisher) and `Observer`s (also known as Subscribers). The `Subject` maintains a list of its `Observer`s and notifies them of any state changes, usually by calling an `update` method on each observer. `Observer`s register themselves with the `Subject` to receive notifications. In the example, when the `subject.state` is changed, all attached observers are automatically updated, demonstrating the one-to-many dependency.

**When to Use:**

*   When a change to one object requires changing others, and you don't know how many objects need to be changed.
*   When an object should be able to notify other objects without making assumptions about who these other objects are.
*   Commonly used in GUI frameworks (e.g., button clicks), event handling systems, and reactive programming.

**Considerations:**

*   Can lead to unexpected updates if not managed carefully, especially in complex systems.
*   The order of notification is not guaranteed unless explicitly implemented.




### Iterator Pattern

**Purpose:** The Iterator pattern provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation. It separates the traversal logic from the collection itself.

**Structure:**

```python
class MyCollection:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def __iter__(self):
        return MyIterator(self._items)

class MyIterator:
    def __init__(self, items):
        self._items = items
        self._index = 0

    def __next__(self):
        if self._index < len(self._items):
            item = self._items[self._index]
            self._index += 1
            return item
        raise StopIteration

# Usage
collection = MyCollection()
collection.add_item("Apple")
collection.add_item("Banana")
collection.add_item("Cherry")

print("Iterating through the collection:")
for fruit in collection:
    print(fruit)

print("\\nUsing next() directly:")
my_iterator = iter(collection)
print(next(my_iterator))
print(next(my_iterator))
```

**Explanation:**

The Iterator pattern allows you to traverse elements of a collection (like a list or a custom data structure) without exposing its internal structure. In Python, this is naturally supported by the `__iter__` and `__next__` methods. The `MyCollection` class implements `__iter__` to return an instance of `MyIterator`. The `MyIterator` class implements `__next__` to return the next item in the collection and raises `StopIteration` when there are no more items. This allows the `for...in` loop to work seamlessly with `MyCollection`.

**When to Use:**

*   When you need to access the contents of an aggregate object without exposing its internal representation.
*   When you need to support multiple traversals of the same aggregate object.
*   When you need to provide a uniform interface for traversing different aggregate structures.

**Considerations:**

*   Python's built-in iteration protocol (using `__iter__` and `__next__`) makes implementing this pattern very straightforward.
*   Can be combined with other patterns, such as the Composite pattern, to traverse complex tree-like structures.




### Strategy Pattern

**Purpose:** The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it. This allows you to select an algorithm at runtime.

**Structure:**

```python
from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using Credit Card.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using PayPal.")

class BankTransferPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using Bank Transfer.")

# Context
class ShoppingCart:
    def __init__(self, payment_strategy: PaymentStrategy):
        self._payment_strategy = payment_strategy

    def set_payment_strategy(self, payment_strategy: PaymentStrategy):
        self._payment_strategy = payment_strategy

    def checkout(self, amount):
        self._payment_strategy.pay(amount)

# Usage
# Pay with Credit Card
cart = ShoppingCart(CreditCardPayment())
cart.checkout(100)

# Change strategy to PayPal
cart.set_payment_strategy(PayPalPayment())
cart.checkout(50)

# Change strategy to Bank Transfer
cart.set_payment_strategy(BankTransferPayment())
cart.checkout(200)
```

**Explanation:**

The Strategy pattern involves a `Context` (e.g., `ShoppingCart`) that holds a reference to a `Strategy` object (e.g., `PaymentStrategy`). The `Context` delegates the execution of an algorithm to its linked `Strategy` object. Different concrete `Strategy` classes (e.g., `CreditCardPayment`, `PayPalPayment`, `BankTransferPayment`) implement the same interface, allowing them to be interchangeable. This means the client (the `ShoppingCart` in this case) can change its behavior at runtime by simply switching the `PaymentStrategy` object it uses, without modifying its own code.

**When to Use:**

*   When you have many related classes that differ only in their behavior.
*   When you need different variants of an algorithm.
*   When an algorithm uses data that clients shouldn't know about.
*   When you want to avoid hardcoding algorithm behaviors into a class.

**Considerations:**

*   Can increase the number of objects if you have many strategies.
*   The client must be aware of the different strategies to choose the appropriate one.



