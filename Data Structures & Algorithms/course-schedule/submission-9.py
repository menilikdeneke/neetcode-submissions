class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs_to_courses = {i:[] for i in range(numCourses)}

        seen = set()

        for pre, crs in prerequisites:
            prereqs_to_courses[crs].append(pre)

        def dfs(crs):
            if crs in seen:
                return False      
            if prereqs_to_courses[crs] == []:
                return True
            
            seen.add(crs)

            for pre in prereqs_to_courses[crs]:
                if not dfs(pre):
                    return False
                
            seen.remove(crs)
            prereqs_to_courses[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
