"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals: return True

        # Since Interval is an object we provide the key that should be used to sort
        # as the start attribute
        intervals.sort(key=lambda x: x.start)
        prev = intervals[0].end

        for interval in intervals[1:]:
            if interval.start < prev:
                return False
            else:
                prev = interval.end
        return True
