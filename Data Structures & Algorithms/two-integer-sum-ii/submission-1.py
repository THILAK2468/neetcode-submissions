class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return[]
        s,e = 0,len(numbers)-1
        while s<e:
            if numbers[s]+numbers[e]==target:
                break
            elif numbers[s]+numbers[e]>target:
                e-=1
            else:
                s+=1
        return [s+1,e+1]
        
