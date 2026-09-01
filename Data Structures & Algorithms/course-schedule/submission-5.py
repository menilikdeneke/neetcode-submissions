class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for pre, crs in prerequisites:
            preMap[pre].append(crs)
        
        seen = set()

        def dfs(crs):
            if crs in seen:
                return False
            if crs == []:
                return True
            
            seen.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            seen.remove(crs)
            preMap[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True