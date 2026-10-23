class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap=dict()
        for i in range(len(nums)):
            if target-nums[i] in myMap:
                return [myMap[target-nums[i]], i]
            else:
                myMap[nums[i]]=i