class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        
        for start, end in intervals[1:]:
            # Pick the interval that ends quicker as it is the better greedy
            # choice for fewer overlaps in the future
            if start < prevEnd:
                prevEnd = min(end, prevEnd)
                res += 1
            else:
                prevEnd = end
        return res