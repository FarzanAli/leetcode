class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rank = [ 0 for _ in range(len(edges) + 1) ]
        par = [ i for i in range(len(edges) + 1) ]

        def find(n):
            if n == par[n]:
                return n
            par[n] = find(par[n])
            return par[n]

        def union(a, b):
            a, b = find(a), find(b)
            if a == b:
                return False
            if rank[a] > rank[b]:
                par[b] = a
                rank[a] += rank[b]
            else:
                par[a] = b
                rank[b] += rank[a]
            return True
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]
        return True
