class Solution:
    def trap(self, height: List[int]) -> int:
        pre=[0]*len(height)
        pre[0]=height[0]
        for i in range(1,len(height)):
            pre[i] = max(pre[i-1],height[i])
        suf=[0]*len(height)
        suf[-1]=height[-1]
        for i in range(len(height)-2,-1,-1):
            suf[i] = max(suf[i+1],height[i])
        
        max_val = 0

        for i in range(len(height)):
            max_val +=min(pre[i],suf[i]) - height[i]
        return max_val
        