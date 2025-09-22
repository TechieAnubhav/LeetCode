# Count Elements With Maximum Frequency

## Problem
You are given an array `nums` consisting of positive integers.  

Return the total frequencies of elements in `nums` such that those elements all have the maximum frequency.  

The frequency of an element is the number of occurrences of that element in the array.  

## Examples

### Example 1
Input: `nums = [1,2,2,3,1,4]`  
Output: `4`  
Explanation:  
- The elements `1` and `2` both appear 2 times, which is the maximum frequency.  
- So, total count = `2 + 2 = 4`.  

### Example 2
Input: `nums = [1,2,3,4,5]`  
Output: `5`  
Explanation:  
- All elements appear once, so max frequency = `1`.  
- Since there are 5 elements, the total is `5`.  

## Constraints
- 1 <= nums.length <= 100  
- 1 <= nums[i] <= 100  

## Code
```python
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = [0] * 101
        maxFreq = 0
        
        for num in nums:
            freq[num] += 1
            maxFreq = max(maxFreq, freq[num])
        
        ans = 0
        for f in freq:
            if f == maxFreq:
                ans += maxFreq
        return ans
```

## 🧩 How I Solved It — Step-by-Step
1. Created a frequency array `freq` of size 101 since `nums[i] <= 100`.  
2. Counted the frequency of each number while tracking the maximum frequency.  
3. Iterated through `freq` to add up counts of elements that had frequency equal to `maxFreq`.  
4. Returned the sum.  

## 🛠️ Possible Improvements
- Use Python’s `collections.Counter` for shorter code.  
- Could also use a dictionary if numbers weren’t bounded by 100.  

## 🧠 Time & Space Complexity
- **Time Complexity:** O(n + k), where n = length of nums and k = range of values (100).  
- **Space Complexity:** O(k), fixed at 101 for the frequency array.  
