# Water Bottles

## Problem

There are `numBottles` water bottles that are initially full of water. You can exchange `numExchange` empty water bottles from the market with one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Given the two integers `numBottles` and `numExchange`, return the maximum number of water bottles you can drink.

## Examples

**Example 1:**

```
Input: numBottles = 9, numExchange = 3
Output: 13
Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 9 + 3 + 1 = 13.
```

**Example 2:**

```
Input: numBottles = 15, numExchange = 4
Output: 19
Explanation: You can exchange 4 empty bottles to get 1 full water bottle. 
Number of water bottles you can drink: 15 + 3 + 1 = 19.
```

## Constraints

* 1 <= numBottles <= 100
* 2 <= numExchange <= 100

## Code

```python
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles - 1) // (numExchange - 1)
```

## 🧩 How I Solved It — Step-by-Step

1. Start with `numBottles` as the initial count of bottles drunk.
2. Every time you drink a bottle, it turns into an empty one.
3. To maximize drinking, exchange empty bottles for new ones.
4. Each exchange requires `numExchange` empty bottles, meaning for every `(numExchange - 1)` bottles, you effectively gain 1 extra drink.
5. The formula simplifies to:

   ```
   total = numBottles + (numBottles - 1) // (numExchange - 1)
   ```
6. Return this total as the final answer.

## 🛠️ Possible Improvements

* The current formula is optimal and direct.
* Alternatively, simulate the process with a while loop to make the logic more explicit, but it would be less efficient.

## 🧠 Time & Space Complexity

* **Time Complexity:** `O(1)` — direct calculation without loops.
* **Space Complexity:** `O(1)` — no extra storage used.
