def backspaceCompare(s,t):
        def nextValid(string,i):
            backspace = 0
            while backspace >= 0:
                i -= 1
                if i < 0: return -1
                if string[i] == "#": backspace += 1
                else: backspace -= 1
            return i
        
        p, q = len(s), len(t)
        while p >= 0 and q >= 0:
            p, q = nextValid(s, p), nextValid(t, q)
            if p >= 0 and q >= 0 and s[p] != t[q]: return False
        return (p < 0 and q < 0) or (p == q == 0)
print(backspaceCompare(input(),input()))