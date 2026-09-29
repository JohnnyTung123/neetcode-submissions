class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        n = len(nums)
        ans = []

        for i in range(n):
            count[nums[i]] = 1 + count.get(nums[i], 0)

        # count = sorted(count.items(), key= lambda x: x[1], reverse=True)

        bucket = [[] for _ in range(n+1)]
        for num, freq in count.items():
            bucket[freq].append(num)
        
        for i in range(n, -1, -1):
            for num in bucket[i]:
                if len(ans) == k: break
                ans.append(num)
                
        
        return ans