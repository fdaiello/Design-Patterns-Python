# Strategy Pattern
# Defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

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


