class Customer:
    def __init__(self, name, age):
        self._name = name
        self._age = age

class Order:
    def __init__(self, customer, total):
        self._customer = customer
        self._total = total

if __name__ == "__main__":
    alice = Customer("Alice", 30)
    order = Order(alice, 100)
    
    
