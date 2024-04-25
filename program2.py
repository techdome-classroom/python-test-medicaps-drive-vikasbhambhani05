class Solution(object):
    def romanToInt(self, s):
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0

        for char in s:
            current_value = roman_values[char]
            total += current_value

            if current_value > prev_value:
                total -= 2 * prev_value

            prev_value = current_value

        return total