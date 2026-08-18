class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = current_sum = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                current_sum += nums[i]
            else:
                if current_sum > max_sum :
                    max_sum = current_sum 
                current_sum =nums[i]
        return current_sum if current_sum > max_sum else max_sum 
        