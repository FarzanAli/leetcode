class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        minHeap = [(0, k)]
        visited = set()

        most = 0
        while minHeap:
            timeTaken, curr = heapq.heappop(minHeap)
            if curr in visited:
                continue
            visited.add(curr)
            most = max(most, timeTaken)

            for nb, w in graph[curr]:
                if nb not in visited:
                    heapq.heappush(minHeap, (timeTaken + w, nb))
        return most if len(visited) == n else -1