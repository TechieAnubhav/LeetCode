# Distribute Candies

## Problem
Alice has `n` candies, where the ith candy is of type `candyType[i]`.  
The doctor advised Alice to only eat `n / 2` of the candies (n is always even).  
Alice wants to maximize the number of different types of candies she eats while following the doctor's advice.

Return the maximum number of different types of candies she can eat if she only eats `n / 2` of them.

## Examples
**Example 1:**
```
Input: candyType = [1,1,2,2,3,3]
Output: 3
Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.
```

**Example 2:**
```
Input: candyType = [1,1,2,3]
Output: 2
Explanation: Alice can only eat 4 / 2 = 2 candies. Whether she eats types [1,2], [1,3], or [2,3], she still can only eat 2 different types.
```

**Example 3:**
```
Input: candyType = [6,6,6,6]
Output: 1
Explanation: Alice can only eat 4 / 2 = 2 candies. Even though she can eat 2 candies, she only has 1 type.
```

## Constraints
- n == candyType.length  
- 2 <= n <= 10^4  
- n is even  
- -10^5 <= candyType[i] <= 10^5  

## Code
```python
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType) // 2
        s = set(candyType)
        if n >= len(s):
            return len(s)
        else:
            return n
```

## 🧩 How I Solved It — Step-by-Step
1. Alice can eat only `n/2` candies.  
2. Count how many unique types exist using a set.  
3. If the number of unique types is **less than or equal** to `n/2`, then Alice can eat all types.  
4. Otherwise, she can only eat `n/2` unique types.  

## 🛠️ Possible Improvements
- Simplify the return statement with `min(len(s), n)`:
```python
return min(len(set(candyType)), len(candyType)//2)
```

## 🧠 Time & Space Complexity
- **Time Complexity:** O(n) — building the set takes linear time.  
- **Space Complexity:** O(n) — for storing unique types.  
