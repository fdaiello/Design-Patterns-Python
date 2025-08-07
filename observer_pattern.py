# Observer Pattern
# Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

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
        print(f"Observer {self.name}: Subject's state is now {state}")

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

print("\nDetaching Observer 2")
subject.detach(observer2)

print("\nSetting subject state to 20")
subject.state = 20


