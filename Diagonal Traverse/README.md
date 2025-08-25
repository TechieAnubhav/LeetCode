# Diagonal Traverse

## Problem
Given an `m x n` matrix `mat`, return an array of all the elements of the array in a diagonal order.

---

**Example 1:**
```
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
```

**Example 2:**
```
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
```

---

**Constraints:**
- m == mat.length  
- n == mat[i].length  
- 1 <= m, n <= 10⁴  
- 1 <= m * n <= 10⁴  
- -10⁵ <= mat[i][j] <= 10⁵  

---

## Code
```python
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        result = []
        row = col = 0

        for _ in range(m * n):
            result.append(mat[row][col])

            if (row + col) % 2 == 0:  # moving up-right
                if col == n - 1:
                    row += 1
                elif row == 0:
                    col += 1
                else:
                    row -= 1
                    col += 1
            else:  # moving down-left
                if row == m - 1:
                    col += 1
                elif col == 0:
                    row += 1
                else:
                    row += 1
                    col -= 1

        return result
```

---

🧩 **How I Solved It — Step-by-Step**  
1. Start from `mat[0][0]`.  
2. Traverse diagonals alternately:  
   - If `(row+col)` is even → move up-right.  
   - Else → move down-left.  
3. Handle boundary conditions:  
   - If at last column → move down.  
   - If at first row → move right.  
   - If at last row → move right.  
   - If at first column → move down.  
4. Collect all elements until `m*n` elements are added.  

---

🛠️ **Possible Improvements**  
- Could use a **hash map of diagonals** (`row+col` as key, append elements) and then reverse alternating diagonals.  
  - Simpler to implement but uses **extra space**.  
- Current pointer approach is **space-optimal**.  

---

🧠 **Time & Space Complexity**  
- Time: **O(m * n)** (each element is visited once).  
- Space: **O(1)** extra (ignoring output array).  
