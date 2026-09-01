class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            prereqs[crs].append(pre)
        
        seen, visit = set(), set()
        output = []

        def dfs(crs):
            if crs in seen:
                return False
            if crs in visit:
                return True
            
            seen.add(crs)
            for pre in prereqs[crs]:
                if dfs(pre) == False:
                    return False
            seen.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output