def sumOddLengthSubarrays(arr):
        n = len(arr)
        return sum(
            a * ((1 + (i+1)*(n-i))//2)
            for i,a in enumerate(arr)
        )
print(sumOddLengthSubarrays([ int(x.strip()) for x in input().split(",")]))