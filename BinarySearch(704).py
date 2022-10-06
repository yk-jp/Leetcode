class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(l, r):
            mid = (l + r) // 2
            
            if l <= r:
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    return helper(mid + 1, r)
                else:
                    return helper(l, mid - 1)
            
            return -1
        
        return helper(0, len(nums)-1)