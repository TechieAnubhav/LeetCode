# Final Value of Variable After Performing Operations

## Problem
There is a programming language with only four operations and one variable `X`:

- `++X` and `X++` increments the value of the variable `X` by 1.
- `--X` and `X--` decrements the value of the variable `X` by 1.

Initially, the value of `X` is 0.

Given an array of strings `operations` containing a list of operations, return the final value of `X` after performing all the operations.

### Example 1:
**Input:** `operations = ["--X","X++","X++"]`  
**Output:** `1`

### Example 2:
**Input:** `operations = ["++X","++X","X++"]`  
**Output:** `3`

### Example 3:
**Input:** `operations = ["X++","++X","--X","X--"]`  
**Output:** `0`

### Constraints:
- 1 <= operations.length <= 100  
- operations[i] will be either `"++X"`, `"X++"`, `"--X"`, or `"X--"`

## Code
```python
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for i in operations:
            if i in "--XX--":
                x -= 1
            elif i in "++XX++":
                x += 1
        return x
```

## 🧩 How I Solved It — Step-by-Step
1. Initialize a variable `x` as 0.
2. Loop through all operations.
3. If the operation contains `"--"`, decrement `x` by 1.
4. If the operation contains `"++"`, increment `x` by 1.
5. Return the final value of `x`.

## 🛠️ Possible Improvements
- Use a cleaner condition like `if '+' in i:` instead of string containment logic for clarity.
- Add input validation for better robustness.

## 🧠 Time & Space Complexity
- **Time Complexity:** O(n), where n is the length of operations.
- **Space Complexity:** O(1)
