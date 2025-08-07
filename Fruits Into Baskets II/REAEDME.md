# 🍎 Fruits Into Baskets II

## 📝 Problem Statement

You are given two arrays of integers, `fruits` and `baskets`, each of length `n`, where:

- `fruits[i]` represents the quantity of the *i-th* type of fruit  
- `baskets[j]` represents the capacity of the *j-th* basket  

From left to right, place the fruits according to these rules:

1. Each fruit type must be placed in the **leftmost** available basket with a **capacity ≥** the quantity of that fruit.
2. Each basket can hold **only one type** of fruit.
3. If a fruit type cannot be placed in any basket, it remains **unplaced**.

Return the **number of fruit types** that remain unplaced after all possible allocations are made.

---

## 📌 Examples

### Example 1

**Input:**  
`fruits = [4,2,5]`  
`baskets = [3,5,4]`  

**Output:** `1`

**Explanation:**  
- fruits[0] = 4 → placed in baskets[1] = 5  
- fruits[1] = 2 → placed in baskets[0] = 3  
- fruits[2] = 5 → cannot be placed in baskets[2] = 4  
→ 1 fruit type remains unplaced

---

### Example 2

**Input:**  
`fruits = [3,6,1]`  
`baskets = [6,4,7]`  

**Output:** `0`

**Explanation:**  
- fruits[0] = 3 → placed in baskets[0] = 6  
- fruits[1] = 6 → placed in baskets[2] = 7 (skips basket[1])  
- fruits[2] = 1 → placed in baskets[1] = 4  
→ All fruits placed

---

## 📚 Constraints

- `n == fruits.length == baskets.length`  
- `1 <= n <= 100`  
- `1 <= fruits[i], baskets[i] <= 1000`

---

## ✅ My Solution (Python)

```python
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = 0
        for i in fruits:
            for j in baskets:
                if i <= j:
                    baskets.remove(j)
                    break
            else:
                n += 1
        return n
```



### ✅ Block 2 — Explanation, Complexity, and Improvements

```markdown
## 🧩 How I Solved It — Step-by-Step

1. **Loop Through Fruits:**  
   For each fruit type in `fruits`, check for a valid basket.

2. **Find Leftmost Valid Basket:**  
   Loop through the `baskets` list.  
   - If a basket's capacity is ≥ the fruit's quantity, use it and remove it from the list.

3. **Track Unplaced Fruits:**  
   If no valid basket is found, increment a counter.

4. **Return the Result:**  
   Return the number of unplaced fruits after going through all.

---

## 🧠 Time & Space Complexity

- **Time Complexity:** `O(n^2)`  
  For each fruit (`n`), we may search all baskets (`n`).

- **Space Complexity:** `O(1)`  
  No additional data structures used apart from basic counters.

---

## 🛠️ Possible Improvements

- Use an auxiliary boolean list or index tracking to avoid modifying the list with `remove()`, which is costly.
- Use sorting or priority queues to optimize the basket search and bring time down to `O(n log n)` in a greedy approach.

---

## 🔖 Tags

`greedy`, `arrays`, `placement`, `simulation`, `leetcode-medium`
