import heapq
class Solution:
    def KweakestRows(self, matrix: list[list[int]], k: int) -> list[int]:
        min_heap = []
        for i, row in enumerate(matrix):
            soldiers_count = 0
            for j in range(len(row)):
                if row[j] == 1:
                    soldiers_count += 1
                else:
                    break 
            heapq.heappush(min_heap, (soldiers_count, i)) 
        weakest_rows = [heapq.heappop(min_heap)[1] for _ in range(k)]
        
        return weakest_rows

sol = Solution()
matrix = [
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1]
]
k = 3
print(sol.KweakestRows(matrix, k))