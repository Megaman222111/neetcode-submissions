class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = {}
        nums.sort()

        for x in range(len(nums)):
            for y in range(x, -1, -1):
                l=y+1
                r=x-1

                while (l<r):
                    if (nums[l]+nums[r]+nums[x]+nums[y])==target:
                        res[nums[l], nums[r], nums[x], nums[y]] = 0
                    if nums[l]+nums[r]+nums[x]+nums[y]>target:
                        r-=1
                    else:
                        l+=1
        
        wha = []

        for item in res:
            wha.append(list(item))

        return wha