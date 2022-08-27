class Solution:
    
    def maxHeap(self, arr, n):
        if self.lt(n)>=len(arr):
            return
        self.maxHeap(arr, self.lt(n))
        if self.rt(n)>=len(arr):
            if arr[self.lt(n)]>arr[n]:
                arr[self.lt(n)], arr[n] = arr[n], arr[self.lt(n)]
            return
        self.maxHeap(arr, self.rt(n))
        mx = max(arr[n], arr[self.lt(n)], arr[self.rt(n)])
        if arr[n]==mx:
            return
        elif arr[self.lt(n)]==mx:
            arr[n], arr[self.lt(n)] = arr[self.lt(n)], arr[n]
        else:
            arr[n], arr[self.rt(n)] = arr[self.rt(n)], arr[n]
        return
        
            
    def maintainHeap(self, arr):
        i = 0
        while True:
            lt = self.lt(i)
            rt = self.rt(i)
            if rt<len(arr):
                mx = max(arr[i], arr[lt], arr[rt])
                if arr[i]==mx:
                    return
                elif arr[lt]==mx:
                    arr[lt],arr[i]=arr[i],arr[lt]
                    i=lt
                else:
                    arr[rt],arr[i]=arr[i],arr[rt]
                    i=rt
            elif lt<len(arr):
                mx = max(arr[i], arr[lt])
                if arr[i]==mx:
                    return
                else:
                    arr[lt],arr[i]=arr[i],arr[lt]
                    return
            else:
                return
            
            
    def findKthLargest(self, nums, k):
        self.lt = lambda x:int((2*x)+1)
        self.rt = lambda x:int((2*x)+2)
        self.pt = lambda x:int((x-1)/2)
        for i in range(int(math.log(len(nums))+1)):
            self.maxHeap(nums, 0)
        res = None
        for i in range(k):
            res = nums[0]
            nums[0] = nums[len(nums)-1]
            nums.pop()
            self.maintainHeap(nums)
        return res

ans= Solution()
nums = [ int(x.strip()) for x in input().split(",")]
k=int(input())
print(ans.findKthLargest(nums,k))