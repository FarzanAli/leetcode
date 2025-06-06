class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i, j = 0, 1
        res = []

        while i < len(intervals):
            start, end = intervals[i]
            while j < len(intervals) and intervals[j][0] <= end:
                end = max(end, intervals[j][1])
                j += 1
            res.append([start, end])
            i = j
            j = i + 1
        
        return res
