from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lnums = len(nums)
        cnt = 0
        i = 0
        
        while i < len(nums):
            if nums[i] == 0:
                del nums[i]
                cnt += 1
                
            else:
                i += 1
                
        nums += [0] * cnt

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    Solution().moveZeroes(nums)
    print(nums)