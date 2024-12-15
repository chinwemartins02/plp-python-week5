# Parent Class: Superhero
class Superhero:
    def __init__(self, name, alias, power_level):
        self.name = name                # Public attribute
        self._alias = alias             # Protected attribute
        self.__power_level = power_level  # Private attribute

    # Public method
    def introduce(self):
        return f"I am {self.name}, also known as {self._alias}!"

    # Encapsulation: Getter for private attribute
    def get_power_level(self):
        return self.__power_level

    # Encapsulation: Setter for private attribute
    def train(self):
        self.__power_level += 10
        print(f"{self.name} trains hard! Power level increases to {self.__power_level}.")

    # Polymorphism: Method to describe a special power
    def special_power(self):
        return f"{self._alias} uses a generic power!"

# Child Class: FlyingHero
class FlyingHero(Superhero):
    def __init__(self, name, alias, power_level, flight_speed):
        super().__init__(name, alias, power_level)
        self.flight_speed = flight_speed  # New attribute specific to FlyingHero

    # Overriding the special_power method
    def special_power(self):
        return f"{self._alias} flies at a speed of {self.flight_speed} mph!"

# Child Class: StrongHero
class StrongHero(Superhero):
    def __init__(self, name, alias, power_level, lifting_capacity):
        super().__init__(name, alias, power_level)
        self.lifting_capacity = lifting_capacity  # New attribute specific to StrongHero

    # Overriding the special_power method
    def special_power(self):
        return f"{self._alias} lifts objects weighing up to {self.lifting_capacity} tons!"

# Main Program
if __name__ == "__main__":
    # Create instances of Superhero and subclasses
    generic_hero = Superhero("John Doe", "HeroX", 50)
    flying_hero = FlyingHero("Clark Kent", "Superman", 90, 200)
    strong_hero = StrongHero("Diana Prince", "Wonder Woman", 85, 50)

    # Introduce heroes and showcase their powers
    print(generic_hero.introduce())
    print(generic_hero.special_power())
    print()

    print(flying_hero.introduce())
    print(flying_hero.special_power())
    flying_hero.train()  # Boost power level through training
    print()

    print(strong_hero.introduce())
    print(strong_hero.special_power())
    strong_hero.train()  # Boost power level through training
