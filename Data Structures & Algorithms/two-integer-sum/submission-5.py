class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if nums[i] in targets:
                return [targets[nums[i]], i]

            targets[complement] = i



        
        

        