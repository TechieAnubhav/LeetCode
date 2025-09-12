# Vowels Game in a String

## Problem
Alice and Bob are playing a game on a string `s`. The rules are:

1. Alice starts first and removes any non-empty substring containing an **odd** number of vowels.
2. Bob goes next and removes any non-empty substring containing an **even** number of vowels.
3. The first player who cannot make a move on their turn loses the game.
4. Both players play optimally.

Return `true` if Alice wins the game, and `false` otherwise.

Vowels are 'a', 'e', 'i', 'o', 'u'.

---

## Examples

**Example 1:**
```
Input: s = "leetcoder"
Output: true
```
Explanation: Alice can start by removing a substring with an odd number of vowels and eventually win as Bob will run out of moves.

**Example 2:**
```
Input: s = "bbcd"
Output: false
```
Explanation: There are no vowels in the string, so Alice cannot make any valid move and loses.

---

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists only of lowercase English letters.

---

## Code
```python
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for i in s:
            if i in "aeiou":
                return True
        return False
```

---

## 🧩 How I Solved It — Step-by-Step
1. Observed that Alice can win if there's at least one vowel in the string.
2. Iterated through the string to check if any character is a vowel.
3. If a vowel is found, Alice can make the first move and win, so return `True`.
4. If no vowels are found, Alice has no valid move and loses, so return `False`.

---

## 🛠️ Possible Improvements
- Use a set instead of a string to check for vowels in O(1) time.
- Avoid iterating through the whole string once a vowel is found by returning immediately.

---

## 🧠 Time & Space Complexity
- **Time Complexity:** O(n), where `n` is the length of the string. We may need to scan each character once.
- **Space Complexity:** O(1), as we use a constant amount of extra space.
