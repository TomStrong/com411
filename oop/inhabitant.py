class Inhabitant:

  MAX_ENERGY = 100

  def __init__(self, name="Inhabitant", age=0, energy=MAX_ENERGY):
    self.name = name
    self.age = age
    self.energy = energy

  
  def __str__(self):
    return f"{self.name}: {self.age} Years, {self.energy} Energy"