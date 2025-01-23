def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    Two pointers approach
    https://leetcode.com/problems/find-the-duplicate-number/
    Input: nums = [1,3,4,2,2]
    Output: 2
    """
    # Phase 1: Detect the cycle
    tortoise = nums[0]
    hare = nums[0]

    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    
    # Phase 2: Find the cycle start
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return hare


print('Ans: ', findDuplicate([1,3,4,2,2])) # 2