# Define the base class Animal
class Animal:
    zoo_name = "Zoo"

    def __init__(self, name_, hunger_=0):
        self.name_ = name_
        self.hunger_ = hunger_

    def is_hungry(self):
        return self.hunger_ > 0

    def feed(self):
        if self.hunger_ > 0:
            self.hunger_ -= 1

    def get_name(self):
        return self.name_

    def talk(self):
        pass


# Define derived classes
class Dog(Animal):
    def talk(self):
        print(f"{self.name_} says: Woof!")

    def fetch_stick(self):
        print(f"{self.name_} is fetching a stick.")


class Cat(Animal):
    def talk(self):
        print(f"{self.name_} says: Meow!")

    def chase_laser(self):
        print(f"{self.name_} is chasing a laser.")


class Skunk(Animal):
    def talk(self):
        print(f"{self.name_} says: Ssss!")

    def stink(self):
        print(f"{self.name_} is stinking.")


class Unicorn(Animal):
    def talk(self):
        print(f"{self.name_} says: Neigh!")

    def sing(self):
        print(f"{self.name_} is singing.")


class Dragon(Animal):
    def talk(self):
        print(f"{self.name_} says: Roar!")

    def breath_fire(self):
        print(f"{self.name_} is breathing fire.")


# Main function
def main():
    zoo_lst = [
        Dog("Brownie", 10),
        Cat("Zelda", 3),
        Skunk("Stinky", 0),
        Unicorn("Keith", 7),
        Dragon("Lizzy", 1450),
        Dog("Doggo", 80),
        Cat("Kitty", 80),
        Skunk("Stinky Jr.", 80),
        Unicorn("Clair", 80),
        Dragon("McFly", 80)
    ]

    for animal in zoo_lst:
        if animal.is_hungry():
            print(f"{animal.__class__.__name__} {animal.get_name()} is hungry.")
            while animal.is_hungry():
                animal.feed()

        animal.talk()

        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

    print(f"Zoo name: {Animal.zoo_name}")


if __name__ == "__main__":
    main()
