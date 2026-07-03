"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        intervals.sort(key = lambda interval: interval.start)
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i].start < res[-1].end:
                return False
            res.append(intervals[i])
        return True