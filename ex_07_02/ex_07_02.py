# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
# Use the file name mbox-short.txt as the file name
from pathlib import Path

while True:
    filename = input("Enter file name: ")
    filepath = Path(filename)
    if filepath.exists() and filepath.is_file():
        break
    else:
        print("File does not exists.")

with open(filename) as f:
    count = 0
    total = 0
    for line in f:
        if not line.startswith("X-DSPAM-Confidence:"):
            continue
        colon_position = line.find(":")
        text_after_colon = line[colon_position + 1 :]
        values = float(text_after_colon)
        count = count + 1
        total = total + values
    average = total / count
    print("Average spam confidence:", average)
