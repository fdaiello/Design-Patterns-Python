# Singleton Pattern
# Ensures a class has only one instance and provides a global point of access to that instance.

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


