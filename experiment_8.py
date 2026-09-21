# File Handling and I/O

# Read input file
file = open("input.txt", "r")
lines = file.readlines()
file.close()

# Count lines
print("Total lines:", len(lines))

# Extract first two lines
first_two = lines[:2]

print("First two lines:")
print("".join(first_two))

# Write to output file
file = open("output.txt", "w")
file.writelines(first_two)
file.close()

print("Data written to output.txt")