import csv
import json

# Define file paths
csv_file_path = "input.csv"
json_file_path = "output.json"

# Read CSV and convert each row into a dictionary
with open(csv_file_path, mode="r", encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)

# Write the list of dictionaries to a JSON file
with open(json_file_path, mode="w", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=4)

print("CSV converted to JSON successfully.")