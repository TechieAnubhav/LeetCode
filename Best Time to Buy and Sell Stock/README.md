# Best Time to Buy and Sell Stock

## Problem
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i-th` day.  

You want to maximize your profit by choosing **one day to buy** and **a later day to sell**.  

Return the maximum profit you can achieve. If no profit is possible, return `0`.

---

## Examples

**Example 1:**
```
Input: prices = [7,1,5,3,6,4]
Output: 5
```
**Explanation:**  
Buy on day 2 (price = 1), sell on day 5 (price = 6).  
Profit = 6 - 1 = 5.

---

**Example 2:**
```
Input: prices = [7,6,4,3,1]
Output: 0
```
**Explanation:**  
No profitable transactions can be made.  

---

## Constraints
- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

---

## Code
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            profit = max(profit, prices[i] - buy)
        return profit
```

---

## 🧩 How I Solved It — Step-by-Step
1. Initialize `buy` with the first price and `profit` as 0.
2. Traverse the list:
   - Update `buy` if a smaller price is found.
   - Update `profit` if the current price - `buy` is greater than the current max.
3. Return the maximum profit found.

---

## 🛠️ Possible Improvements
- This solution is already optimal (O(n), O(1)).
- Could add extra checks for empty input (not needed due to constraints).
- Could extend to **multiple transactions** if problem changes.

---

## 🧠 Time & Space Complexity
- **Time Complexity:** O(n) — single pass over the array.  
- **Space Complexity:** O(1) — only two variables (`buy`, `profit`) are maintained.  
