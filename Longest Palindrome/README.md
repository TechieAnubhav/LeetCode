# Longest Palindrome

## Problem
Given a string `s` which consists of lowercase or uppercase letters, return the **length of the longest palindrome** that can be built with those letters.

Letters are **case sensitive**, for example, `"Aa"` is not considered a palindrome.

---

## Examples

**Example 1:**
```
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
```

**Example 2:**
```
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
```

---

## Constraints
- 1 <= s.length <= 2000  
- s consists of lowercase and/or uppercase English letters only.

---

## Code
```python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd=0
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
            if d[i]%2==1:
                odd+=1
            else:
                odd-=1
        if odd>1:
            return len(s)-odd+1
        return len(s)
```

---

🧩 **How I Solved It — Step-by-Step**
1. Used a dictionary to count occurrences of each character.  
2. Tracked the number of characters with odd frequencies.  
3. If there’s more than one odd frequency, one can be placed in the middle of the palindrome, so subtract the extras.  
4. Return the length of the longest palindrome.

---

🛠️ **Possible Improvements**
- Use `collections.Counter` for cleaner counting.  
- Could be optimized to run faster for very long strings by early exits when odd count becomes minimal.

---

🧠 **Time & Space Complexity**
- **Time Complexity:** O(n), where n is the length of `s`.  
- **Space Complexity:** O(1), since the alphabet size is fixed (only uppercase + lowercase English letters).
