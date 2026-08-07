class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        op = s.split()
        return len(op[-1])

        