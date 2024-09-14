unit_mapping = {
    # Length
    'meter': 'm', 'meters': 'm', 'metre': 'm', 'metres': 'm', 'm': 'm',
    'centimeter': 'cm', 'centimeters': 'cm', 'centimetre': 'cm', 'centimetres': 'cm', 'cm': 'cm',
    'millimeter': 'mm', 'millimeters': 'mm', 'millimetre': 'mm', 'millimetres': 'mm', 'mm': 'mm',
    'kilometer': 'km', 'kilometers': 'km', 'kilometre': 'km', 'kilometres': 'km', 'km': 'km',
    'foot': 'ft', 'feet': 'ft', 'ft': 'ft',
    'inch': 'in', 'inches': 'in', 'in': 'in',
    'yard': 'yd', 'yards': 'yd', 'yd': 'yd',
    'mile': 'mi', 'miles': 'mi', 'mi': 'mi',
    'nautical mile': 'nmi', 'nautical miles': 'nmi', 'nmi': 'nmi',
    'angstrom': 'Å', 'angstroms': 'Å', 'Å': 'Å',
    'fathom': 'fathom', 'fathoms': 'fathom', 'fathom': 'fathom',

    # Area
    'square meter': 'm2', 'square meters': 'm2', 'square metre': 'm2', 'square metres': 'm2', 'm2': 'm2',
    'square centimeter': 'cm2', 'square centimeters': 'cm2', 'square centimetre': 'cm2', 'square centimetres': 'cm2', 'cm2': 'cm2',
    'square millimeter': 'mm2', 'square millimeters': 'mm2', 'square millimetre': 'mm2', 'square millimetres': 'mm2', 'mm2': 'mm2',
    'square kilometer': 'km2', 'square kilometers': 'km2', 'square kilometre': 'km2', 'square kilometres': 'km2', 'km2': 'km2',
    'acre': 'acre', 'acres': 'acre',
    'hectare': 'ha', 'hectares': 'ha', 'ha': 'ha',
    'barn': 'b', 'barns': 'b', 'b': 'b',
    'are': 'a', 'ares': 'a', 'a': 'a',

    # Volume
    'liter': 'L', 'liters': 'L', 'litre': 'L', 'litres': 'L', 'l': 'L',
    'milliliter': 'mL', 'milliliters': 'mL', 'millilitre': 'mL', 'millilitres': 'mL', 'ml': 'mL',
    'cubic meter': 'm3', 'cubic meters': 'm3', 'cubic metre': 'm3', 'cubic metres': 'm3', 'm3': 'm3',
    'cubic centimeter': 'cm3', 'cubic centimeters': 'cm3', 'cubic centimetre': 'cm3', 'cubic centimetres': 'cm3', 'cm3': 'cm3',
    'cubic inch': 'in3', 'cubic inches': 'in3', 'in3': 'in3',
    'cubic foot': 'ft3', 'cubic feet': 'ft3', 'ft3': 'ft3',
    'gallon': 'gal', 'gallons': 'gal', 'gal': 'gal',
    'quart': 'qt', 'quarts': 'qt', 'qt': 'qt',
    'pint': 'pt', 'pints': 'pt', 'pt': 'pt',
    'fluid ounce': 'fl oz', 'fluid ounces': 'fl oz', 'fl oz': 'fl oz',
    'liter per minute': 'L/min', 'litre per minute': 'L/min', 'L/min': 'L/min',

    # Mass
    'kilogram': 'kg', 'kilograms': 'kg', 'kg': 'kg',
    'gram': 'g', 'grams': 'g', 'g': 'g',
    'milligram': 'mg', 'milligrams': 'mg', 'mg': 'mg',
    'tonne': 't', 'tonnes': 't', 'metric ton': 't', 'metric tons': 't', 't': 't',
    'pound': 'lb', 'pounds': 'lb', 'lb': 'lb',
    'ounce': 'oz', 'ounces': 'oz', 'oz': 'oz',
    'stone': 'st', 'stones': 'st', 'st': 'st',
    'carat': 'ct', 'carats': 'ct', 'ct': 'ct',
    'slug': 'slug', 'slugs': 'slug', 'slug': 'slug',

    # Temperature
    'celsius': 'C', 'celsius': 'C', 'celcius': 'C', 'c': 'C',
    'fahrenheit': 'F', 'fahrenheits': 'F', 'f': 'F',
    'kelvin': 'K', 'kelvins': 'K', 'k': 'K',

    # Time
    'second': 's', 'seconds': 's', 'sec': 's',
    'minute': 'min', 'minutes': 'min', 'min': 'min',
    'hour': 'h', 'hours': 'h', 'hr': 'h',
    'day': 'd', 'days': 'd',
    'week': 'w', 'weeks': 'w',
    'month': 'mo', 'months': 'mo',
    'year': 'yr', 'years': 'yr',
    'decade': 'dec', 'decades': 'dec', 'dec': 'dec',
    'century': 'c', 'centuries': 'c', 'c': 'c',
    'jiffy': 'jiffy', 'jiffies': 'jiffy', 'jiffy': 'jiffy',

    # Energy
    'joule': 'J', 'joules': 'J', 'j': 'J',
    'calorie': 'cal', 'calories': 'cal', 'cal': 'cal',
    'kilocalorie': 'kcal', 'kilocalories': 'kcal', 'kcal': 'kcal',
    'watt-hour': 'Wh', 'watt-hours': 'Wh', 'Wh': 'Wh',
    'kilowatt-hour': 'kWh', 'kilowatt-hours': 'kWh', 'kWh': 'kWh',
    'electronvolt': 'eV', 'electronvolts': 'eV', 'eV': 'eV',
    'BTU': 'BTU', 'British thermal unit': 'BTU', 'BTU': 'BTU',
    'therm': 'therm', 'therms': 'therm', 'therm': 'therm',

    # Power
    'watt': 'W', 'watts': 'W', 'w': 'W',
    'kilowatt': 'kW', 'kilowatts': 'kW', 'kW': 'kW',
    'megawatt': 'MW', 'megawatts': 'MW', 'MW': 'MW',
    'gigawatt': 'GW', 'gigawatts': 'GW', 'GW': 'GW',
    'terawatt': 'TW', 'terawatts': 'TW', 'TW': 'TW',
    'horsepower': 'hp', 'horsepowers': 'hp', 'hp': 'hp',
    'metric horsepower': 'PS', 'metric horsepowers': 'PS', 'PS': 'PS',

    # Pressure
    'pascal': 'Pa', 'pascals': 'Pa', 'pa': 'Pa',
    'bar': 'bar', 'bars': 'bar', 'bar': 'bar',
    'psi': 'psi', 'pounds per square inch': 'psi', 'pounds per square inch': 'psi',
    'atmosphere': 'atm', 'atmospheres': 'atm', 'atm': 'atm',
    'torr': 'Torr', 'torrs': 'Torr', 'Torr': 'Torr',
    'millimeter of mercury': 'mmHg', 'millimeters of mercury': 'mmHg', 'mmHg': 'mmHg',
    'centimeter of mercury': 'cmHg', 'centimeters of mercury': 'cmHg', 'cmHg': 'cmHg',

    # Frequency
    'hertz': 'Hz', 'hertz': 'Hz', 'hz': 'Hz',
    'kilohertz': 'kHz', 'kilohertz': 'kHz', 'khz': 'kHz',
    'megahertz': 'MHz', 'megahertz': 'MHz', 'mhz': 'MHz',
    'gigahertz': 'GHz', 'gigahertz': 'GHz', 'ghz': 'GHz',
    'terahertz': 'THz', 'terahertz': 'THz', 'thz': 'THz',

    # Density
    'kilogram per cubic meter': 'kg/m3', 'kilograms per cubic meter': 'kg/m3', 'kg/m3': 'kg/m3',
    'gram per cubic centimeter': 'g/cm3', 'grams per cubic centimeter': 'g/cm3', 'g/cm3': 'g/cm3',
    'pound per cubic foot': 'lb/ft3', 'pounds per cubic foot': 'lb/ft3', 'lb/ft3': 'lb/ft3',

    # Speed
    'meters per second': 'm/s', 'meter per second': 'm/s', 'm/s': 'm/s',
    'kilometers per hour': 'km/h', 'kilometer per hour': 'km/h', 'km/h': 'km/h',
    'miles per hour': 'mph', 'mile per hour': 'mph', 'mph': 'mph',

    # Fuel Efficiency
    'kilometers per liter': 'km/l', 'kilometer per liter': 'km/l', 'km/l': 'km/l',
    'miles per gallon': 'mpg', 'mile per gallon': 'mpg', 'mpg': 'mpg',
    'liters per 100 kilometers': 'L/100km', 'litres per 100 kilometers': 'L/100km', 'L/100km': 'L/100km',

    # Power Density
    'watt per square meter': 'W/m2', 'watts per square meter': 'W/m2', 'W/m2': 'W/m2',
    'watt per cubic meter': 'W/m3', 'watts per cubic meter': 'W/m3', 'W/m3': 'W/m3',

    # Pressure
    'newton per square meter': 'N/m2', 'newtons per square meter': 'N/m2', 'N/m2': 'N/m2',
    'pounds per square inch': 'psi', 'pound per square inch': 'psi', 'psi': 'psi',

    # Specific Energy
    'joules per kilogram': 'J/kg', 'joule per kilogram': 'J/kg', 'J/kg': 'J/kg',

    # Current Density
    'ampere per square meter': 'A/m2', 'amperes per square meter': 'A/m2', 'A/m2': 'A/m2',

    # Linear Mass Density
    'kilogram per meter': 'kg/m', 'kilograms per meter': 'kg/m', 'kg/m': 'kg/m',

    # Luminous Flux per Area (Illuminance)
    'lumen per square meter': 'lm/m2', 'lumens per square meter': 'lm/m2', 'lm/m2': 'lm/m2',
    
    # Flow Rate
    'cubic meter per second': 'm3/s', 'cubic meters per second': 'm3/s', 'm3/s': 'm3/s',
    'liter per second': 'L/s', 'liters per second': 'L/s', 'L/s': 'L/s',
    'liter per minute': 'L/min', 'liters per minute': 'L/min', 'L/min': 'L/min',

    # Heat Flux
    'watt per square meter kelvin': 'W/(m2·K)', 'watts per square meter kelvin': 'W/(m2·K)', 'W/(m2·K)': 'W/(m2·K)',

    # Heat Transfer Coefficient
    'watt per square meter kelvin': 'W/m2K', 'watts per square meter kelvin': 'W/m2K', 'W/m2K': 'W/m2K',
}
