#2sum should match the given target 
#brutefore = would be to verify every number with the next and other nuber to optimise this we rater see the need of number remaining
class Solution:
      def twoSum(self, nums, target):
      #store already read numbers 
          read = {}

          for i, a in enumerate(nums):
         # number required to reach the target
              remaining = target - a
         # if that x number was seen before return 
              if remaining in read:
                  return [read[remaining], i]
         #store it 
              read[a] = i
         # else return null 
          return [] 
