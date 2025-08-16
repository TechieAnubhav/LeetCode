# Maximum 69 Number

## Problem
You are given a positive integer `num` consisting only of digits `6` and `9`.  

Return the maximum number you can get by changing **at most one digit** (`6` becomes `9`, and `9` becomes `6`).

---

**Example 1:**
```
Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.
```

**Example 2:**
```
Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.
```

**Example 3:**
```
Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.
```

---

**Constraints:**
- 1 <= num <= 10⁴
- num consists of only 6 and 9 digits.

---

## Code
```python
class Solution:
    def maximum69Number (self, num: int) -> int:
        m = num
        l = list(str(num))
        for i in range(len(l)):
            if l[i] == "6":
                l[i] = "9"
                m = int("".join(l))
                print(m)
                break
        return m
```

---

🧩 **How I Solved It — Step-by-Step**  
1. Convert the number into a list of its digits.  
2. Traverse the list from left to right.  
3. On the first occurrence of `6`, change it to `9`.  
4. Convert the updated list back to an integer.  
5. Break the loop since only one change is allowed.  
6. Return the resulting number.

---

🛠️ **Possible Improvements**  
- Remove the `print(m)` statement (debugging output not needed).  
- Directly replace the first `6` in the string using `str.replace("6", "9", 1)` for a cleaner solution.  
- This avoids manual looping and conversions.

---

🧠 **Time & Space Complexity**  
- **Time Complexity:** O(d) — where `d` is the number of digits (at most 4, constant time).  
- **Space Complexity:** O(d) — for storing digits as a list.
