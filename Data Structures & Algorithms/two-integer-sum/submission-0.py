class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # num -> idx
        seen[nums[0]] = 0
        n = len(nums)

        for i in range(1, n):
            if target - nums[i] in seen:
                idx = seen[target - nums[i]]
                return [idx, i]
            seen[nums[i]] = i

        return [-1, -1]