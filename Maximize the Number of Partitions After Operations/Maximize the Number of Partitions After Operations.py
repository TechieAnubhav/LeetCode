class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        if k == 26:  # all letters fit in one partition
            return 1

        # precompute prefix partitions and masks
        p1, m1 = [0]*n, [0]*n
        p = 1; m = 0
        for i, c in enumerate(s):
            cm = 1 << (ord(c) - ord('a'))
            if bin(m | cm).count('1') > k:  # too many distinct chars
                p += 1
                m = cm
            else:
                m |= cm
            p1[i] = p; m1[i] = m

        # precompute suffix partitions and masks
        p2, m2 = [0]*n, [0]*n
        p = 1; m = 0
        for i in range(n-1, -1, -1):
            cm = 1 << (ord(s[i]) - ord('a'))
            if bin(m | cm).count('1') > k:
                p += 1
                m = cm
            else:
                m |= cm
            p2[i] = p; m2[i] = m

        ans = p2[0]
        for i in range(n):
            for j in range(26):
                ncm = 1 << j
                pb, mb = (p1[i-1], m1[i-1]) if i else (0, 0)
                pa, ma = (p2[i+1], m2[i+1]) if i+1 < n else (0, 0)
                # decide if new char starts new partition or joins previous
                if i == 0:
                    cp, cmask = 1, ncm
                else:
                    if bin(mb | ncm).count('1') > k:
                        cp, cmask = pb + 1, ncm
                    else:
                        cp, cmask = pb, mb | ncm
                t = cp + pa
                if pa and bin(cmask | ma).count('1') <= k:
                    t -= 1  # merge partitions
                ans = max(ans, t)
        return ans
