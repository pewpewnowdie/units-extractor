import re
from unit_mapping import unit_mapping
from fuzzywuzzy import process

class UnitExtractor:
    def __init__(self):
        # Updated regex to capture units like m/s, ft/s without ^.
        self.pattern = r'(\d+[\.,]?\d*)\s*([\'\"\u2019\u201C\u201D`]+|[\w/]+)'
        self.unit_map = unit_mapping
        self.unit_names = list(unit_mapping.keys())
        self.THRESHOLD = 50

    def extract_matches(self, text):
        matches = re.findall(self.pattern, text, re.IGNORECASE)
        processed_matches = self.process_units(matches)
        return processed_matches

    def spell_matching(self, unit):
        closest_match, score = process.extractOne(unit, self.unit_names)
        if score >= self.THRESHOLD: 
            return closest_match
        else:
            return unit

    def process_units(self, matches):
        processed_matches = []
        i = 0
        while i < len(matches):
            value, unit = matches[i]
            unit = unit.lower().strip()

            # Handle compound units like m/s
            if '/' in unit:
                unit = self.spell_matching(unit)
                try:
                    processed_matches.append((value, self.unit_map[unit]))
                except KeyError:
                    processed_matches.append((value, unit))
            elif unit in ["'", '"', "`", "\u2019", "\u201C", "\u201D"]:
                if i > 0 and (matches[i-1][1] in ["'", '"', "`", "\u2019", "\u201C", "\u201D"]):
                    previous_value, previous_unit = matches[i-1]
                    previous_unit = previous_unit.lower()
                    if previous_unit in ["'", '"', "`", "\u2019", "\u201C", "\u201D"]:
                        try:
                            feet = float(previous_value) if previous_value else 0
                            inches = float(value) if value else 0
                            total_inches = (feet * 12) + inches
                            processed_matches[-1] = (str(total_inches), 'in')
                        except ValueError:
                            try:
                                processed_matches.append((value, self.unit_map[unit]))
                            except KeyError:
                                processed_matches.append((value, unit))
                else:
                    if unit in ["'", '"', "`", "\u2019", "\u201C", "\u201D"]:
                            processed_matches.append((value, 'ft' if unit in ["'", "`"] else 'in'))
                    else:
                        try:
                            processed_matches.append((value, self.unit_map[unit]))
                        except KeyError:
                            processed_matches.append((value, unit))
            else:
                unit = self.spell_matching(unit)
                try:
                    processed_matches.append((value, self.unit_map[unit]))
                except:
                    processed_matches.append((value, unit))
                
            i += 1
        return processed_matches
