class Bird:
    def fly(self): print("Bird is flying")


class Airplane:
    def fly(self): print("Airplane is flying")


class Fish:
    def swim(self): print("Fish is swimming")

def move_in_air(entity): entity.fly()

bird = Bird()
airplane = Airplane()
fish = Fish()

move_in_air(bird)  # Bird is flying
move_in_air(airplane)  # Airplane is flying
# move_in_air(fish)  # AttributeError