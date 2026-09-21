import csv
import json

# Read CSV file
with open("input.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)

# Write data to JSON file
with open("output.json", "w") as jsonfile:
    json.dump(data, jsonfile, indent=4)

print("CSV converted to JSON successfully.")