def numsSameConsecDiff(n,k):
        if n==1:
            return [x for x in range(10)]
        res=[]
        def dfs(n,num):
            if n==0:
                return res.append(num)
            tdigit = num%10
            possibility = set([tdigit+k,tdigit-k])
            for digit in possibility:
                if 0<=digit and digit<=9:
                    newNum=num*10+digit
                    dfs(n-1,newNum)
        for num in range(1,10):
            dfs(n-1,num)
        return(res)
print(numsSameConsecDiff(int(input()),int(input())))