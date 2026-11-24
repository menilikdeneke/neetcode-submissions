class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_to_crs = {i : [] for i in range(numCourses)}

        for pre, crs in prerequisites:
            prereq_to_crs[crs].append(pre)
        
        visit, cycle = set(), set()
        
        def dfs(node):
            if prereq_to_crs[node] == []:
                return True
            
            if node in visit:
                return False
            
            visit.add(node)
            for pre in prereq_to_crs[node]:
                if not dfs(pre):
                    return False
            visit.remove(node)
            prereq_to_crs[node] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True