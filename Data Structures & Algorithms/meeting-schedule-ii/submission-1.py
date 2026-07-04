"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        s = []
        e = []
        res = count = 0
        for interval in intervals:
            s.append(interval.start)
            e.append(interval.end)
        
        s.sort()
        e.sort()    
        i = 0
        j = 0
        while j < len(e):
            if i < len(s) and s[i] < e[j]:
                i += 1
                count += 1
            else:
                j += 1
                count -= 1
            res = max(res, count)
        return res