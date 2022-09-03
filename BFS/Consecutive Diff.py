def numsSameConsecDiff(n,k):
        if n==1:
            return [x for x in range(10)]
        queue=[x for x in range(1,10)]
        
        for _ in range(n-1):
            nqueue=[]
            for num in queue:
                tdigit = num %10
                possibility = set([tdigit+k,tdigit-k])
                for digit in possibility:
                    if 0<=digit and digit<=9:
                        newNum=num*10+digit
                        nqueue.append(newNum)
            queue=nqueue
        return(queue)
print(numsSameConsecDiff(int(input()),int(input())))