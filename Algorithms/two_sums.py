class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        complementMap = {}
        
        for i in range(len(nums)):
            
            num = nums[i]
            complement = target - num
            
            if num in complementMap:
                return [complementMap[num], i]
            
            else:
                complementMap[complement] = i