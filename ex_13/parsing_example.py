class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello! My name is {self.name}!")

    def foo(self):
        return 1

    def bar(self):
        return [1]

    # def __repr__(self):
    #     return f"name: {self.name}"


class Trabalhador(Person):
    def __init__(self, name):
        super().__init__(name)


def parse_to_persons(text: str):
    names = text.split(".")
    return [Trabalhador(name) for name in names]


if __name__ == "__main__":
    text = "pricilla.marcus.chris"
    persons = parse_to_persons(text)
    for person in persons:
        print(person)
