conversion_map = {
    # Length (convert to allowed units: metre, centimetre, inch, foot, millimetre, yard)
    'centimetre': 1.0,           # Base unit for length (as allowed in entity_unit_map)
    'foot': 1.0,                 # Base unit (no conversion needed)
    'inch': 1.0,                 # Base unit (no conversion needed)
    'metre': 1.0,                # Base unit (no conversion needed)
    'millimetre': 1.0,           # Base unit (no conversion needed)
    'yard': 1.0,                 # Base unit (no conversion needed)
    'kilometre': 1000.0,         # Convert kilometre to metre
    'mile': 1609.34,             # Convert mile to metre

    # Weight (convert to allowed units: kilogram, gram, pound, ton, ounce)
    'gram': 1.0,                 # Base unit for weight
    'kilogram': 1.0,             # Base unit (no conversion needed)
    'microgram': 1e-6,           # Convert to gram
    'milligram': 0.001,          # Convert to gram
    'ounce': 1.0,                # Base unit (no conversion needed)
    'pound': 1.0,                # Base unit (no conversion needed)
    'ton': 1.0,                  # Base unit (no conversion needed)
    'stone': 6.35029,            # Convert stone to kilogram

    # Voltage (convert to allowed units: volt, millivolt, kilovolt)
    'volt': 1.0,                 # Base unit (no conversion needed)
    'millivolt': 1.0,            # Base unit (no conversion needed)
    'kilovolt': 1.0,             # Base unit (no conversion needed)

    # Wattage (convert to allowed units: watt, kilowatt)
    'watt': 1.0,                 # Base unit (no conversion needed)
    'kilowatt': 1.0,             # Base unit (no conversion needed)
    'megawatt': 1000.0,          # Convert megawatt to kilowatt

    # Volume (convert to allowed units: litre, millilitre, gallon, pint, quart, cubic foot, etc.)
    'litre': 1.0,                # Base unit for volume
    'millilitre': 1.0,           # Base unit (no conversion needed)
    'centilitre': 1.0,           # Base unit (no conversion needed)
    'gallon': 1.0,               # Base unit (no conversion needed)
    'imperial gallon': 1.0,      # Base unit (no conversion needed)
    'pint': 1.0,                 # Base unit (no conversion needed)
    'quart': 1.0,                # Base unit (no conversion needed)
    'cubic foot': 1.0,           # Base unit (no conversion needed)
    'cubic inch': 1.0,           # Base unit (no conversion needed)
    'microlitre': 1e-6,          # Convert microlitre to litre
    'fluid ounce': 0.0295735,    # Convert fluid ounce to litre
    'barrel': 158.987,           # Convert barrel to litre
}
