# Adapter Pattern
# Allows objects with incompatible interfaces to collaborate.

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


