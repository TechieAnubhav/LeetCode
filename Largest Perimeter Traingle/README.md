# Largest Perimeter Triangle

## Problem
Given an integer array `nums`, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths.  
If it is impossible to form any triangle of a non-zero area, return `0`.

## Examples
**Example 1:**
```
Input: nums = [2,1,2]
Output: 5
Explanation: You can form a triangle with three side lengths: 1, 2, and 2.
```

**Example 2:**
```
Input: nums = [1,2,1,10]
Output: 0
Explanation: No valid triangle can be formed.
```

## Constraints
- 3 <= nums.length <= 10⁴  
- 1 <= nums[i] <= 10⁶  

## Code
```python
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i+1] + nums[i+2] > nums[i]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0
```

## 🧩 How I Solved It — Step-by-Step
1. **Triangle condition**: A triangle is valid if the sum of the two smaller sides is greater than the largest side.  
2. Sort the array in **descending order** so the largest side is always `nums[i]`.  
3. Iterate through the array and check the **triangle inequality** for each triplet.  
4. Return the **first valid perimeter** found (this is guaranteed to be the largest because of descending sort).  
5. If no valid triangle exists, return `0`.  

## 🛠️ Possible Improvements
- Could also sort in ascending order and check from the end, but descending makes it slightly more direct.  
- Early return ensures efficient performance, no need to check all triplets once a valid one is found.  

## 🧠 Time & Space Complexity
- **Time Complexity:** O(n log n) for sorting + O(n) for iteration → O(n log n).  
- **Space Complexity:** O(1), only variables used.  
