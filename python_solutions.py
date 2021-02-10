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
middle_way
prev  |  next  |  chance
Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.


middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]
"""
def middle_way(a, b):
  return([a[len(a) % 2] , b[len(b) % 2]])


"""
make_ends
prev  |  next  |  chance
Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.


make_ends([1, 2, 3]) → [1, 3]
make_ends([1, 2, 3, 4]) → [1, 4]
make_ends([7, 4, 6, 2]) → [7, 2]
"""
def make_ends(nums):
  return [nums[0],nums[-1]]
  

  """"
  has23
prev  |  next  |  chance
Given an int array length 2, return True if it contains a 2 or a 3.
"""
  def has23(nums):
  return 2 in nums or 3 in nums
"""
has23([2, 5]) → True
has23([4, 3]) → True
has23([4, 5]) → False
"""

"""
 count_evens
prev  |  next  |  chance
Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0
"""
def count_evens(nums):
  return(len(list(filter(lambda x: (x%2 == 0) , nums)) )) 

"""
big_diff
prev  |  next  |  chance
Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.


big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8
"""
def big_diff(nums):
  return max(nums) - min(nums)

"""
 centered_average
prev  |  next  |  chance
Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.


centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3
"""
def centered_average(nums):
  return ( sum(nums) - max(nums) - min(nums) ) / (len(nums) - 2)

"""
sum13
prev  |  next  |  chance
Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.


sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6

"""
def sum13(nums):
  if len(nums) == 0:
    return 0
 
  for i in range(0, len(nums)):
    if nums[i] == 13:
      nums[i] = 0
      if i+1 < len(nums): 
        nums[i+1] = 0
  return sum(nums)
  
"""
 sum67
prev  |  next  |  chance
Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.


sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
"""

def sum67(nums):
  for i in range(0, len(nums)):
    if nums[i] == 6:
      nums[i] = 0
      for j in range(i+1, len(nums)):
        temp = nums[j]
        nums[j] = 0
        if temp == 7:
          i = j + 1
          break
  return sum(nums)

"""
has22
prev  |  next  |  chance
Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.


has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False
"""
def has22(nums):
 for i in range(0, len(nums)-1):
    #if nums[i] == 2 and nums[i+1] == 2:
    if nums[i:i+2] == [2,2]:
      return True    
 return False

