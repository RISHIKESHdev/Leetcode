def findTwoSum(nums, target):
  d = {}
  n = len(nums)
  for i in range(n):
    m = target - nums[i]
    if m in d:
      return [d[m],i]
    d[nums[i]] = i
arr = [ int(x.strip()) for x in input().split(",")]
target=int(input())
print(findTwoSum(arr, target))