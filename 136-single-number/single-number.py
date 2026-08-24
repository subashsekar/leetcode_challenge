class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        emp = 0
        for i in nums:
            emp ^= i
        return emp
        