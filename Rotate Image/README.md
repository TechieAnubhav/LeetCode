# Rotate Image

## Problem
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

---

## Examples

### Example 1
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]  
Output: [[7,4,1],[8,5,2],[9,6,3]]  

### Example 2
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]  
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]  

---

## Constraints
- n == matrix.length == matrix[i].length  
- 1 <= n <= 20  
- -1000 <= matrix[i][j] <= 1000  

---

## Code
```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        '''
        Do not return anything, modify matrix in-place instead.
        '''
        n = len(matrix)
        i = 0
        j = i + 1
        while i < n - 1:
            for m in range(i + 1, n):
                matrix[i][m], matrix[m][i] = matrix[m][i], matrix[i][m]
            i += 1
            j = i + 1
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
```

---

## 🧩 How I Solved It — Step-by-Step
1. First, I transposed the matrix (swap matrix[i][j] with matrix[j][i]).  
2. After transposing, I reversed each row.  
3. Transpose + Reverse Rows = 90° clockwise rotation.  
4. All operations were done in-place to satisfy the constraint.

---

## 🛠️ Possible Improvements
- The transpose loop can be simplified using nested for-loops instead of a while-loop.
- Code readability can be improved by separating transpose and reverse into clear blocks.

---

## 🧠 Time & Space Complexity
- **Time Complexity:** O(n²) — Every element is visited during transpose and reverse.
- **Space Complexity:** O(1) — In-place modification.
