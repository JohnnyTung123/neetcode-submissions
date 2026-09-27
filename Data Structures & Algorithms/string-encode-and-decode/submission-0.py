class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + '#' + s
        
        return res

    def decode(self, s: str) -> List[str]:
        n = len(s)
        i = 0
        res = []

        while i < n:
            # get the length
            j = i

            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            # get the string
            t = s[j+1 : j+1+length]

            # append the string and ready for the next iteration
            res.append(t)
            i = j + 1 + length
        
        return res
            
