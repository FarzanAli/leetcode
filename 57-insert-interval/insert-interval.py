class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        index = 0
        newStart, newEnd = newInterval
        ans = []

        # This loop helps us find the first overlapping interval
        while index < len(intervals) and newStart > intervals[index][1]:
            ans.append(intervals[index])
            index += 1
            
        # This loop helps us find the rest of the overlapping intervals
        # while updating what our new start and end times
        while index < len(intervals) and newEnd >= intervals[index][0]:
            newStart = min(newStart, intervals[index][0])
            newEnd = max(newEnd, intervals[index][1])
            index += 1

        ans.append([newStart, newEnd])

        # Appends rest of the non overlapping intervals
        while index < len(intervals):
            ans.append(intervals[index])
            index += 1
        return ans

