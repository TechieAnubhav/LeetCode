# Find Greatest Common Divisor of Array

## Problem
Given an integer array `nums`, return the greatest common divisor (GCD) of the smallest number and largest number in `nums`.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

### Examples

**Example 1:**  
Input: `nums = [2,5,6,9,10]`  
Output: `2`  
Explanation:  
The smallest number in nums is 2.  
The largest number in nums is 10.  
The greatest common divisor of 2 and 10 is 2.

**Example 2:**  
Input: `nums = [7,5,6,8,3]`  
Output: `1`  
Explanation:  
The smallest number in nums is 3.  
The largest number in nums is 8.  
The greatest common divisor of 3 and 8 is 1.

**Example 3:**  
Input: `nums = [3,3]`  
Output: `3`  
Explanation:  
The smallest number in nums is 3.  
The largest number in nums is 3.  
The greatest common divisor of 3 and 3 is 3.

### Constraints
- 2 <= nums.length <= 1000  
- 1 <= nums[i] <= 1000  

## Code
```python
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        ma = max(nums)
        mi = min(nums)
        gcd = 1
        for i in range(2, mi + 1):
            if ma % i == 0 and mi % i == 0:
                gcd = i
        return gcd
```

## 🧩 How I Solved It — Step-by-Step
1. Find the smallest (`mi`) and largest (`ma`) numbers in the array.
2. Initialize `gcd = 1` as a default.
3. Iterate from 2 to `mi` (since GCD cannot be greater than the smaller number).
4. For each number `i`, check if both `ma` and `mi` are divisible by `i`.
5. Update `gcd` whenever both are divisible.
6. Return the final `gcd` value.

## 🛠️ Possible Improvements
- Use Python’s built-in `math.gcd()` for better efficiency.  
  Example:
  ```python
  import math
  return math.gcd(min(nums), max(nums))
  ```

## 🧠 Time & Space Complexity
- **Time Complexity:** O(n), where n = min(nums). We iterate up to the smallest number.  
- **Space Complexity:** O(1), constant space used.
