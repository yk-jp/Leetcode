# 1st attempt

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        max_val = float('-inf')
        l , r = 0, 0
        
        sub = 0
        
        while r - l + 1 <= k:
                sub += nums[r]
                r += 1
                
        max_val = max(sub, max_val)
        
        while r < len(nums):
            sub += nums[r]
            sub -= nums[l]
            max_val = max(sub, max_val)
            l += 1
            r += 1
        print(max_val)
        return max(sub, max_val) / k

# 2nd attempt
      
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_val = sub_val = sum(nums[:k])
        
        for i in range(k, len(nums)):
            sub_val -= nums[i-k]
            sub_val += nums[i]
            max_val = max(max_val, sub_val)
            
        return max_val / k