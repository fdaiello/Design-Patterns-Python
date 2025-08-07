# Decorator Pattern
# Attaches new behaviors to objects by placing them inside special wrapper objects that contain the behaviors.

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


