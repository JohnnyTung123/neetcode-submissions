class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        count = {}
        n = len(nums)

        # num -> freq
        for i in range(n):
            count[nums[i]] = count.get(nums[i], 0) + 1

        # bucket sort: freq -> num
        # bucket = [0] * n
        bucket = [[] for _ in range(n+1)]
        for num, freq in count.items():
            bucket[freq].append(num)

        for i in range(n, -1, -1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        
        return ans

