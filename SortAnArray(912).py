# O(nlog(n))


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums)//2
    
        l_sub_nums = self.sortArray(nums[:mid])
        r_sub_nums = self.sortArray(nums[mid:])
        
        return self.combine_arr(l_sub_nums, r_sub_nums)
    
    def combine_arr(self, l_sub, r_sub):
        combined = []
        
        idx_l = 0
        idx_r = 0
        
        while idx_l < len(l_sub) and idx_r < len(r_sub):    
            if l_sub[idx_l] < r_sub[idx_r]:
                combined.append(l_sub[idx_l])
                idx_l += 1
            else:
                combined.append(r_sub[idx_r])
                idx_r += 1
                
        if len(combined) < len(l_sub) + len(r_sub):
            combined += r_sub[idx_r:] if idx_l >= len(l_sub) else l_sub[idx_l:] 
        
        return combined