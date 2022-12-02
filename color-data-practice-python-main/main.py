# COLOR DATA PRACTICE

import json

# Load Color Data from JSON file
file = open("color-data.json", "r")
dataStr = file.read()
file.close()

color_data = json.loads(dataStr)

#Q1
for color in color_data:
    print(f"{color['name']} = {color['family']}")

#Q2
for color in color_data:
    if color['brightness'] > 200:
        print(f"{color['name']} = {color['brightness']}")

#Q3
for color in color_data:

        print(f"{color['name']} = {color['family']}")