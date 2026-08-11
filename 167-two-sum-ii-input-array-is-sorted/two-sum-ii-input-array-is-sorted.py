class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i,j in enumerate(numbers):
            com= target - j
            if com  in seen:
                return [seen[com],i+1]
            seen[j] = i+1
        return []

