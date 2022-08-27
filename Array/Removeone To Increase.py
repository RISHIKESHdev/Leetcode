def canBeIncreasing(nums):
        removed=False
        for i in range(len(nums)-1):
            if(nums[i]<nums[i+1]):
                continue
            if(removed):
                return False
            if(i==0 or nums[i-1]<nums[i+1]):
                nums[i]=nums[i+1]
            else:
                nums[i+1]=nums[i]
            removed=True
        return True
print(canBeIncreasing([ int(x.strip()) for x in input().split(",")]))