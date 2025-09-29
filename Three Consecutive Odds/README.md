# Three Consecutive Odds

## Problem
Given an integer array `arr`, return `true` if there are three consecutive odd numbers in the array. Otherwise, return `false`.

## Examples
**Example 1:**
```
Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
```

**Example 2:**
```
Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.
```

## Constraints
- 1 <= arr.length <= 1000  
- 1 <= arr[i] <= 1000  

## Code
```python
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            if arr[i] % 2 == 1 and arr[i+1] % 2 == 1 and arr[i+2] % 2 == 1:
                return True
        return False
```

## 🧩 How I Solved It — Step-by-Step
1. Loop through the array until the third-last element (since we check triples).  
2. For each index `i`, check if `arr[i]`, `arr[i+1]`, and `arr[i+2]` are all odd numbers.  
3. If such a triple is found, return `True`.  
4. If no triple is found by the end of the loop, return `False`.  

## 🛠️ Possible Improvements
- Could use a sliding window counter to track consecutive odd numbers, resetting when an even appears. This makes the logic a bit cleaner.  

## 🧠 Time & Space Complexity
- **Time Complexity:** O(n), where `n` is the length of the array.  
- **Space Complexity:** O(1), as only constant extra space is used.  
