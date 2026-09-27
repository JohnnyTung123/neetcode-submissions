class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # num -> idx
        n = len(nums)

        # for i in range(1, n):
        for i in range(n):
            if target - nums[i] in seen:
                idx = seen[target - nums[i]]
                return [idx, i]
            seen[nums[i]] = i

        return [-1, -1]