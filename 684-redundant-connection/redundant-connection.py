class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}
        largest = 1
        total = set()
        for a, b in edges:
            total.add(a)
            total.add(b)
            largest = max(largest, max(a, b))
            if a in graph: graph[a].append(b)
            else: graph[a] = [b]

            if b in graph: graph[b].append(a)
            else: graph[b] = [a]
        
        def dfs(n, visited, prev):
            if n in visited:
                return [False, visited]
            visited.add(n)
            for nb in graph[n]:
                if nb != prev and not dfs(nb, visited, n)[0]: return [False, visited]
            return [True, visited]
        
        for i in range(1, largest + 1):
            visited = dfs(i, set(), -1)[1]
            total = total & visited
        
        for a, b in reversed(edges):
            if a in total and b in total:
                return [a, b]