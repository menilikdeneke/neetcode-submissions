class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {_: [] for _ in range(numCourses)}

        for pre, crs in prerequisites:
            preMap[pre].append(crs)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if preMap[crs] == []:
                return True
            
            visited.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            preMap[crs] = []
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True