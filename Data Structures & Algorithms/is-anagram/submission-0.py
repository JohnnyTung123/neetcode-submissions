class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m != n: return False

        s_count = {}
        t_count = {}

        for i in range(m):
            s_count[s[i]] = s_count.get(s[i], 0) + 1
            t_count[t[i]] = t_count.get(t[i], 0) + 1

        for key, val in s_count.items():
            if t_count.get(key, 0) < val:
                return False
        
        return True