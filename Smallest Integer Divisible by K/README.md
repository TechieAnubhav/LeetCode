# Smallest Integer Divisible by K

## Problem

Given a positive integer `k`, find the length of the smallest positive
integer `n` such that:

-   `n` is divisible by `k`
-   `n` contains only the digit `1`

Return the length of `n`.\
If no such number exists, return `-1`.

⚠️ Note: `n` can be extremely large and may not fit into a 64-bit signed
integer.

------------------------------------------------------------------------

## Examples

### Example 1

Input: k = 1\
Output: 1\
Explanation: The smallest number is 1.

### Example 2

Input: k = 2\
Output: -1\
Explanation: No number made only of 1s is divisible by 2.

### Example 3

Input: k = 3\
Output: 3\
Explanation: 111 is divisible by 3.

------------------------------------------------------------------------

## Constraints

-   `1 <= k <= 10^5`

------------------------------------------------------------------------

## Code

``` cpp
class Solution {
public:
    int smallestRepunitDivByK(int k) {
        if (k % 2 == 0 || k % 5 == 0) {
            return -1;
        }

        int rem = 0;
        int i = 0;

        while (i <= k) {
            rem = ((rem * 10) + 1) % k;
            i++;

            if (rem == 0) {
                return i;
            }
        }

        return -1;
    }
};
```

------------------------------------------------------------------------

## 🧩 How I Solved It --- Step-by-Step

### 1️⃣ Key Mathematical Observation

A number made only of `1`s (repunit) looks like:

1\
11\
111\
1111\
...

Instead of building the full number (which would overflow), we track
only the remainder modulo `k`.

If at any step:

remainder == 0

That means the current repunit is divisible by `k`.

------------------------------------------------------------------------

### 2️⃣ Important Edge Case

If `k` is divisible by:

-   `2`
-   `5`

Then the answer is impossible.

Reason: - A number made only of 1s is always odd → cannot be divisible
by 2\
- It never ends in 0 or 5 → cannot be divisible by 5

So we immediately return `-1`.

------------------------------------------------------------------------

### 3️⃣ Remainder Simulation

Instead of constructing the full number:

111

We simulate using:

rem = (previous_rem \* 10 + 1) % k

This keeps values small and avoids overflow.

------------------------------------------------------------------------

### 4️⃣ Why We Iterate At Most k Times

There are only `k` possible remainders:

0, 1, 2, ..., k-1

If we don't hit remainder `0` within `k` iterations, we will enter a
cycle.

By the Pigeonhole Principle, if a solution exists, we must find it
within `k` steps.

------------------------------------------------------------------------

## 🛠️ Possible Improvements

### Cleaner Loop

We can write:

``` cpp
for (int i = 1; i <= k; i++)
```

Instead of using a while loop.

------------------------------------------------------------------------

## 🧠 Time & Space Complexity

### ⏱️ Time Complexity

O(k)

We iterate at most `k` times.

### 🗂️ Space Complexity

O(1)

Only a few integer variables are used.
