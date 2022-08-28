def mergedList(list1, list2):
    sorted_list =[]
    while list1 and list2:
        if list1[0] <  list2[0]:
            sorted_list.append(list1.pop(0))
        else:
            sorted_list.append(list2.pop(0))
    sorted_list += list1
    sorted_list += list2
    
    return sorted_list

def getMedian(lis):
    mid = len(lis) // 2
    return (lis[mid] + lis[~mid]) / 2

def findMedianSortedArrays(nums1, nums2):
    sortedList = mergedList(nums1, nums2)
    return getMedian(sortedList)

nums1=[int(x.strip()) for x in input().split(",")]
nums2=[int(x.strip()) for x in input().split(",")]
print(findMedianSortedArrays(nums1, nums2))