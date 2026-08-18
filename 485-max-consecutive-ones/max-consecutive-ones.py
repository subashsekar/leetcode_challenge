class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ans = current_count = 0
        for num in nums:
            if num == 1:
                current_count += 1
                max_ans = max(max_ans,current_count)
            else:
                current_count = 0
        return max_ans