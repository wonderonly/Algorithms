#Question:
#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#Example:
#Given nums = [2, 7, 11, 15], target = 9,
#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].

class Solution(object):
  def twoSum(self, nums, target):
    table = {}
    for i in range(0, len(nums)):
      diff = target - nums[i]
      if diff in table:
        return [table[diff], i]
      table[nums[i]] = i

if __name__ == "__main__":
  sol = Solution()
  print sol.twoSum([2, 7, 11, 15], 9)
