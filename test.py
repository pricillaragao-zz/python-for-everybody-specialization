class Reader:
    def __init__(self, filename: str):
        self.file = open(filename)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()


with Reader("5_04.py") as my_reader:
    print(my_reader.file.read())
