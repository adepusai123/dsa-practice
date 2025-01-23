def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    https://leetcode.com/problems/maximum-subarray/
    Kadenes algorithm
    -ve : [-1], [-3,-2,-1,-2]
    """
    max_sum = float('-inf')
    cur_sum = 0
    for i in nums:
        cur_sum += i
        max_sum = max(cur_sum, max_sum)
        if cur_sum < 0:
            cur_sum = 0
    return max_sum

print('Ans:', maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) #6