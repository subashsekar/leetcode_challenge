class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        emp = {}

        for i in nums:
            emp[i] = emp.get(i, 0) + 1

        ans = []
        limit = len(nums) // 3
        for k, v in emp.items():
            if v > limit:
                ans.append(k)

        return ans