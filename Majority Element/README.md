# Majority Element

## Problem
Given an array `nums` of size `n`, return the majority element.  
The majority element is the element that appears more than ⌊n / 2⌋ times.  
You may assume that the majority element always exists in the array.

---

**Example 1:**
```
Input: nums = [3,2,3]
Output: 3
```

**Example 2:**
```
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

---

**Constraints:**
- n == nums.length  
- 1 <= n <= 5 * 10⁴  
- -10⁹ <= nums[i] <= 10⁹  

---

## Code
```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
```

---

🧩 **How I Solved It — Step-by-Step**  
1. Initialize a `candidate` and a counter.  
2. Traverse the array.  
3. If counter is `0`, pick current number as the candidate.  
4. Increase counter if number == candidate, otherwise decrease it.  
5. At the end, candidate is the majority element.  

---

🛠️ **Possible Improvements**  
- Sorting + returning `nums[n//2]` (your approach) is simpler but **O(n log n)**.  
- Using a hashmap (Counter) also works but uses **O(n)** space.  
- Boyer-Moore is best with **O(n)** time and **O(1)** space.  

---

🧠 **Time & Space Complexity**  
- **Boyer-Moore Voting Algorithm:**  
  - Time: O(n)  
  - Space: O(1)  
- **Sorting approach:**  
  - Time: O(n log n)  
  - Space: O(1)  
