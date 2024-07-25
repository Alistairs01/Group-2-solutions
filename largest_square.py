def isSquarePossible(A, n ,l):
    # Count how many columns have height >= l
    # A is the array of column heights
    # n is the number of columns in the array
    # l is the minimum height of a square
    count = 0
    for height in A:
        if height >= l:
            count += 1
        # If we have found enough columns, return True
        if count >= l:
            return True
    return False

def solution(A):
    n = len(A)
    left, right = 0, n
    max_side = 0
    
    while left <= right:
        mid = (left + right) // 2 #truncation to ensure the result is an integer
        
        if isSquarePossible(A, n, mid):
            max_side = mid    #(left + right) // 2
            left = mid + 1    #((left + right) // 2 ) + 1
        else:
            right = mid - 1   #((left + right) // 2) - 1
    
    return max_side

# Example usage:
A1 = [1, 2, 2, 2, 4, 4, 5]
A2 = [1, 2, 2, 4, 5]
A3 = [10, 10, 10, 10]



print(solution(A1))  # Output: 3 The largest square possible has a side length of 3
print(solution(A2))  # Output: 2 The largest possible square has a side length of 2
print(solution(A3))  # Output: 4 The largest possible square has a side length of 4

