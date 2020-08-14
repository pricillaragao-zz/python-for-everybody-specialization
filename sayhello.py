class Person:
  def __init__(self, altura, cor):
    self.altura = altura
    self.cor = cor

  def say_hello(self, name):
    print(f"Hello {name}! My height is {self.altura} and my color is {self.cor}.")

pricilla = Person(155, "white")
marcus = Person(176, "green")

pricilla.say_hello("Marcus")
marcus.say_hello("Hayley")
