
# Water Bottles II

## Problem
You are given two integers `numBottles` and `numExchange`.

- `numBottles` represents the number of full water bottles that you initially have.  
- In one operation, you can perform one of the following operations:
  1. Drink any number of full water bottles turning them into empty bottles.
  2. Exchange `numExchange` empty bottles with one full water bottle. Then, increase `numExchange` by one.

**Note:** You cannot exchange multiple batches of empty bottles for the same value of `numExchange`. For example, if `numBottles == 3` and `numExchange == 1`, you cannot exchange 3 empty water bottles for 3 full bottles.

Return the maximum number of water bottles you can drink.

---

**Example 1:**
```
Input: numBottles = 13, numExchange = 6
Output: 15
```

**Example 2:**
```
Input: numBottles = 10, numExchange = 3
Output: 13
```

---

**Constraints:**
- 1 <= numBottles <= 100  
- 1 <= numExchange <= 100  

---

## Code (Python)
```python
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        s = 0
        e = 0
        while numBottles > 0:
            e += numBottles
            s += numBottles
            numBottles = 0
            if e >= numExchange:
                e -= numExchange
                numExchange += 1
                numBottles += 1
        return s
```

---

🧩 **How I Solved It — Step-by-Step**  
1. Initialize `s` (bottles drunk) and `e` (empty bottles) as 0.  
2. While there are full bottles (`numBottles > 0`):  
   - Drink all full bottles: add to `s` and `e`.  
   - Set `numBottles = 0`.  
   - If `e >= numExchange`, exchange empty bottles for a full bottle:  
     - Reduce `e` by `numExchange`.  
     - Increment `numExchange` by 1.  
     - Increment `numBottles` by 1.  
3. Repeat until no more exchanges or full bottles are left.  

---

🛠️ **Possible Improvements**  
- Pre-calculate total exchanges for small numbers to avoid iterative loops.  
- Handle cases where `numExchange` starts greater than `numBottles`.  

---

🧠 **Time & Space Complexity**  
- Time: O(numBottles + numExchange) — each bottle processed at most once.  
- Space: O(1) — only integers used, no extra data structures.  
