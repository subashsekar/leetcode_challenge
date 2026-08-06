class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i]= 1
            else:
                dic[i] +=1
        return [k for k,v in dic.items() if v > 1] 

        
        