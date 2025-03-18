from collections import deque
from typing import List

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        # if n == 1, return 0 only one node
        if n == 1:
            return 0
        
        final_mask = (1 << n) - 1
        queue = deque()

        visited = [[False] * (1 << n) for _ in range(n)]
        # start from every node
        for i in range(n):
            mask = 1 << i
            queue.append((i, mask, 0))
            visited[i][mask] = True
        # BFS search
        while queue:
            node, mask, dist = queue.popleft()
            if mask == final_mask:
                return dist
            # check all the neighbors
            for neighbor in graph[node]:
                new_mask = mask | (1 << neighbor)
                if not visited[neighbor][new_mask]:
                    visited[neighbor][new_mask] = True
                    queue.append((neighbor, new_mask, dist + 1))
        # if no path found (for prortection)
        return -1
    
if __name__ == "__main__":
    graph = [[1,2,3],[0],[0],[0]]
    print(Solution().shortestPathLength(graph))