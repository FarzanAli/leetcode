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
            # Create minHeap such that all intervals start before the current query value
            # mantain each intervals size and end value
            while index < len(intervals) and intervals[index][0] <= q[0]:
                heapq.heappush(minHeap, [intervals[index][1] - intervals[index][0] + 1, intervals[index][1]])
                index += 1
            # Remove all the smallest intervals that have an end value less
            # than the query value (irrelevant intervals)
            while minHeap and minHeap[0][1] < q[0]:
                size, r = heapq.heappop(minHeap)
            # If an interval exists that encompasses the query value, overwrite the -1
            if minHeap:
                ans[q[1]] = minHeap[0][0]
        return ans