class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            adj[course].append(prerequisite)

        visiting = set()
        def dfs(node):
            # course in visisting
            if node in visiting:
                return False
            # base case
            if adj[node] == []:
                return True

            visiting.add(node)
            for nxtNode in adj[node]:
                if not dfs(nxtNode):
                    return False
            visiting.remove(node)
            # clean in adj
            adj[node] = []
            return True
        for node in range(numCourses):
            if not dfs(node):
                return False
        return True