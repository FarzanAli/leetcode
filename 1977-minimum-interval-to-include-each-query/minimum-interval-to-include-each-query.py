class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queries = [[v, i] for i, v in enumerate(queries)]
        queries.sort(key = lambda x: -x[0])
        intervals.sort()
        minHeap = []
        index = 0
        ans = [-1] * len(queries)

        while queries:
            q = queries.pop()
            while index < len(intervals) and intervals[index][0] <= q[0]:
                heapq.heappush(minHeap, [intervals[index][1] - intervals[index][0] + 1, intervals[index][1]])
                index += 1
            
            while minHeap and minHeap[0][1] < q[0]:
                size, r = heapq.heappop(minHeap)
            if minHeap:
                ans[q[1]] = minHeap[0][0]
        return ans