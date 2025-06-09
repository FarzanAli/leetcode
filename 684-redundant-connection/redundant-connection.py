class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rank = [0] * (len(edges) + 1)
        par = [i for i in range(len(edges) + 1)]

        def find(a):
            if a != par[a]:
                # Path compression
                par[a] = find(par[a])
            return par[a]

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
            # Check if this edge creates a cycle
            if not union(a, b):
                return [a, b]