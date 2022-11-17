class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = []
        patterns = {}
        
        i = 0
        while i < len(s):
            sequence = s[i:i + 10]

            if sequence not in patterns:
                patterns[sequence] = 1
            else:
                patterns[sequence] += 1

                if patterns[sequence] == 2:
                    res.append(sequence)
            i += 1
        return res