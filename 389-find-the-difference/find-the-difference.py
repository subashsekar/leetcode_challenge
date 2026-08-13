class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ascii_difference = sum(ord(char) for char in t) - sum(ord(char) for char in s)
            
            # Convert the resulting ASCII value back to a character
        return chr(ascii_difference)