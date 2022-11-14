class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = {}

        for ch in s:
            if ch not in hashmap:
                hashmap[ch] = 1
            else:
                hashmap[ch] += 1
        
        ans = 0
        is_added = False
        for key in hashmap:
            ans += hashmap[key]//2 * 2
            hashmap[key] -= hashmap[key]//2 * 2

            if not is_added and hashmap[key] > 0:
                ans += 1
                is_added = True

        return ans