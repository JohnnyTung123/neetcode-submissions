class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # seen = set(nums)
        # n = len(nums)
        # ans = 0

        # for i in range(n):
        #     if nums[i] - 1 not in seen:
        #         start = nums[i]
        #         res = 1
        #         while start+1 in seen:
        #             res += 1
        #             start += 1

        #         ans = max(ans, res)

        # return ans
        n = len(nums)
        if n == 0: return 0
        nums.sort()
        ans = 1
        
        res = 1
        for i in range(1, n):
            if nums[i] == nums[i-1]+1:
                res += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                res = 1

            ans = max(ans, res)
        return ans

