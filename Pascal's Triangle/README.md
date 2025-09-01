# Pascal's Triangle

## Problem
Given an integer `numRows`, return the first `numRows` of Pascal's triangle.  

In Pascal's triangle, each number is the sum of the two numbers directly above it.

---

## Examples

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

## Constraints
- 1 <= numRows <= 30

---

## Code
```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result= []
        if numRows==0:
            return result
        
        first_row=[1]
        result.append(first_row)
        for i in range(1,numRows):
            prev_row=result[i-1]
            current_row=[1]
            for j in range(1,i):
                current_row.append(prev_row[j-1] + prev_row[j])
            current_row.append(1)
            result.append(current_row)
        return result
```

---

## 🧩 How I Solved It — Step-by-Step
1. Start with an empty list `result` to store rows.  
2. Add the first row `[1]` as the base case.  
3. For each subsequent row:  
   - Begin with `1`.  
   - For each element in the middle, sum the two numbers directly above (`prev_row[j-1] + prev_row[j]`).  
   - End the row with `1`.  
4. Append each row to `result`.  
5. Return `result`.

---

## 🛠️ Possible Improvements
- The solution is already optimal, but we can reduce space if we only return the last row instead of storing all rows when required in a different variant of the problem.  
- Could also use recursion with memoization to build rows.

---

## 🧠 Time & Space Complexity
- **Time Complexity:** O(numRows²), since each row computation depends on all previous rows.  
- **Space Complexity:** O(numRows²), because we store the entire triangle in memory.  
