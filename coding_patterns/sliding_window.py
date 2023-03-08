'''
Given an array consisting of n integers, find the contiguous subarray of 
given length k that has the maximum average value. And you need to output 
the maximum average value.
'''
# Example:

# Input: [1, 12, -5, -6, 50, 3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

def findMaxAverage(nums,k):
    max_average=0.0

    for i in range(len(nums) - k + 1):
        _sum = 0.0

        for j in range(i,i+k):
            _sum += nums[j]
        average = _sum/k
        max_average=max(max_average,average)
    if len(nums)==1:
        return average
    return max_average

print(findMaxAverage([1, 12, -5, -6, 50, 3],4))

# Solving using sliding window technique


def slidingWindow(nums,k):
    average = []
    _sum, start = 0,0

    for end in range(len(nums)):
        _sum += nums[end]

        if end >= k-1:
            average.append(_sum/k)
            _sum -= nums[start]
            start += 1
    return max(average)

print(slidingWindow([1, 12, -5, -6, 50, 3],4))