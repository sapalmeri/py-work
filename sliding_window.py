# O(n) solution for finding
# maximum sum of a subarray of size k
  
  
def maxSum(arr, k):
    # length of the array
    n = len(arr)
  
    # n must be greater than k
    if n < k:
        print("Invalid")
        return -1
  
    # Compute sum of first window of size k
    window_sum = sum(arr[:k])
  
    # first sum available
    max_sum = window_sum
  
    # Compute the sums of remaining windows by
    # removing first element of previous
    # window and adding last element of
    # the current window.

    # arr = [|1, 4, 2, 10,| 2, 3, 1, 0, 20]
    # n = 9
    # k = 4
    # for i in range(5)
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        #      18  =       17   -   1    +    2
        #   17     =      18     -    4   +    3
        #   16     =      17     -   2       + 1
        max_sum = max(window_sum, max_sum)
        #   18             18   ,   17
        #   18             17   , 18
        #   18             16   , 18
    return max_sum
  
# Driver code
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
print(maxSum(arr, k))