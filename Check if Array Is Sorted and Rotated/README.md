# Check if Array Is Sorted and Rotated

## Problem
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.

### Example 1:
Input: nums = [3,4,5,1,2]  
Output: true  
Explanation: [1,2,3,4,5] is the original sorted array. You can rotate the array by x = 2 positions to begin on the element of value 3: [3,4,5,1,2].

### Example 2:
Input: nums = [2,1,3,4]  
Output: false  
Explanation: There is no sorted array once rotated that can make nums.

### Example 3:
Input: nums = [1,2,3]  
Output: true  
Explanation: [1,2,3] is the original sorted array. You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.

## Constraints
1 <= nums.length <= 100  
1 <= nums[i] <= 100

```python
class Solution:
    def check(self, nums: List[int]) -> bool:
        c=0
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                c+=1
        if nums[-1]>nums[0]:
            c+=1
        return c<=1
```

## 🧩 How I Solved It — Step-by-Step
1. Count the number of times the array decreases (`nums[i] < nums[i-1]`).
2. If it decreases more than once, it's not sorted and rotated.
3. Additionally, check if the last element is greater than the first; that’s an extra rotation check.
4. Return `True` only if the count is ≤ 1.

## 🛠️ Possible Improvements
- Could optimize by using early termination once `c > 1`.
- Alternatively, verify using array sorting + rotation simulation for clarity in interviews.

## 🧠 Time & Space Complexity
- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)
