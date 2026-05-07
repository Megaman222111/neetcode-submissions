class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        nums = {}
        numt = {}

        for x in s:
            if x in nums:
                nums[x] += 1
            else:
                nums[x] = 0
        
        for y in t:
            if y in numt:
                numt[y] +=1
            else:
                numt[y] = 0
        
        return nums==numt