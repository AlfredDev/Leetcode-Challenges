from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        
        for i in range(numRows):
            lis  = []
            lis.append(1)

            for j in range(1 , i):
                val = triangle[i - 1][j - 1] + triangle[i - 1][j]
                lis.append(val)
            
            if i > 0:
                lis.append(1)
            triangle.append(lis)
        return triangle
    

