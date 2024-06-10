'''You are given an array of positive and negative integers and a number n and n > 1. The array may have elements that occurs more than once. Find all the combinations of n elements of the array that their sum are 0.
arr = [1, -1, 2, 3, -2]
n = 3
find_zero_sum_groups(arr, n) == [-2, -1, 3] # -2 - 1 + 3 = 0

The function should ouput every combination or group in increasing order.
We may have more than one group:
arr = [1, -1, 2, 3, -2, 4, 5, -3 ]
n = 3
find_zero_sum_groups(arr, n) == [[-3, -2, 5], [-3, -1, 4], [-3, 1, 2], [-2, -1, 3]]

In the case above the function should output a sorted 2D array.
The function will not give a group twice, or more, only once.
arr = [1, -1, 2, 3, -2, 4, 5, -3, -3, -1, 2, 1, 4, 5, -3 ]
n = 3
find_zero_sum_groups(arr, n) == [[-3, -2, 5], [-3, -1, 4], [-3, 1, 2], [-2, -1, 3]]

If there are no combinations with sum equals to 0, the function will output an alerting message.
arr = [1, 1, 2, 3]
n = 2
find_zero_sum_groups(arr, n) == "No combinations"

If the function receives an empty array will output an specific alert:
arr = []
n = 2
find_zero_sum_groups(arr, n) == "No elements to combine"'''


#check if array is type of list or its less than n or n is less than 1
#Use a helper function to generate all combinations of n elements from the array
#For each combination, check if the sum is zero. If it is, add it to the set to ensure uniqueness.
#Convert the set to a sorted list of lists and return it.
def find_zero_sum_groups(arr, n):
    #check is the array is of type array
    if not type(arr) == list:
        return "Not an array"
    #check if the array is empty or len less than n
    if len(arr) < n or n < 1:
        return  "No elements to combine"
    # create a set variable to hold unique values
    result = set()
    # create a helper function to track items 
    def track_elements(start, path):
      #check if path len equal to n and sum of path is 0
      if len(path) == n:
        if sum(path) == 0:
            #add the path to the set as a tuple
            result.add(tuple(sorted(path)))
            return
      #iterate the array an recursively call track_items
      for i in range(start, len(arr)):
            track_elements(i+1, path + [arr[i]])

    track_elements(0, [])
    if not result:
        return "No combinations"
    sorted_list = sorted(list(group) for group in result)
    if len(sorted_list) == 1:
        return sorted_list[0]
    return sorted_list
        

'''print(fins_zero_sum_groups[[-3, -2, 5], [-3, -1, 4], [-3, 1, 2], [-2, -1, 3], [-2, 1, 1], [-1, -1, 2]] should equal [[-3, -2, 5], [-3, -1, 4], [-3, 1, 2], [-2, -1, 3]]'''
        

# test cases
print(find_zero_sum_groups([1, -1, 2, 3, -2, 4, 5, -3, -3, -1, 2, 1, 4, 5, -3 ], 3)) #[[-3, -2, 5], [-3, -1, 4], [-3, 1, 2], [-2, -1, 3]]
print(find_zero_sum_groups([1, -1, 2, 3, -2], 3))  # [[-2, -1, 3]]
print(find_zero_sum_groups([1, -1, 2, 3, -2, 4, 5, -3], 3))  # [[-3, -2, 5], [-3, -1, 4], [-3, 1, 2], [-2, -1, 3]]
print(find_zero_sum_groups([1, 1, 2, 3], 2))  # "No combinations"
print(find_zero_sum_groups([], 2))  # "No enough elements
print(find_zero_sum_groups('1', 3)) #not an array