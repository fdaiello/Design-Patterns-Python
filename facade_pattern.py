# Facade Pattern
# Provides a simplified interface to a complex subsystem.

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

# Usage
car = CarFacade()
car.start_car()
print("\n")
car.stop_car()


