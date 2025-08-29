# Summary Ranges

## Problem  
You are given a sorted unique integer array `nums`.

A range `[a,b]` is the set of all integers from `a` to `b` (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of `nums` is covered by exactly one of the ranges, and there is no integer `x` such that `x` is in one of the ranges but not in `nums`.

Each range `[a,b]` in the list should be output as:

- `"a->b"` if `a != b`  
- `"a"` if `a == b`  

---

## Examples

**Example 1:**
```
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
```

**Example 2:**
```
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
```

---

## Constraints
- `0 <= nums.length <= 20`
- `-2^31 <= nums[i] <= 2^31 - 1`
- All the values of `nums` are unique.
- `nums` is sorted in ascending order.

---

## Code
```python
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l=[]
        m=[]
        for i in range(len(nums)):
            if len(l)>0 and nums[i]!=l[-1]+1:
                if len(l)==1:
                    m.append(f"{l[0]}")
                    l.clear()
                else:
                    m.append(f"{l[0]}->{l[-1]}")
                    l.clear()
            l.append(nums[i])
        if len(l)==1:
            m.append(f"{l[0]}")
        elif len(l)>1:
            m.append(f"{l[0]}->{l[-1]}")
        return m
```

---

## 🧩 How I Solved It — Step-by-Step
1. Created a temporary list `l` to track the current range.  
2. Iterated through `nums`, and checked if the current number continues the sequence (`nums[i] == l[-1] + 1`).  
3. If not, closed the current range and added it to the result list `m` (single number `"a"` or range `"a->b"`).  
4. Cleared `l` and started a new range with the current number.  
5. After the loop, appended the last remaining range to the result.  

---

## 🛠️ Possible Improvements
- Instead of using `l.clear()` and appending repeatedly, use two pointers (`start` and `end`) to make the code cleaner.  
- Directly build strings without maintaining an extra list for the current range.  

---

## 🧠 Time & Space Complexity
- **Time Complexity:** `O(n)` — Each element is visited once.  
- **Space Complexity:** `O(1)` extra space (output list not counted).  
