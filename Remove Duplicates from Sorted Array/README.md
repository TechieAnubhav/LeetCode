# Remove Duplicates from Sorted Array

## Problem
Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.

Consider the number of unique elements of `nums` to be `k`. To get accepted, you need to do the following things:

1. Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially.  
2. The remaining elements of `nums` are not important, as well as the size of `nums`.  
3. Return `k`.  

---

## Examples

**Example 1:**
```
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
```

**Example 2:**
```
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
```

---

## Constraints
- `1 <= nums.length <= 3 * 10^4`  
- `-100 <= nums[i] <= 100`  
- `nums` is sorted in non-decreasing order.  

---

## Code
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        j=0
        for i in range(1,len(nums)):
            if nums[j] != nums[i]:
                j+=1
                nums[j]=nums[i]
        return j+1
```

---

## 🧩 How I Solved It — Step-by-Step
1. Start with two pointers: `j` (tracks position of unique elements) and `i` (scans the array).  
2. Iterate from the second element onwards.  
3. If `nums[i]` is different from `nums[j]`, move `j` forward and set `nums[j] = nums[i]`.  
4. Continue until the end of the array.  
5. The result is `j + 1` (count of unique elements).  

---

## 🛠️ Possible Improvements
- This approach is already optimal (`O(n)` time, `O(1)` space).  
- Alternative would be using Python sets, but that breaks the in-place constraint and order requirement.  

---

## 🧠 Time & S
