class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        emp = {}
        for i in nums:
            if i not in emp:
                emp[i] =1
            else:
                emp[i] +=1
        for num,value in emp.items():
            if value == 1:
                return num
        