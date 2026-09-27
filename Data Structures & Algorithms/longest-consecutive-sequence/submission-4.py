class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0

        seen = set(nums)
        ans = 1

        for i in range(n):
            if nums[i] - 1 not in seen:
                res = 1
                while (nums[i] + res) in seen:
                    res += 1

                ans = max(ans, res)

        return ans
        # n = len(nums)
        # if n == 0: return 0
        # nums.sort()
        # ans = 1
        
        # res = 1
        # for i in range(1, n):
        #     if nums[i] == nums[i-1]+1:
        #         res += 1
        #     elif nums[i] == nums[i-1]:
        #         continue
        #     else:
        #         res = 1

        #     ans = max(ans, res)
        # return ans

