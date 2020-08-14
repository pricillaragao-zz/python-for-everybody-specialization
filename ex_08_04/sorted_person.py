class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"name: {self.name}, age: {self.age}"


pricilla = Person("Pricilla Patricia de Aragao", 27)
marcus = Person("Marcus Vinicius Monteiro de Souza", 31)
carlos = Person("Carlos de Souza", 76)
pessoas = [carlos, pricilla, marcus]
print(pessoas)
print(sorted(pessoas, key=lambda p: p.name))
