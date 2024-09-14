import re

class UnitExtractor:
    def __init__(self):
        self.pattern = r'(\d+[\.,]?\d*)\s*([\'\"\u2019\u201C\u201D`]+|\w+)'

    def extract_matches(self, text):
        matches = re.findall(self.pattern, text, re.IGNORECASE)
        processed_matches = self.process_units(matches)
        return processed_matches

    def process_units(self, matches):
        processed_matches = []
        i = 0
        while i < len(matches):
            value, unit = matches[i]
            unit = unit.lower()  
            
            if unit in ["'", '"', "`", "\u2019", "\u201C", "\u201D"]:
                if i > 0 and (matches[i-1][1] in ["'", '"', "`", "\u2019", "\u201C", "\u201D"]):
                    previous_value, previous_unit = matches[i-1]
                    previous_unit = previous_unit.lower()
                    if previous_unit in ["'", '"', "`", "\u2019", "\u201C", "\u201D"]:
                        try:
                            feet = float(previous_value) if previous_value else 0
                            inches = float(value) if value else 0
                            total_inches = (feet * 12) + inches
                            processed_matches[-1] = (str(total_inches), 'inches')
                        except ValueError:
                            processed_matches.append((value, unit))
                else:
                    if unit in ["'", '"', "`", "\u2019", "\u201C", "\u201D"]:
                        processed_matches.append((value, 'feet' if unit in ["'", "`"] else 'inches'))
                    else:
                        processed_matches.append((value, unit))
            else:
                processed_matches.append((value, unit))
                
            i += 1
        return processed_matches
