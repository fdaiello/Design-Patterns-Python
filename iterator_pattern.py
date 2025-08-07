# Iterator Pattern
# Provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

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

print("\nUsing next() directly:")
my_iterator = iter(collection)
print(next(my_iterator))
print(next(my_iterator))


