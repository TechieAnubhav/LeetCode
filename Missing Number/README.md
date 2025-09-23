# Missing Number

## Problem
You are given an array `nums` containing `n` distinct numbers in the range `[0, n]`.  
Return the only number in the range that is missing from the array.

## Examples

### Example 1
Input: `nums = [3,0,1]`  
Output: `2`  
Explanation:  
- `n = 3`, so numbers should be `[0,1,2,3]`.  
- `2` is missing.  

### Example 2
Input: `nums = [0,1]`  
Output: `2`  
Explanation:  
- `n = 2`, so numbers should be `[0,1,2]`.  
- `2` is missing.  

### Example 3
Input: `nums = [9,6,4,2,3,5,7,0,1]`  
Output: `8`  
Explanation:  
- `n = 9`, so numbers should be `[0,1,2,3,4,5,6,7,8,9]`.  
- `8` is missing.  

## Constraints
- n == nums.length  
- 1 <= n <= 10⁴  
- 0 <= nums[i] <= n  
- All numbers in `nums` are unique  

## Code
```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set(nums)
        for i in range(len(nums) + 1):
            if i not in s:
                return i
```

## 🧩 How I Solved It — Step-by-Step
1. Converted the input list `nums` into a set `s` for O(1) lookups.  
2. Iterated from `0` to `n` (`len(nums)` inclusive).  
3. Returned the first number not present in the set.  

## 🛠️ Possible Improvements
- Use the **Gauss sum formula**:  
  ```python
  return n*(n+1)//2 - sum(nums)
  ```  
  This is faster and uses O(1) extra space.  

- XOR method is also possible for O(1) space without risk of overflow.  

## 🧠 Time & Space Complexity
- **Current Solution:**  
  - Time Complexity: O(n) (iteration + set lookup).  
  - Space Complexity: O(n) (set storage).  

- **Gauss Formula / XOR Solution:**  
  - Time Complexity: O(n).  
  - Space Complexity: O(1).  
