# Maximum Number of Words You Can Type

## Problem
There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

Given a string `text` of words separated by a single space (no leading or trailing spaces) and a string `brokenLetters` of all distinct letter keys that are broken, return the number of words in `text` you can fully type using this keyboard.

---

## Examples

**Example 1:**
```
Input: text = "hello world", brokenLetters = "ad"
Output: 1
```
**Explanation:**  
We cannot type "world" because the 'd' key is broken.

**Example 2:**
```
Input: text = "leet code", brokenLetters = "lt"
Output: 1
```
**Explanation:**  
We cannot type "leet" because the 'l' and 't' keys are broken.

**Example 3:**
```
Input: text = "leet code", brokenLetters = "e"
Output: 0
```
**Explanation:**  
We cannot type either word because the 'e' key is broken.

---

## Constraints

- `1 <= text.length <= 10^4`
- `0 <= brokenLetters.length <= 26`
- `text` consists of words separated by a single space without any leading or trailing spaces.
- Each word only consists of lowercase English letters.
- `brokenLetters` consists of distinct lowercase English letters.

---

## Code
```python
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        l = text.split()
        c = 0
        for i in l:
            s = set(i)
            for j in brokenLetters:
                if j in s:
                    break
            else:
                c += 1
        return c
```

---

## 🧩 How I Solved It — Step-by-Step
1. Split the input `text` into individual words.
2. For each word, checked if any broken letter exists in that word.
3. If a word doesn't contain any broken letters, incremented the count.
4. Used a `set` for each word to optimize membership checks.
5. Returned the count of typeable words.

---

## 🛠️ Possible Improvements
- Convert `brokenLetters` to a `set` once at the beginning to further speed up lookups.
- Avoid repeatedly converting each word to a set.

---

## 🧠 Time & Space Complexity

- **Time Complexity:** O(n * k), where n is the number of words and k is the average length of a word.
- **Space Complexity:** O(k), used for storing each word as a set during the iteration.
