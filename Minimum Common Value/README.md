# Minimum Common Value

## Problem

Given two sorted integer arrays `nums1` and `nums2`, return the minimum integer common to both arrays.

If no common integer exists, return `-1`.

---

## Examples

### Example 1

```text
Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2
```

---

### Example 2

```text
Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
Output: 2
```

---

## Constraints

- `1 <= nums1.length, nums2.length <= 10^5`
- `1 <= nums1[i], nums2[j] <= 10^9`
- Both arrays are sorted in non-decreasing order

---

## Code

```cpp
class Solution {
public:
    int getCommon(vector<int>& nums1, vector<int>& nums2) {
        int i=0, j=0;

        while (i<nums1.size() && j<nums2.size()){

            if (nums1[i]==nums2[j]){
                return nums1[i];
            }

            else if (nums1[i]>nums2[j]){
                j++;
            }

            else{
                i++;
            }
        }

        return -1;
    }
};
```

---

## 🧩 How I Solved It — Step-by-Step

### 1️⃣ Use Two Pointers

Since both arrays are already sorted:
- Use one pointer for each array

```cpp
i → nums1
j → nums2
```

---

### 2️⃣ Compare Current Elements

If:

```cpp
nums1[i] == nums2[j]
```

we found the smallest common element.

Return immediately.

---

### 3️⃣ Move Smaller Element Pointer

If:

```cpp
nums1[i] > nums2[j]
```

then:
- `nums2[j]` is too small
- Move `j`

Otherwise:
- Move `i`

This works because arrays are sorted.

---

### 4️⃣ No Common Element

If traversal finishes without finding equality:

```cpp
return -1;
```

---

## 🛠️ Possible Improvements

### Binary Search Approach

Alternative approach:
- Iterate through smaller array
- Binary search in larger array

Complexity:

```text
O(n log m)
```

But two pointers are more optimal here.

---

### Why Two Pointers Work Best

Because arrays are sorted:
- No need for nested loops
- No hashmap needed
- Linear traversal is enough

---

## 🧠 Time & Space Complexity

### ⏱️ Time Complexity

```text
O(n + m)
```

Where:
- `n = nums1.size()`
- `m = nums2.size()`

---

### 🗂️ Space Complexity

```text
O(1)
```

Only two pointers are used.
