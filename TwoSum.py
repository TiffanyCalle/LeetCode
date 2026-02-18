class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {}

        for index,value in enumerate(nums):
            complement = target - value
            if complement in hash_map:
                return (index, hash_map[complement])
            hash_map[value] = index
            