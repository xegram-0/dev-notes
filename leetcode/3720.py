# Working
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - ord('a')] += 1

        def next_char(cnt, c):
            x = ord(c) - ord('a')

            for i in range(x + 1, 26):
                if cnt[i]:
                    return chr(ord('a') + i)

            return None

        tmp = cnt[:]
        j = -1

        for i, c in enumerate(target):
            nxt = next_char(tmp, c)

            if nxt:
                j = i

            x = ord(c) - ord('a')

            if tmp[x] == 0:
                break

            tmp[x] -= 1

        if j == -1:
            return ""

        ans = []

        # Match target before j
        for i in range(j):
            ans.append(target[i])
            cnt[ord(target[i]) - ord('a')] -= 1

        # Make position j strictly larger
        c = next_char(cnt, target[j])
        ans.append(c)
        cnt[ord(c) - ord('a')] -= 1

        # Smallest possible suffix
        for i in range(26):
            ans.append(chr(ord('a') + i) * cnt[i])

        return "".join(ans)
      
# Reference
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        # Consume as much of target's prefix as the multiset allows.
        p = 0
        while p < n:
            c = ord(target[p]) - 97
            if cnt[c] == 0:
                break
            cnt[c] -= 1
            p += 1

        i = p
        while i >= 0:
            if i < n:
                t = ord(target[i]) - 97
                pick = -1
                for c in range(t + 1, 26):
                    if cnt[c] > 0:
                        pick = c
                        break
                if pick >= 0:
                    cnt[pick] -= 1
                    tail = ''.join(chr(97 + c) * cnt[c] for c in range(26))
                    cnt[pick] += 1
                    return target[:i] + chr(97 + pick) + tail
            i -= 1
            if i >= 0:
                cnt[ord(target[i]) - 97] += 1
        return ""

        
# Attempted
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        ans = []
        ansdict = {}

        if len(s) != len(target):
            return ""

        for char in s:
            ansdict[char] = ansdict.get(char, 0) + 1

        for i in range(len(s)):
            if target[i] in ansdict:
                ansdict[target[i]] -= 1

                if ansdict[target[i]] == 0:
                    del ansdict[target[i]]

                ans.append(target[i])

            else:
                # Find the smallest available character
                # greater than target[i]
                bigger = None

                for char in ansdict:
                    if char > target[i]:
                        if bigger is None or char < bigger:
                            bigger = char

                if bigger is None:
                    # Can't make the answer greater here.
                    # We need to go backward.
                    break

                ans.append(bigger)
                ansdict[bigger] -= 1

                if ansdict[bigger] == 0:
                    del ansdict[bigger]

                # Put remaining characters in sorted order
                for char in sorted(ansdict):
                    ans.extend([char] * ansdict[char])

                return ''.join(ans)

        return ""


