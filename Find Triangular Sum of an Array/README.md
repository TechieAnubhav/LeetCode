# Find Triangular Sum of an Array

## Problem
You are given a 0-indexed integer array `nums`, where `nums[i]` is a digit between `0` and `9` (inclusive).  

The triangular sum of `nums` is the value of the only element present in `nums` after repeatedly performing this process:

1. If `n == 1`, end the process.  
2. Otherwise, create a new array `newNums` of length `n - 1`.  
3. For each index `i` (0 ≤ i < n - 1), set  
   `newNums[i] = (nums[i] + nums[i+1]) % 10`.  
4. Replace `nums` with `newNums` and repeat.  

Return the triangular sum of `nums`.

## Examples
**Example 1:**
```
Input: nums = [1,2,3,4,5]
Output: 8
Explanation:
[1,2,3,4,5] → [3,5,7,9] → [8,2,6] → [0,8] → [8]
```

**Example 2:**
```
Input: nums = [5]
Output: 5
```

## Constraints
- 1 <= nums.length <= 1000  
- 0 <= nums[i] <= 9  

## Code
```python
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) != 1:
            new = []
            for i in range(len(nums) - 1):
                new.append((nums[i] + nums[i+1]) % 10)
            nums = new
        return nums[0]
```

## 🧩 How I Solved It — Step-by-Step
1. While the array has more than one element, build the next row (`newNums`).  
2. Each new element is formed by `(nums[i] + nums[i+1]) % 10`.  
3. Replace `nums` with `newNums`.  
4. Once only one number remains, return it.  

## 🛠️ Possible Improvements
- This solution simulates the process directly, which is fine for `n <= 1000`.  
- For optimization, we could use **binomial coefficients** (`nCr`) modulo 10 to compute the final triangular sum in O(n) without repeatedly building arrays.  

## 🧠 Time & Space Complexity
- **Time Complexity:** O(n²), since we shrink the array step by step.  
- **Space Complexity:** O(n), due to storing intermediate arrays.  
