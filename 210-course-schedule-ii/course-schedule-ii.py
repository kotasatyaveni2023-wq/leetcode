class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order=[]
        courses=prerequisites
        g=defaultdict(list)
        for a,b in courses:
            g[a].append(b)
        unvisited=0
        visiting=1
        visited=2
        states=[unvisited]*numCourses
        def dfs(node):
            state=states[node]
            if state==visiting:
                return False
            if state==visited:
                return True
            states[node]=visiting
            for nei in g[node]:
                if not dfs(nei):
                    return False
            states[node]=visited
            order.append(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return order

        