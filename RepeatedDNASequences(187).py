class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = []
        patterns = {}
        
        i = 0
        while i + 10 <= len(s):
            dna = s[i:i + 10]
            
            if dna not in patterns:
                patterns[dna] = 1
            else:
                patterns[dna] += 1
                if patterns[dna] == 2:
                    res.append(dna)
            
            i += 1
        
        return res