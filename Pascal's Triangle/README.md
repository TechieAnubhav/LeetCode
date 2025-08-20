# Pascal's Triangle

## Problem
Given an integer `numRows`, return the first `numRows` of Pascal's triangle.  

In Pascal's triangle, each number is the sum of the two numbers directly above it.

---

**Example 1:**
```
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```

**Example 2:**
```
Input: numRows = 1
Output: [[1]]
```

---

**Constraints:**
- 1 <= numRows <= 30  

---

## Code
```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        
        for i in range(1, numRows):
            prev = triangle[-1]
            row = [1]
            
            for j in range(1, len(prev)):
                row.append(prev[j-1] + prev[j])
            
            row.append(1)
            triangle.append(row)
        
        return triangle
```

---

🧩 **How I Solved It — Step-by-Step**  
1. Start with the first row `[1]`.  
2. For each new row, begin and end with `1`.  
3. Each middle element is the sum of the two numbers directly above it.  
4. Repeat until `numRows` rows are built.  

---

🛠️ **Possible Improvements**  
- If only the *n-th row* is needed, we can compute it directly using binomial coefficients instead of building the entire triangle.  
- For memory optimization, we could generate only the previous row and current row instead of storing the whole triangle.  

---

🧠 **Time & Space Complexity**  
- **Time Complexity:** O(numRows²) — since each row is built by summing up elements from the previous row.  
- **Space Complexity:** O(numRows²) — storing the entire triangle.  
