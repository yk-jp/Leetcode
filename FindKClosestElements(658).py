class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i = 0
        min_abs = abs(arr[0] - x)
        center = 0
        
        while i < len(arr):
            curr_abs = abs(arr[i] - x)
            if(curr_abs < min_abs):
                min_abs = curr_abs
                center = i
            i += 1
        
        l,r = center, center
        print(center)
        while r - l + 1 < k:
            if l <= 0:
                r += 1
                continue
            if r >= len(arr)-1:
                l -= 1
                continue
            
            condition1 = abs(arr[l-1] - x) < abs(arr[r+1] - x)
            condition2 = abs(arr[l-1] - x) == abs(arr[r+1] - x) and arr[l-1] < arr[r+1]
          
            if condition1 or condition2:
                l -= 1
            else:
                r += 1
        print(f"l={l} r={r}")
        return arr[l:r + 1]