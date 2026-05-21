# Find All Numbers Disappeared in an Array

## Problem

Given an array `nums` of size `n` where:

```text
1 <= nums[i] <= n
```

Return all numbers in the range:

```text
[1, n]
```

that do not appear in the array.

---

## Examples

### Example 1

```text
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
```

---

### Example 2

```text
Input: nums = [1,1]
Output: [2]
```

---

## Constraints

- `n == nums.length`
- `1 <= n <= 10^5`
- `1 <= nums[i] <= n`

---

## Code

```cpp
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {

        vector <int> ans;

        for (int i=0; i<nums.size(); i++){

            if (nums[abs(nums[i])-1]>0){
                nums[abs(nums[i])-1]=-nums[abs(nums[i])-1];
            }
        }

        for (int i=0; i<nums.size(); i++){

            if (nums[i]>0){
                ans.push_back(i+1);
            }
        }

        return ans;
    }
};
```

---

## 🧩 How I Solved It — Step-by-Step

### 1️⃣ Use Index Marking Trick

Since:

```text
1 <= nums[i] <= n
```

every value can map directly to an index.

Example:

```text
value 1 → index 0
value 2 → index 1
```

and so on.

---

### 2️⃣ Mark Visited Numbers

For every number:

```cpp
abs(nums[i]) - 1
```

gives its corresponding index.

We mark that index as negative:

```cpp
nums[index] = -nums[index];
```

This means:
- That number exists in the array

---

### 3️⃣ Why Use abs()?

Some values may already be negative from previous marking.

So:

```cpp
abs(nums[i])
```

ensures correct indexing.

---

### 4️⃣ Find Missing Numbers

After marking:
- Positive indices represent numbers never visited

Example:

```text
nums[i] > 0
```

means:

```text
i + 1
```

is missing.

So push:

```cpp
i + 1
```

into answer.

---

## 🛠️ Possible Improvements

### Better Readability

Store index in variable:

```cpp
int index = abs(nums[i]) - 1;
```

instead of repeating expression multiple times.

---

### Why This Is Optimal

This solution:
- Uses no extra array
- Works in-place
- Achieves O(n) time

Exactly matches follow-up requirement.

---

## 🧠 Time & Space Complexity

### ⏱️ Time Complexity

```text
O(n)
```

Single traversal for marking and one for checking.

---

### 🗂️ Space Complexity

```text
O(1)
```

Ignoring output array.
