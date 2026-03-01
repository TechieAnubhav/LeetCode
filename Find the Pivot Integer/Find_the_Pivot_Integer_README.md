# Find the Pivot Integer

## Problem

Given a positive integer `n`, find the pivot integer `x` such that:

The sum of all elements between `1` and `x` inclusively equals the sum
of all elements between `x` and `n` inclusively.

Return the pivot integer `x`. If no such integer exists, return `-1`.

It is guaranteed that there will be at most one pivot integer for the
given input.

------------------------------------------------------------------------

## Examples

### Example 1

**Input:**

    n = 8

**Output:**

    6

**Explanation:**

    1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21

------------------------------------------------------------------------

### Example 2

**Input:**

    n = 1

**Output:**

    1

**Explanation:**

    1 = 1

------------------------------------------------------------------------

### Example 3

**Input:**

    n = 4

**Output:**

    -1

**Explanation:**\
It can be proven that no such integer exists.

------------------------------------------------------------------------

## Constraints

-   `1 <= n <= 1000`

------------------------------------------------------------------------

## Code

``` cpp
class Solution {
public:
    int pivotInteger(int& n) {
        double a = sqrt((n * (n + 1)) / 2);
        if (a - ceil(a) == 0) {
            return int(a);
        }
        else {
            return -1;
        }
    }
};
```

------------------------------------------------------------------------

## 🧩 How I Solved It --- Step-by-Step

### Step 1: Mathematical Observation

We want:

Sum from 1 to x = Sum from x to n

Using:

Sum(1 to k) = k(k + 1) / 2

After simplification:

x² = n(n + 1)/2

So:

x = sqrt(n(n + 1)/2)

------------------------------------------------------------------------

### Step 2: Perfect Square Check

If `n(n+1)/2` is a perfect square → pivot exists.\
Otherwise → return -1.

------------------------------------------------------------------------

### Step 3: Final Logic

-   Compute total sum
-   Take square root
-   If integer → return it
-   Else → return -1

------------------------------------------------------------------------

## 🛠️ Possible Improvements

1.  Avoid floating point precision:
    -   Compute totalSum
    -   Let x = sqrt(totalSum)
    -   Check if x \* x == totalSum
2.  Remove reference parameter since modification is unnecessary.

------------------------------------------------------------------------

## 🧠 Time & Space Complexity

### Time Complexity

O(1)

### Space Complexity

O(1)
