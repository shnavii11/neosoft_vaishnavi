#2sum should match the given target 
class Solution:
      def twoSum(self, nums, target):
          read = {}

          for i, a in enumerate(nums):
              remaining = target - a

              if remaining in read:
                  return [read[remaining], i]

              read[a] = i

          return [] 
