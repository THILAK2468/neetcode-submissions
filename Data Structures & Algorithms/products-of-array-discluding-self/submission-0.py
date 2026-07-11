class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1]*n
        sufix =[1]*n
        res =[1]*n
        for i in range(1,n):
            pre[i] =pre[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            sufix[i] = sufix[i+1]*nums[i+1]
        for i in range(n):
            res[i] = pre[i]*sufix[i]
        return res 