class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
       single = int("".join(map(str,digits)))
       split = single + 1
       digit_split = [int(i) for i in str(split)]
       return digit_split
        