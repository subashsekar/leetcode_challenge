class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = 0
        count =0
        for ch in s:
            if ch == "R":
                count +=1
            else:
                count -= 1
            if count == 0:
                result +=1
        return result
        