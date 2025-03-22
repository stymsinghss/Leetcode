import collections
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        graph = collections.defaultdict(list)
        visited = set()

        # Create adjacency list from adj matrix
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1 and i != j:
                    graph[i].append(j)

        # Check
        for i in range(len(isConnected)):
            if i not in visited:
                provinces += 1
                self.dfs(graph, i, visited)

        return provinces

    def dfs(self, graph, node, visited):
        visited.add(node)

        for neigh in graph[node]:
            if neigh not in visited:
                self.dfs(graph, neigh, visited)
