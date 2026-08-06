class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numbers = set(nums)
        emp = []
        leng = len(nums)+1
        for i in range(1, leng):
            if i not in numbers:
                emp.append(i)

        return emp
        
        