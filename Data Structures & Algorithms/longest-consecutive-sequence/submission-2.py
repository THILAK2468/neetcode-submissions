class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numSet = set(nums)
        max_len = 1

        for num in nums:
            if (num-1) not in numSet:
                currentnum = num
                currentlen = 1
                while(currentnum+1) in numSet:
                    currentnum+=1
                    currentlen+=1
                max_len = max(max_len,currentlen)
        return max_len