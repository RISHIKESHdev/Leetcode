def canBeEqual(target,arr):
        counter = collections.defaultdict(int)
        for t in target:
            counter[t] += 1
        for a in arr:
            if a not in counter or counter[a] == 0:
                return False
            counter[a] -= 1
        return all(v == 0 for v in counter.values())
target=[ int(x.strip()) for x in input().split(",")]
arr=[ int(x.strip()) for x in input().split(",")]
print(canBeEqual(target,arr))