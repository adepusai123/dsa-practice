def merge(A, m, B, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    https://leetcode.com/problems/merge-sorted-array/description/
    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
    Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
    The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
    """
    idx, i, j = m+n-1, m-1, n-1
    while i >= 0 and j >= 0:
        if A[i] > B[j]:
            A[idx] = A[i]
            i -= 1
        else:
            A[idx] = B[j]
            j -= 1
        idx -= 1

    # If there are remaining elements in nums2, copy them
    A[:j + 1] = B[:j + 1]

    return A

print('Ans: ', merge([1,2,3,0,0,0], 3, [2,5,6], 3)) # [1,2,2,3,5,6]