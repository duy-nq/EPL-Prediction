from fuzzywuzzy import fuzz

def match_strings(str1, str2, threshold=35):
    similarity_ratio = fuzz.ratio(str1.lower(), str2.lower())
    return similarity_ratio >= threshold

# Example usage
name1 = "Joseph Whitworth"
name2 = "Joe Whitworth"

if match_strings(name1, name2):
    print(f"{name1} and {name2} are considered a match.")
else:
    print(f"{name1} and {name2} are not considered a match.")
