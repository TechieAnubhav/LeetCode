# Largest Triangle Area

## Problem
Given an array of points on the X-Y plane `points` where `points[i] = [xi, yi]`, return the area of the largest triangle that can be formed by any three different points.  

Answers within `10^-5` of the actual answer will be accepted.

## Examples
**Example 1:**
```
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.00000
Explanation: The five points are shown in the above figure. The red triangle is the largest.
```

**Example 2:**
```
Input: points = [[1,0],[0,0],[0,1]]
Output: 0.50000
```

## Constraints
- 3 <= points.length <= 50  
- -50 <= xi, yi <= 50  
- All the given points are unique  

## Code
```python
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        a = 0
        for i in range(len(points)):
            for j in range(i, len(points)):
                for k in range(j, len(points)):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    area = abs(0.5 * (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)))
                    a = max(a, area)
        return a
```

## 🧩 How I Solved It — Step-by-Step
1. A triangle’s area from three points `(x1,y1), (x2,y2), (x3,y3)` can be found using the **shoelace formula**.  
   ```
   Area = | 0.5 * (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) |
   ```
2. Iterate through **all possible triplets of points**.  
3. For each triplet, compute the area.  
4. Keep track of the **maximum area** encountered.  
5. Return the largest area.  

## 🛠️ Possible Improvements
- Instead of manually unpacking x/y separately, Python tuple unpacking (`x1,y1 = points[i]`) makes code cleaner.  
- For larger constraints, optimization using convex hull could be applied, but unnecessary here since max n=50.  

## 🧠 Time & Space Complexity
- **Time Complexity:** O(n³), since we check all combinations of 3 points. With n ≤ 50, this is efficient enough.  
- **Space Complexity:** O(1), only variables are used.  
