class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = set()
        for num in nums:
            hash.add(num)
        if len(hash) < len(nums):
            return True
        else:
            return False