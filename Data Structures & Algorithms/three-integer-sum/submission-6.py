class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        sums = set()

        for i in range(len(nums)):
            left = 0
            right = i-1

            while left < right:
                sum = nums[left] + nums[right] + nums[i]
                if sum < 0:
                    left+=1
                elif sum > 0:
                    right-=1
                else:
                    temp = (nums[left], nums[right], nums[i])
                    sums.add(temp)
                    left += 1
                    right -= 1
            
        return list(sums)
                    