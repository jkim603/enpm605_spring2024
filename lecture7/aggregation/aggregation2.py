class Manager:
    def __init__(self, name):
        self.name = name


class Department:
    def __init__(self, name, manager=None):
        self.name = name
        self.manager = manager  # Aggregation: Department HAS-A Manager


# Creating an instance of Manager
manager1 = Manager("Alice Smith")

# Creating an instance of Department and associating it with the Manager
dept1 = Department("IT", manager1)