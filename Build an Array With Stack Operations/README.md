# Build an Array With Stack Operations

## Problem

You are given:

- A strictly increasing array `target`
- An integer `n`

You have an empty stack and can perform two operations:

- `"Push"` → add the next stream number to the stack
- `"Pop"` → remove the top element

Numbers are read sequentially from the stream:

```text
1, 2, 3, ..., n
```

Return the sequence of stack operations required to build `target`.

---

## Examples

### Example 1

```text
Input: target = [1,3], n = 3
Output: ["Push","Push","Pop","Push"]
```

---

### Example 2

```text
Input: target = [1,2,3], n = 3
Output: ["Push","Push","Push"]
```

---

### Example 3

```text
Input: target = [1,2], n = 4
Output: ["Push","Push"]
```

---

## Constraints

- `1 <= target.length <= 100`
- `1 <= n <= 100`
- `1 <= target[i] <= n`
- `target` is strictly increasing

---

## Code

```cpp
class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        vector<string> ans;

        for (int i = 1, j = 0; i <= target.back(); i++) {

            ans.push_back("Push");

            if(target[j] != i){
                ans.push_back("Pop");
            }

            else {
                j++;
            }
        }

        return ans;
    }
};
```

---

## 🧩 How I Solved It — Step-by-Step

### 1️⃣ Simulate Reading the Stream

We process numbers from:

```cpp
1 → target.back()
```

No need to read beyond the largest target value because the array is already complete at that point.

---

### 2️⃣ Always Push Current Number

Whenever a number is read from the stream:

```cpp
ans.push_back("Push");
```

because every read number must first be pushed onto the stack.

---

### 3️⃣ Check Whether Number Is Needed

If current stream number equals the next target value:

```cpp
target[j] == i
```

keep it in the stack and move to the next target element.

```cpp
j++;
```

---

### 4️⃣ Remove Unwanted Numbers

If current number does not belong to target:

```cpp
target[j] != i
```

immediately remove it:

```cpp
ans.push_back("Pop");
```

This simulates discarding unwanted stream values.

---

### 5️⃣ Stop at Largest Target Element

Loop condition:

```cpp
i <= target.back()
```

ensures we stop exactly when target has been constructed.

No unnecessary stream elements are read.

---

## 🛠️ Possible Improvements

### Ignore Unused Parameter

`n` is not actually needed because:

```cpp
target.back() <= n
```

and construction stops at the last target element.

---

### Alternative Simulation

A more explicit solution could maintain a stack and simulate operations directly, but it would use unnecessary extra space.

---

## 🧠 Time & Space Complexity

### ⏱️ Time Complexity

```text
O(target.back())
```

At most one iteration for every stream number read.

---

### 🗂️ Space Complexity

```text
O(k)
```

Where:

```text
k = number of operations returned
```

excluding output storage, the algorithm itself uses:

```text
O(1)
```

extra space.
