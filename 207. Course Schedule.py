import collections
from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        indegree = [0]*numCourses

        for end,start in prerequisites:
            graph[end].append(start)
            indegree[start] += 1

        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        courses = 0
        while q:
            node = q.popleft()
            courses += 1
            for neigh in graph[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)

        return courses == numCourses
