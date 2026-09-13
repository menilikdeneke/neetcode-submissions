class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs_to_courses = {i : [] for i in range(numCourses)}

        for pre, crs in prerequisites:
            prereqs_to_courses[crs].append(pre)
        seen = set()

        def dfs(node):
            if prereqs_to_courses[node] == []:
                return True
            if node in seen:
                return False
            
            seen.add(node)

            for crs in prereqs_to_courses[node]:
                if not dfs(crs):
                    return False
            seen.remove(node)
            prereqs_to_courses[crs] = []

            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True