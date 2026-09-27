class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        n = len(nums)
        ans = 0

        for i in range(n):
            if nums[i] - 1 not in seen:
                start = nums[i]
                res = 1
                while start+1 in seen:
                    res += 1
                    start += 1

                ans = max(ans, res)

        return ans