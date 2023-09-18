class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        count = []
        for i, row in enumerate(mat):
            count.append((row.count(1), i))
        
        count.sort(key=lambda x: (x[0], x[1]))
        return [i[1] for i in count[:k]]