class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {i : [] for i in range(numCourses)}
        for pair in prerequisites:
            prereqs[pair[0]].append(pair[1])
        path = set()

        def dfs(node):
            if node in path:
                return False
            if prereqs[node] == []:
                return True

            path.add(node)
            for nei in prereqs[node]:
                if not dfs(nei) == True:
                    return False
            path.remove(node)
            prereqs[node] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True