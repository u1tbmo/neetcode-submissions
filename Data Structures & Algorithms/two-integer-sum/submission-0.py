class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, n in enumerate(nums):
            nums_dict[n] = i
        for i, n in enumerate(nums):
            remaining = target - n
            if remaining in nums_dict and nums_dict[remaining] != i:
                return [i, nums_dict[remaining]]
        return []
