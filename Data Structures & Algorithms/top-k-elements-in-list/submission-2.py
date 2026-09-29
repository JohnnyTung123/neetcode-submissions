class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        n = len(nums)
        ans = []

        for i in range(n):
            count[nums[i]] = 1 + count.get(nums[i], 0)

        count = sorted(count.items(), key= lambda x: x[1], reverse=True)

        for num, freq in count:
            if len(ans) == k: break
            ans.append(num)
         
        
        return ans