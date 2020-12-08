from inhabitant import Inhabitant

class Human(Inhabitant):
  def __init__(self, name="Human", age=0, energy=Inhabitant.MAX_ENERGY):
    super().__init__(name=name, age=age, energy=energy)

  def __repr__(self):
      return f'human(name={self.name}, age={self.age}, energy={self.energy})'

  def __str__(self):
    return f'My name is {self.name} and I am {self.age} years old and my energy is {self.energy}.'

  # instance methods
  def display(self):
    print(f"I am {self.name}")

  def grow(self):
    self.age += 1

  def eat(self, amount):
    potential_energy = self.energy + amount
    if (potential_energy > Inhabitant.MAX_ENERGY):
      self.energy = Inhabitant.MAX_ENERGY
      return potential_energy - self.energy
    else:
      self.energy = potential_energy
      return 0

  def move(self, distance):
    potential_energy = self.energy - distance
    if (potential_energy < 0):
      self.energy = 0
      return self.energy - abs(potential_energy)
    else:
      self.energy = potential_energy
      return 0


if (__name__ == "__main__"):
  human = Human()
  print(repr(human))
  human.move(10)
  print(repr(human))
  human.eat(5)
  print(repr(human))
  human.eat(20)
  print(repr(human))