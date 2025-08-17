# Plus One

## Problem
You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the ith digit of the integer.  
The digits are ordered from most significant to least significant in left-to-right order.  
The large integer does not contain any leading `0`s.  

Increment the large integer by one and return the resulting array of digits.

---

**Example 1:**
```
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
```

**Example 2:**
```
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
```

**Example 3:**
```
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
```

---

**Constraints:**
- 1 <= digits.length <= 100  
- 0 <= digits[i] <= 9  
- digits does not contain any leading 0's.  

---

## Code
```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = int("".join(map(str, digits)))
        a += 1
        return [int(ch) for ch in str(a)]
```

---

🧩 **How I Solved It — Step-by-Step**  
1. Convert the digit list into a string.  
2. Convert that string into an integer.  
3. Increment the integer by 1.  
4. Convert the new integer back into a string.  
5. Convert each character of that string back into an integer.  
6. Return the new list of digits.  

---

🛠️ **Possible Improvements**  
- Instead of converting to int and back, we can handle carry manually to avoid very large number conversions.  
- This is useful if digits.length becomes extremely large (thousands or millions).  

---

🧠 **Time & Space Complexity**  
- **Time Complexity:** O(n) — where n is the number of digits (due to string and list conversions).  
- **Space Complexity:** O(n) — for storing the new list of digits.  
