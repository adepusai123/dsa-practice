def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
        1. find pivot. arr[i] < arr[i+1]
        2. swap pivot with last index (since last index is smallest number)
        3. pivot + 1, next element reverse them to get least number
        4. if not pivot return -1

    https://leetcode.com/problems/next-permutation/
    Input: nums = [1,2,3]
    Output: [1,3,2]
    """
    n = len(nums)
    # Step 1: Find the first decreasing element
    i = n-2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    
    if i >= 0:    
    # Step 2: Find the smallest element larger than nums[i]
        j = n-1
        while nums[j] <= nums[i]:
            j -= 1
        # Step 3: Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]

    # Step 4: Reverse the suffix
    nums[i + 1:] = reversed(nums[i + 1:])

    return nums


print('Ans: ', nextPermutation([1,2,3])) # [1,3,2]