class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        count_arr = [1] * len(nums)
        
        for i in range(len(nums)):
            max_num = nums[i]
            for j in range(0, i, 1):
                if nums[j] < max_num:
                    count_arr[i] = max(count_arr[i],count_arr[j] + 1)
                    
        print(count_arr)
        
        return max(count_arr)