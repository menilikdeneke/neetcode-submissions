"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        s = 0
        e = 0
        total = 0
        res = 0

        while s < len(start):
            if start[s] < end[e]:
                s += 1
                total += 1
            else:
                e += 1
                total -= 1
            res = max(res, total)
        
        return res