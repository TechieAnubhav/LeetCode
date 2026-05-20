# Find the Prefix Common Array of Two Arrays

## Problem

You are given two integer permutations `A` and `B` of length `n`.

A prefix common array `C` is defined such that:

```text
C[i]
```

represents the count of numbers that appear in both arrays at or before index `i`.

Return the prefix common array.

---

## Examples

### Example 1

```text
Input: A = [1,3,2,4], B = [3,1,2,4]
Output: [0,2,3,4]
```

---

### Example 2

```text
Input: A = [2,3,1], B = [3,1,2]
Output: [0,1,3]
```

---

## Constraints

- `1 <= A.length == B.length <= 50`
- `1 <= A[i], B[i] <= n`
- `A` and `B` are permutations

---

## Code

```cpp
class Solution {
public:
    vector<int> findThePrefixCommonArray(vector<int>& A, vector<int>& B) {
        vector <int> freq(50,0);
        vector <int> ans;

        int c=0;

        for (int i=0; i<A.size(); i++){

            freq[A[i]-1]++;
            freq[B[i]-1]++;

            if (A[i]==B[i]){
                c++;
                ans.push_back(c);
                continue;
            }

            if (freq[A[i]-1]==2){
                c++;
            }

            if (freq[B[i]-1]==2){
                c++;
            }

            ans.push_back(c);
        }

        return ans;
    }
};
```

---

## 🧩 How I Solved It — Step-by-Step

### 1️⃣ Use Frequency Array

We use:

```cpp
vector<int> freq(50,0);
```

to track how many times each number has appeared across both arrays.

---

### 2️⃣ Traverse Both Arrays Together

At every index `i`:

```cpp
freq[A[i]-1]++;
freq[B[i]-1]++;
```

This updates occurrences for current elements.

---

### 3️⃣ Count Common Elements

A number becomes common when its frequency reaches `2`.

Meaning:
- It has appeared once in `A`
- And once in `B`

So:

```cpp
if (freq[A[i]-1]==2)
```

or

```cpp
if (freq[B[i]-1]==2)
```

increase common count.

---

### 4️⃣ Special Case: Same Element

If:

```cpp
A[i] == B[i]
```

then both updates happen simultaneously for the same number.

So common count increases only once.

```cpp
c++;
```

Then continue directly.

---

### 5️⃣ Store Prefix Answer

At every step:

```cpp
ans.push_back(c);
```

stores the current prefix common count.

---

## 🛠️ Possible Improvements

### Use Dynamic Frequency Size

Instead of:

```cpp
vector<int> freq(50,0);
```

Could use:

```cpp
vector<int> freq(A.size()+1,0);
```

More flexible and cleaner.

---

### Better Variable Names

Instead of:

```cpp
c
```

Could use:

```cpp
commonCount
```

for readability.

---

## 🧠 Time & Space Complexity

### ⏱️ Time Complexity

```text
O(n)
```

Single traversal of both arrays.

---

### 🗂️ Space Complexity

```text
O(n)
```

Frequency array and answer array are used.
