class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        res = []

        p_map = self.create_hashmap(p)
        sub_map = self.create_hashmap(s[0:len(p)])

        for i in range(len(s) - len(p) + 1):
            if i != 0:
                end_el_at = s[i + len(p) - 1]
                sub_map[end_el_at] = 1 + sub_map.get(end_el_at, 0)  
                sub_map[s[i-1]] -= 1
                
                if sub_map[s[i-1]] <= 0:
                    sub_map.pop(s[i-1])
              
            if p_map == sub_map:
                res.append(i)

        return res

    def create_hashmap(self, s):
        hashmap = {}

        for i in range(len(s)):
            hashmap[s[i]] = 1 + hashmap.get(s[i],0)
        
        return hashmap