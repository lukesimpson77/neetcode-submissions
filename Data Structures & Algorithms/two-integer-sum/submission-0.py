class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSet = set()

        for i in range(len(nums)):
            goal = target - nums[i]
            if goal in hashSet:
                for j in range(0,i):
                    if nums[j] == goal:
                        list = [j,i]
                        return list
            hashSet.add(nums[i])