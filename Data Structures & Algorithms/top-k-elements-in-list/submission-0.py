class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] =1
        buckets = [[] for i in range(len(nums)+1)]

        for num,val in freq.items():
            buckets[val].append(num)
        res=[]
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                res.append(num)
            if len(res) == k:
                return res