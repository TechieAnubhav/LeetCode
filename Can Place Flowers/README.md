# Can Place Flowers

## Problem
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

---

**Example 1:**
```
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
```

**Example 2:**
```
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
```

---

**Constraints:**
- 1 <= flowerbed.length <= 2 * 10⁴
- flowerbed[i] is 0 or 1.
- There are no two adjacent flowers in flowerbed.
- 0 <= n <= flowerbed.length

---

## Code (Python)
```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if flowerbed==[0] and n<=1:
            return True
        c=0
        for i in range(len(flowerbed)):
            if flowerbed[i]==0 and i!=0 and i!=len(flowerbed)-1 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                c+=1
            elif i==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                c+=1
            elif i==len(flowerbed)-1 and flowerbed[i]==0 and flowerbed[i-1]==0:
                flowerbed[i]=1
                c+=1
        return c==n or c>n
```

---

🧩 **How I Solved It — Step-by-Step**
1. Traverse through the flowerbed list.
2. Check each position to see if a flower can be placed (both adjacent plots are empty).
3. Handle special cases for the first and last plot.
4. Keep count of flowers placed and return True if `c >= n`.

---

🛠️ **Possible Improvements**
- Use an optimized approach with early exit if `c >= n` to reduce unnecessary iterations.
- Can handle edge cases like empty flowerbed or single element more elegantly.

---

🧠 **Time & Space Complexity**
- **Time Complexity:** O(n) — single pass through the array.
- **Space Complexity:** O(1) — constant space used.
