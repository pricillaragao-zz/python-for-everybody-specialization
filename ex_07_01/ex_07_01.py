# 7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case.
# Use the file words.txt to produce the output below.
# You can download the sample data at http://www.py4e.com/code3/words.txt

from pathlib import Path

while True:
    filename = input("Enter file name: ")
    filepath = Path(filename)
    if filepath.exists() and filepath.is_file():
        break
    else:
        print("File does not exists.")

with open(filename) as f:
    print(f.read().upper())
