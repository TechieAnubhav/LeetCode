# Container With Most Water

## Problem
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`-th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

**Note:** You may not slant the container.

---

## Examples

**Example 1:**
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
```
**Explanation:**  
The container formed by lines at positions 1 and 8 holds the maximum amount of water, which is 49.

**Example 2:**
```
Input: height = [1,1]
Output: 1
```
**Explanation:**  
The container formed by the first and last line holds 1 unit of water.

---

## Constraints

- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

---

## Code
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxarea = 0

        while left < right:
            currarea = min(height[left], height[right]) * (right - left)
            maxarea = max(currarea, maxarea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxarea
```

---

## 🧩 How I Solved It — Step-by-Step
1. Initialized two pointers: `left` at the beginning and `right` at the end of the array.
2. Calculated the area between the two lines at the `left` and `right` positions.
3. Updated the `maxarea` with the larger of the current area and the previously stored maximum.
4. Moved the pointer pointing to the shorter line inward to try and find a larger area.
5. Continued until the two pointers meet.
6. Returned the largest area found.

---

## 🛠️ Possible Improvements
- The two-pointer approach is already optimal with O(n) time complexity.
- Edge cases where all heights are the same or very small can be further tested.

---

## 🧠 Time & Space Complexity
- **Time Complexity:** O(n), because each element is processed at most once.
- **Space Complexity:** O(1), since only a few extra variables are used.
