class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        emp = {}

        for i in nums:
            emp[i] = emp.get(i, 0) + 1
        return max(emp,key=emp.get)
        