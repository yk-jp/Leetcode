class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj_list = [[0, 0] for i in range(n + 1)]
        
        for v in trust:
            adj_list[v[0]][0] += 1
            adj_list[v[1]][1] += 1
        
        for label, v in enumerate(adj_list):
            if label == 0:
                continue
            if v[0] == 0 and v[1] == n - 1:
                return label
        
        return -1