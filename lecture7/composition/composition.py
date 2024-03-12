class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower


class Car:
    def __init__(self, model, engine_horsepower):
        self.model = model
        self.engine = Engine(engine_horsepower)  # Engine is a part of Car


# Creating objects and establishing composition
car = Car("Toyota Camry", 268)