class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums= sorted(nums)
        emp = []
        for i,j in enumerate(nums):
            if j == target:
                emp.append(i)
        return emp
        