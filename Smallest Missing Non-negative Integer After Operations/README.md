# Smallest Missing Non-negative Integer After Operations

## Problem

You are given a 0-indexed integer array `nums` and an integer `value`.

In one operation, you can add or subtract `value` from any element of `nums`.

For example, if `nums = [1,2,3]` and `value = 2`, you can choose to subtract `value` from `nums[0]` to make `nums = [-1,2,3]`.

The MEX (minimum excluded) of an array is the smallest missing non-negative integer in it.

For example, the MEX of `[-1,2,3]` is 0 while the MEX of `[1,0,3]` is 2.

Return the maximum MEX of `nums` after applying the mentioned operation any number of times.

---

**Example 1:**

```
Input: nums = [1,-10,7,13,6,8], value = 5
Output: 4
```

Explanation: One can achieve this result by applying the following operations:

* Add value to `nums[1]` twice to make `nums = [1,0,7,13,6,8]`
* Subtract value from `nums[2]` once to make `nums = [1,0,2,13,6,8]`
* Subtract value from `nums[3]` twice to make `nums = [1,0,2,3,6,8]`

The MEX of `nums` is 4. It can be shown that 4 is the maximum MEX we can achieve.

**Example 2:**

```
Input: nums = [1,-10,7,13,6,8], value = 7
Output: 2
```

Explanation: One can achieve this result by applying the operation:

* Subtract value from `nums[2]` once to make `nums = [1,-10,0,13,6,8]`

The MEX of `nums` is 2. It can be shown that 2 is the maximum MEX we can achieve.

---

**Constraints:**

* 1 <= nums.length, value <= 10⁵
* -10⁹ <= nums[i] <= 10⁹

---

## Code (Python)

```python
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        l=[0]*value
        for i in nums:
            j=i%value
            l[j]+=1
        r=0
        while l[r%value]>0:
            l[r%value]-=1
            r+=1
        return r
```

---

🧩 **How I Solved It — Step-by-Step**

1. Count the frequency of each remainder modulo `value`.
2. Track how many numbers occupy each modulo slot.
3. Start from 0 and keep incrementing until a modulo slot has no remaining number.
4. That first number with an empty slot is the maximum achievable MEX.

---

🛠️ **Possible Improvements**

* Could optimize space for extremely large `value` if constraints allow.
* Alternative approaches could simulate operations, but using modulo counting is more efficient.

---

🧠 **Time & Space Complexity**

* Time: O(n + value)
* Space: O(value)
