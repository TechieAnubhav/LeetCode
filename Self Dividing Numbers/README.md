# Self Dividing Numbers

## Problem

A self-dividing number is a number that is divisible by every digit it
contains.

Rules: - The number must not contain the digit 0. - Every digit must
divide the number evenly.

Given two integers `left` and `right`, return a list of all the
self-dividing numbers in the range `[left, right]` (inclusive).

------------------------------------------------------------------------

## Examples

### Example 1

Input: left = 1, right = 22\
Output: \[1,2,3,4,5,6,7,8,9,11,12,15,22\]

### Example 2

Input: left = 47, right = 85\
Output: \[48,55,66,77\]

------------------------------------------------------------------------

## Constraints

-   `1 <= left <= right <= 10^4`

------------------------------------------------------------------------

## Code

``` cpp
class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        int c = 0, flag = 0;
        vector<int> arr;

        for (int i = left; i <= right; i++) {
            int t = i;

            while (t > 0) {
                int r = t % 10;

                if (r == 0) {
                    flag = 1;
                    break;
                }

                if (i % r != 0) {
                    flag = 1;
                    break;
                }

                t = t / 10;
            }

            if (flag == 1) {
                flag = 0;
                continue;
            }

            arr.push_back(i);
        }

        return arr;
    }
};
```

------------------------------------------------------------------------

## 🧩 How I Solved It --- Step-by-Step

### 1️⃣ Iterate Through the Range

We loop from `left` to `right` and check each number individually.

------------------------------------------------------------------------

### 2️⃣ Extract Digits One by One

For each number: - Store it in a temporary variable `t` - Extract digits
using:

t % 10

-   Remove last digit using:

    t = t / 10

------------------------------------------------------------------------

### 3️⃣ Check Two Conditions

For each digit `r`:

1.  If `r == 0` → Not allowed → Stop checking.
2.  If `number % r != 0` → Not divisible → Stop checking.

If either condition fails, we mark it invalid.

------------------------------------------------------------------------

### 4️⃣ Add Valid Numbers

If all digits pass the checks, push the number into the result vector.

------------------------------------------------------------------------

## 🛠️ Possible Improvements

### Cleaner Flag Handling

Instead of using `flag`, we could use a boolean variable:

``` cpp
bool valid = true;
```

This improves readability.

------------------------------------------------------------------------

### Slight Optimization

Since the maximum range is only `10^4`, this brute-force solution is
efficient enough.

------------------------------------------------------------------------

## 🧠 Time & Space Complexity

### ⏱️ Time Complexity

O(n × d)

Where: - `n = right - left` - `d` = number of digits (at most 5)

Since `right <= 10^4`, this is very efficient.

------------------------------------------------------------------------

### 🗂️ Space Complexity

O(k)

Where `k` is the number of self-dividing numbers found.
