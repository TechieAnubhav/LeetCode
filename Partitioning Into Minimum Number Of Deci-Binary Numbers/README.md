# Partitioning Into Minimum Number Of Deci-Binary Numbers

## Problem

A decimal number is called **deci-binary** if each of its digits is
either `0` or `1` without any leading zeros.

Examples: - `101` and `1100` are deci-binary. - `112` and `3001` are not
deci-binary.

You are given a string `n` representing a positive decimal integer.

Return the **minimum number of positive deci-binary numbers** needed so
that they sum up to `n`.

------------------------------------------------------------------------

## Examples

### Example 1

**Input:**

    n = "32"

**Output:**

    3

**Explanation:**

    10 + 11 + 11 = 32

------------------------------------------------------------------------

### Example 2

**Input:**

    n = "82734"

**Output:**

    8

------------------------------------------------------------------------

### Example 3

**Input:**

    n = "27346209830709182346"

**Output:**

    9

------------------------------------------------------------------------

## Constraints

-   `1 <= n.length <= 10^5`
-   `n` consists only of digits.
-   `n` does not contain leading zeros.
-   `n` represents a positive integer.

------------------------------------------------------------------------

## Code

``` cpp
class Solution {
public:
    int minPartitions(const string& n) {
        char m = n[0];
        for (int i = 0; i < n.size(); i++) {
            if (n[i] > m) {
                m = n[i];
            }
        }
        return m - '0';
    }
};
```

------------------------------------------------------------------------

## 🧩 How I Solved It --- Step-by-Step

### Step 1: Key Insight

Each deci-binary number can contribute at most `1` to any digit
position.

If a digit in `n` is `5`, we need at least `5` deci-binary numbers. If a
digit is `9`, we need at least `9`.

So the answer equals the **maximum digit** in the string.

------------------------------------------------------------------------

### Step 2: Find Maximum Digit

Traverse the string and track the maximum character. Convert it to
integer using `m - '0'`.

------------------------------------------------------------------------

### Step 3: Return Result

Return the maximum digit as the minimum partitions required.

------------------------------------------------------------------------

## 🛠️ Possible Improvements

1.  Early exit if digit `'9'` is found.
2.  Use STL:

``` cpp
return *max_element(n.begin(), n.end()) - '0';
```

------------------------------------------------------------------------

## 🧠 Time & Space Complexity

### Time Complexity

O(n)

### Space Complexity

O(1)
