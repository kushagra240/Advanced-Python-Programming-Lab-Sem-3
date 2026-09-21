# Experiment No. 8: File Handling and I/O
# Aim: Read data from an input file, count lines, extract the first two lines, and write them to a new file.

# 1. Read the input file
with open("input.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# 2. Count total lines
print("Total lines:", len(lines))

# 3. Extract the first two lines
first_two = lines[:2]
print("\nFirst two lines:")
for line in first_two:
    print(line, end="")

# 4. Write extracted lines to the output file
with open("output.txt", "w", encoding="utf-8") as file:
    file.writelines(first_two)

print("\n\nData written to output.txt successfully.")