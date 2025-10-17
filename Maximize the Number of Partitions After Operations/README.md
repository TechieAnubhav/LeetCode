# Maximize the Number of Partitions After Operations

## Problem

You are given a string `s` and an integer `k`.

First, you are allowed to change at most one index in `s` to another lowercase English letter.

After that, do the following partitioning operation until `s` is empty:

Choose the longest prefix of `s` containing at most `k` distinct characters.
Delete the prefix from `s` and increase the number of partitions by one. The remaining characters (if any) in `s` maintain their initial order.

Return an integer denoting the maximum number of resulting partitions after the operations by optimally choosing at most one index to change.

### Example 1

**Input:** `s = "accca", k = 2`
**Output:** `3`
**Explanation:**

The optimal way is to change `s[2]` to something other than `a` and `c`, for example, `b`. Then it becomes `"acbca"`.

Performing the operations:

* The longest prefix with at most 2 distinct characters is `"ac"`, remove it → `s = "bca"`.
* The next longest prefix with at most 2 distinct characters is `"bc"`, remove it → `s = "a"`.
* Finally, remove `"a"`.

Hence, 3 partitions are formed.

### Example 2

**Input:** `s = "aabaab", k = 3`
**Output:** `1`

**Explanation:** No matter which character you change, the entire string fits in one partition since it always has ≤ 3 distinct characters.

### Example 3

**Input:** `s = "xxyz", k = 1`
**Output:** `4`

**Explanation:** Changing `s[0]` to a new character (`w`) results in `"wxyz"`. Each character forms its own partition since `k = 1`.

---

## Constraints

* `1 <= s.length <= 10^4`
* `s` consists only of lowercase English letters.
* `1 <= k <= 26`

---

```python
class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        if k == 26:  # all letters fit in one partition
            return 1

        # precompute prefix partitions and masks
        p1, m1 = [0]*n, [0]*n
        p = 1; m = 0
        for i, c in enumerate(s):
            cm = 1 << (ord(c) - ord('a'))
            if bin(m | cm).count('1') > k:  # too many distinct chars
                p += 1
                m = cm
            else:
                m |= cm
            p1[i] = p; m1[i] = m

        # precompute suffix partitions and masks
        p2, m2 = [0]*n, [0]*n
        p = 1; m = 0
        for i in range(n-1, -1, -1):
            cm = 1 << (ord(s[i]) - ord('a'))
            if bin(m | cm).count('1') > k:
                p += 1
                m = cm
            else:
                m |= cm
            p2[i] = p; m2[i] = m

        ans = p2[0]
        for i in range(n):
            for j in range(26):
                ncm = 1 << j
                pb, mb = (p1[i-1], m1[i-1]) if i else (0, 0)
                pa, ma = (p2[i+1], m2[i+1]) if i+1 < n else (0, 0)
                # decide if new char starts new partition or joins previous
                if i == 0:
                    cp, cmask = 1, ncm
                else:
                    if bin(mb | ncm).count('1') > k:
                        cp, cmask = pb + 1, ncm
                    else:
                        cp, cmask = pb, mb | ncm
                t = cp + pa
                if pa and bin(cmask | ma).count('1') <= k:
                    t -= 1  # merge partitions
                ans = max(ans, t)
        return ans
```

---

### 🧩 How I Solved It — Step-by-Step

1. Precompute prefix and suffix partition counts and bitmasks for distinct letters.
2. For each possible character change, simulate how partitions are affected.
3. Use bitmask operations to count distinct characters efficiently.
4. Merge adjacent partitions if they can form one with ≤ k distinct characters.
5. Track the maximum possible partition count.

---

### 🛠️ Possible Improvements

* Optimize by reducing redundant bitmask recalculations.
* Early termination when maximum possible partitions are reached.
* Use integer popcount instead of `bin().count('1')` for faster performance.

---

### 🧠 Time & Space Complexity

* **Time Complexity:** O(26 * n) → for each position and character.
* **Space Complexity:** O(n) → prefix/suffix arrays and masks.
