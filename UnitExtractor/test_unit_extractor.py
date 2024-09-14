from unit_extractor import UnitExtractor

texts = [
    "Weight: 72 kilograms, height: 6'2\", distance: 5 km, object length: 12 inches",
    "Temperature: 98.6°F, pressure: 101.3 kPa, speed: 100mph, altitude: 30000 ft",
    "Area: 45.5 sqft, Volume: 10 cubicmeters, Radius: 12.5m, Length: 30'",
    "Box weight: 25kgs, Height: 1.75 meters, Speed: 55mph, Width: 200mm",
    "Fuel efficiency: 15.5 km/l, Water volume: 500 milliliters, Display size: 6.7in",
    "Height: 5’11”, Temperature: 25Celsius, Battery: 3000mAh, Power: 50watts",
    "Height: 5'11\", Temperature: 25Celsius, Battery: 3000mAh, Power: 50watts"
]

# Create an instance of UnitExtractor
extractor = UnitExtractor()

# Process each text and print the formatted matches
for text in texts:
    matches = extractor.extract_matches(text)
    print("Text:", text)
    print("Matches:", matches)
    print()