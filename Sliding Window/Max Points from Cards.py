def maxScore(cardPoints, k):
        total_sum = sum(cardPoints)
        length = len(cardPoints) - k
        sum_subarray = sum(cardPoints[:length])
        result = total_sum - sum_subarray
        for i in range(1, len(cardPoints)-length+1):
            sum_subarray = sum_subarray + cardPoints[i+length-1] - cardPoints[i-1]
            result = max(result, total_sum - sum_subarray)
        return result
print(maxScore([int(x.strip()) for x in input().split(",")],int(input())))