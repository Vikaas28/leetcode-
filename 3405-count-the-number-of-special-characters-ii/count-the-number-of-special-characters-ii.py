class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = {}
        first_upper = {}

        # Record last lowercase occurrence and first uppercase occurrence
        for idx, char in enumerate(word):
            if char.islower():
                last_lower[char] = idx
            elif char.isupper():
                if char not in first_upper:
                    first_upper[char] = idx

        special_count = 0

        # Check conditions for each lowercase letter present
        for char in last_lower:
            upper_char = char.upper()
            if upper_char in first_upper and last_lower[char] < first_upper[upper_char]:
                special_count += 1

        return special_count