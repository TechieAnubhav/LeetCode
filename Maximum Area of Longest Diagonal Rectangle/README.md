# Maximum Area of Longest Diagonal Rectangle

## Problem
You are given a 2D 0-indexed integer array `dimensions`.

For all indices `i`, `0 <= i < dimensions.length`, `dimensions[i][0]` represents the length and `dimensions[i][1]` represents the width of the rectangle `i`.

Return the area of the rectangle having the longest diagonal. If there are multiple rectangles with the longest diagonal, return the area of the rectangle having the maximum area.

---

## Examples

**Example 1:**
```
Input: dimensions = [[9,3],[8,6]]
Output: 48
```

**Example 2:**
```
Input: dimensions = [[3,4],[4,3]]
Output: 12
```

---

## Constraints
- `1 <= dimensions.length <= 100`
- `dimensions[i].length == 2`
- `1 <= dimensions[i][0], dimensions[i][1] <= 100`

---

## Code
```python
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        a=0
        d=0
        for i in dimensions:
            t=((i[0]**2)+(i[1]**2))**(1/2)
            if d==t:
                if a<i[0]*i[1]:
                    a=i[0]*i[1]
                    d=t
            elif d<t:
                d=t
                a=i[0]*i[1]
        return a
```

---

## 🧩 How I Solved It — Step-by-Step
1. Start with variables `a` (max area) and `d` (max diagonal).  
2. Loop through each rectangle.  
3. Compute diagonal as `sqrt(l² + w²)`.  
4. If diagonal is bigger, update both `d` and `a`.  
5. If diagonal is equal, update only if the new area is larger.  
6. Return `a`.

---

## 🛠️ Possible Improvements
- Compare squared diagonals (`l² + w²`) instead of actual square roots for efficiency and precision.  

---

## 🧠 Time & Space Complexity
- **Time Complexity:** `O(n)` — iterate over rectangles once.  
- **Space Complexity:** `O(1)` — only a few variables used.  
