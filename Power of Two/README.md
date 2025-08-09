# Power of Two

## Problem Statement
Given an integer *n*, return **true** if it is a power of two; otherwise, return **false**. An integer *n* is a power of two if there exists an integer *x* such that `n == 2^x`:contentReference[oaicite:0]{index=0}. In other words, check whether *n* can be expressed as 2 raised to some integer exponent.

## Examples
- Input: `n = 1`  
  Output: `true`  
  Explanation: 2^0 = 1:contentReference[oaicite:1]{index=1}.
- Input: `n = 16`  
  Output: `true`  
  Explanation: 2^4 = 16:contentReference[oaicite:2]{index=2}.
- Input: `n = 3`  
  Output: `false`  
  Explanation: 3 is not a power of two:contentReference[oaicite:3]{index=3}.

## Constraints
- `-2^31 <= n <= 2^31 - 1`:contentReference[oaicite:4]{index=4}.

## My Solution

    class Solution:
        def isPowerOfTwo(self, n: int) -> bool:
            return n > 0 and not (n & (n - 1))

## 🧩 How I Solved It — Step-by-Step
- **Check if `n > 0`:** Only positive integers can be powers of two:contentReference[oaicite:5]{index=5}.
- **Bitwise AND trick:** Compute `n & (n - 1)`. For powers of two, this yields 0, since in binary a power of two has exactly one `1` bit (e.g., `4` is `100` in binary, `4-1 = 3` is `011`), and `100 & 011 = 000`:contentReference[oaicite:6]{index=6}.
- The function returns **true** only if both conditions are satisfied (`n > 0` and `n & (n - 1) == 0`).

## 🧠 Time & Space Complexity
- **Time Complexity:** O(1), since the bitwise AND and comparison operations run in constant time:contentReference[oaicite:7]{index=7}.
- **Space Complexity:** O(1), because we only use a fixed amount of extra space:contentReference[oaicite:8]{index=8}.

## 🛠️ Possible Improvements
- The bitwise solution is already optimal in time and space. We could add input validation (e.g., check if the input is an integer) for robustness.
- An alternative approach (less efficient) in Python is to check if `bin(n).count('1') == 1` when `n > 0`.
- We could also include explanatory comments or docstrings for clarity, or handle edge cases explicitly in languages where integer bounds differ.
