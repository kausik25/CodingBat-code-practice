List-1 > first_last6
"""
gven an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.

first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False
"""
def first_last6(nums):
  return 6 in [nums[0],nums[-1]]

""""
same_first_last

Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.


same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True
"""
def same_first_last(nums):
  return len(nums) > 0 and nums[0] == nums[-1]
  
"""
common_end
prev  |  next  |  chance
Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.


common_end([1, 2, 3], [7, 3]) → True
common_end([1, 2, 3], [7, 3, 2]) → False
common_end([1, 2, 3], [1, 3]) → True
"""

def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]
 """
 sum3
prev  |  next  |  chance
Given an array of ints length 3, return the sum of all the elements.


sum3([1, 2, 3]) → 6
sum3([5, 11, 2]) → 18
sum3([7, 0, 0]) → 7
"""
def sum3(nums):
  return sum(nums)
  
  """
  rotate_left3
prev  |  next  |  chance
Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.


rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]

"""
def rotate_left3(nums):
  return [nums[(i+1) % len(nums)] for i,x in enumerate(nums)]

""""
  > reverse3
prev  |  next  |  chance
Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.


reverse3([1, 2, 3]) → [3, 2, 1]
reverse3([5, 11, 9]) → [9, 11, 5]
reverse3([7, 0, 0]) → [0, 0, 7]
"""
def reverse3(nums):
  return nums[::-1]

"""
max_end3
prev  |  next  |  chance
Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.


max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]
"""
def max_end3(nums):
    return [max(nums[0],nums[-1])]*3

"""
sum2
prev  |  next  |  chance
Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.


sum2([1, 2, 3]) → 3
sum2([1, 1]) → 2
sum2([1, 1, 1, 1]) → 2

"""
def sum2(nums):
  return nums[0] + nums[1] if len(nums) > 1 else sum(nums)

"""

  
