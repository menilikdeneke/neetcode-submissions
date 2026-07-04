"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        s = [i.start for i in intervals]
        e = [i.end for i in intervals]

        s.sort()
        e.sort()

        i = 0
        j = 0
        count = 0
        res = 0
        while j < len(e):
            if i < len(s) and s[i] < e[j]:
                i += 1
                count += 1
            else:
                j += 1
                count -= 1
            res = max(res, count)
        return res