# COLOR DATA PRACTICE

import json

# Load Color Data from JSON file
file = open("color-data.json", "r")
dataStr = file.read()
file.close()

color_data = json.loads(dataStr)

#1
for color in color_data:
    print(f"{color['name']} - {color['family']}")

#2
for color in color_data:
    if color['brightness'] >= 200:
        print(f"{color['name']} - {color['brightness']}")

#3
num_redPink = 0
for color in color_data:
    family = color['family']
    if family == "Red" or family == "Pink":
        print(f"{num_redPink}")

#4
target_family = input("Enter color family: ")
family_count = 0
for color in color_data:
    if color['family'] == target_family:
        print(f"{color['name']} - {color['family']}")
        family_count += 1
print(f"Total Colors in family: {family_count}")

#5
target_letter = input("Enter a starting letter: ")
color_count = 0
for color in color_data:
    if color['name'][0] == target_letter:
        print(color['name'])
        color_count += 1
print(f"total colors with starting letter: {color_count}")
